from otree.api import *
from otree.api import BaseGroup
from statistics import mean

doc = """
intervention
"""

class Constants(BaseConstants):
    name_in_url = 'carbon_footprint_calc'
    players_per_group = None
    num_rounds = 1
    behavior_data = {
   
      
         "<b>Ernährungsverhalten </b> <br> basierend auf dem durchschnittlichen Kalorienbedarf von 2000kcal eines Erwachsenen für 1 Jahr": {
                "Fleischbasiert": 2.206,
                "Vegetarisch ": 1.338
                
            },
            "<b>Wäsche trocknen</b> <br> basierend auf 3 Ladungen pro Woche für 1 Jahr und einem durchschnittlichen Energiemix ": {
                "lässt die Wäsche lufttrocknen": 0.0,
                "benutzt den Trockner (durchschnittlicher Trockner und vollbeladen)": 0.039
            },
            "<b>Recycling</b>  <br> Materialien wie Papier, Glas, Metalle für ein Jahr ": {
                "Recycelt nicht": 0.0575,
                "Recycelt": 0.0
            },
            "<b>Lebensmittel</b>  <br> gekaufte und verbrauchte Lebensmittel und Getränke für 1 Jahr <br> ": {
                "more than 3/4 is regional": 0.0,
                "more than 3/4 is imported": 0.44
            },
            "<b>Arbeitsweg</b> <br> 20 Kilometer täglich zur und von der Arbeit (eine Fahrt =10km), 5 Tage pro Woche während 48 Wochen pro Jahr": {
                "by bus": 0.471,
                "by car": 1.595
            },
            "<b>Urlaub</b>  <br>  ": {
                "fliegt 1 Hin- und Rückflug von 3-6 Stunden (=2 Flüge, z.B. Zürich-Marrakesch, Zurich-Antalya) ": 1.2,
                "Per Zug (fliegt nicht, z. B. Zürich-Paris oder London)": 0.0076
            }
    }

    control_data = {
   
      
         "Streckendistanz von Frankfurt (Fahrstrecke nicht Luftlinie)": {
                "Frankfurt-Düsseldorf": 226,
                "Frankfurt-Berlin ": 548
            },
            "Streckendistanz von Berlin (Fahrstrecke nicht Luftlinie)": {
                "Berlin-Saarbrücken": 723,
                "Berlin-Köln": 575
            },
            "Streckendistanz von München (Fahrstrecke nicht Luftlinie)": {
                "München-Hamburg": 793,
                "München-Osnabrück": 641
            },
            "Streckendistanz von Hannover (Fahrstrecke nicht Luftlinie)": {
                "Hannover-Dresden": 364,
                "Hannover-Frankfurt": 569
            },
             "Streckendistanz von Stuttgart (Fahrstrecke nicht Luftlinie)": {
                "Stuttgart-Bonn": 350,
                "Stuttgart-Erfurt": 339
            },
             "Streckendistanz von Wiesbaden (Fahrstrecke nicht Luftlinie)": {
                "Wiesbaden-Nürnberg": 253,
                "Wiesbaden-Berlin": 573
            }
    }


class Subsession(BaseSubsession):


    def get_completed_count(self):
        players = self.get_players()
        return sum(1 for p in players if p.participant.group_assignment == "active" )

  
class Group(BaseGroup):
    pass

def creating_session(subsession:Subsession):

    import itertools
    group_assignment = itertools.cycle([ "active", "control", "passive"])
    for player in subsession.get_players():
        if subsession.round_number == 1:
            player.participant.group_assignment = next(group_assignment)


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
        choices=[['10', 'Stimme absolut zu (10)'], ['9', '9'],['8', '8'],['7', '7'],
                 ['6', '6'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Stimme absolute nicht zu (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


    diet = models.StringField(choices=["Fleischbasierte Ernährung", "Vegetarische Ernährung"] )
    laundry = models.StringField(choices=["trocknet Wäsche an der Luft", "benutzt den Wäschetrockner (durchschnittlicher Trockner und volle Ladung)"] )
    recycling = models.StringField(choices=["Recycelt nicht", "Recycelt"] )
    food = models.StringField(choices=["Nur regionale Lebensmittel", "Regionale und importierte Lebensmittel"] )
    commute = models.StringField(choices=["Mit dem Bus", "Mit dem Auto"] )
    vacation = models.StringField(choices=["Fliegt zweimal im Jahr", "Mit dem Zug (fliegt nicht)"] )

    controlQuestion1 = models.StringField(label="Wie viele Tonnen CO<sub>2</sub> verursacht der höchste Fussabdruck für diese Kombinationen?",
                                        choices=["2.54", "3.07", "4.24", "5.54", "6.07"] )

    controlQuestion2 = models.StringField(label="Welche Verhaltensänderung trägt am meisten zur Gesamtgrösse des Fussabdrucks bei (d.h. verursacht die grösste <b>Veränderung</b> im CO<sub>2</sub>-Fussabdruck)?",
                                        choices=["Fleischbasierte oder pflanzenbasierte Ernährung", "Wäsche an der Luft trocknen oder Trockner", "Recycling oder nicht", "Regionale oder importierte Lebensmittel", "Pendeln mit Auto oder Bus", "Fliegen oder Zugfahren"] )

    controlQuestion3 = models.StringField(label="Bei welchem Verhalten waren Sie am meisten überrascht über dessen Auswirkungen – entweder weil sie grösser oder kleiner waren als erwartet?",
                                        choices=["Fleischbasierte oder pflanzenbasierte Ernährung", "Wäsche an der Luft trocknen oder Trockner", "Recycling oder nicht", "Regionale oder importierte Lebensmittel", "Pendeln mit Auto oder Bus", "Fliegen oder Zugfahren"] )

    pretest_engaging = make_field('spannend')
    pretest_interesting = make_field('interessant')
    pretest_understandable = make_field('verständlich')
    pretest_knowledge = make_field('hilfreich für die Erweiterung meines Wissens')



# PAGES
class TaskInfo(Page):
    pass


class ActiveSamplingOld(Page):
    #def is_displayed(self):
        #return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class ActiveSamplingIntro(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "active"
    
class ActiveSampling(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class ActiveSampling2(Page):
    form_model = "player"
    form_fields= [ 'controlQuestion1', 'controlQuestion2' , 'controlQuestion3']
  
    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class ActiveSampling3(Page):
  
    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class PassiveSampling(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "passive"
    
class PassiveSampling2(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "passive"
    
class PassiveSampling3(Page):
    form_model = "player"
    form_fields= [ 'controlQuestion1' , 'controlQuestion2', 'controlQuestion3']
    def is_displayed(self):
        return self.participant.group_assignment == "passive"
    

class Transition(Page):
    pass

class PretestQuestions(Page):

    def is_displayed(self):
        return self.participant.group_assignment != "control"

    form_model = 'player'
    form_fields= ['pretest_engaging', 'pretest_interesting', 'pretest_understandable', 'pretest_knowledge' ]



class Control(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'control_data': Constants.control_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class Control2(Page):
    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'control_data': Constants.control_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class Control3(Page):
  
    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})

        return {
            'control_data': Constants.control_data
    
        }
    
page_sequence = [ActiveSamplingIntro, ActiveSampling, ActiveSampling3, ActiveSampling2 , 
                 # ActiveSamplingOld, 
                 PassiveSampling, PassiveSampling2, PassiveSampling3, 
                 Control, Control2, Control3,
                 PretestQuestions]


