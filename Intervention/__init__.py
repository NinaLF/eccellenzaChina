from otree.api import *
from otree.api import BaseGroup
from statistics import mean

doc = """
intervention
"""

class Constants(BaseConstants):
    name_in_url = 'carbon_footprint'
    players_per_group = None
    num_rounds = 1
    behavior_data = {
   
      
         "<b>Diet </b> <br> Based on an average adults' caloric needs for the duration of one year": {
                "Meat-based": 2.206,
                "Vegetarian ": 1.338
                
            },
            "<b>Drying clothes</b> <br> based on 3 drying loads per week and the average energy mix": {
                "air dry clothes": 0.0,
                "use dryer (average dryer and full load)": 0.039
            },
            "<b>Recycling</b>  <br>  Materials such as paper, glass, metals for one year ": {
                "Does not recycle": 0.0575,
                "Recycles": 0.0
            },
            "<b>Food</b>  <br>Foods and bevarages bought and consumed for one year ": {
                "more than 3/4 is regional": 0.0,
                "more than 3/4 is imported": 0.44
            },
            "<b>Commute</b> <br> 12.5 miles to and from work everyday (one trip = 6.25 miles), 5 days a week for 48 weeks per year": {
                "by bus": 0.471,
                "by car": 1.595
            },
            "<b>Travel to go on vacation</b>   ": {
                "1 round-trip 3-6 hour flight (=2 flights)": 1.2,
                "via train (does not fly)": 0.0076
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
    group_assignment = itertools.cycle(["active", "control","active", "control", "passive"])
    for player in subsession.get_players():
        if subsession.round_number == 1:
            player.participant.group_assignment = next(group_assignment)


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
        choices=[['10', 'Agree completely (10)'], ['9', '9'],['8', '8'],['7', '7'],
                 ['6', '6'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

    diet = models.StringField(choices=["Meat-based", "Vegetarian" ] )
    laundry = models.StringField(choices=["Air Dry Clothes", "Use Dryer (average dryer and full load)"] )
    recycling = models.StringField(choices=["Does Not Recycle", "Recycles"] )
    food = models.StringField(choices=["Only Regional", "Regional and Imported"] )
    commute = models.StringField(choices=["By Bus", "By Car"] )
    vacation = models.StringField(choices=["Flies Twice a Year", "via train (does not fly)"] )

    controlQuestion1 = models.StringField(label="How much tons CO<sub>2</sub> does the highest footprint emit for these combinations?",
                                          choices=["2.54", "3.07", "4.24","5.54", "6.07" ])
    
    controlQuestion2 = models.StringField(label="Which behavior change contributes most to the overall size of the footprint (i.e., causes the highest <b>change</b> in the carbon footprint)?",
                                          choices=["Meat or plant-based diet", "Air drying clothes or dryer", "Recycling or not","Regional or imported food", "Car or bus commute", "Flying or taking train"  ] )
    
    controlQuestion3 = models.StringField(label="Which behavior's impact where you most surprised by, either due to having a smaller or bigger impact than you expected?",
                                          choices=["Meat or plant-based diet", "Air drying clothes or dryer", "Recycling or not","Regional or imported food", "Car or bus commute", "Flying or taking train"  ] )
    


    pretest_engaging = make_field('engaging')
    pretest_interesting = make_field('interesting')
    pretest_understandable = make_field('understandable')
    pretest_knowledge = make_field('helpful to increase my knowledge')


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
                 Control, Control2, Control3, PretestQuestions]


