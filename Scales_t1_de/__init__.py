import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest1_de'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



#region functions
def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
            label= 'label'
        )

#endregion



#endregion
def make_likert_n(n):
    nchoices = list(range(1, n+1))
    return models.IntegerField(
        choices=nchoices,
        widget=widgets.RadioSelect,
)



class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
        choices=[['10', 'Agree completely (10)'], ['9', '9'],['8', '8'],['7', '7'],
                 ['6', '6'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )
  

    ## trust in own and foreign governments
    
    pit1 = make_likert10()
    pit2 = make_likert10()

    ## behaviors


    footprint_food_overall1 =  models.StringField(widget=widgets.RadioSelect , 
                                                  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label='Rindfleisch')
    
    footprint_food_overall2 =  models.StringField(widget=widgets.RadioSelect,
                                                    choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label = 'Lamm oder Hammelfleisch' )
    
    footprint_food_overall3 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Schweinefleisch')
    
    footprint_food_overall4 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Geflügel (z.B. Huhn)')
    
    footprint_food_overall5 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ] ] , label= 'Fisch')
    
    footprint_food_overall6 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Milchprodukte (z.B. Milch oder Käse)' )

    # further behavior items
    
    
    footprint_commute_car =  models.IntegerField( min=0, max=1000 , 
                                                 label= "Wie viele Kilometer sind Sie an einem typischen <b>Arbeitstag in den letzten 2 Wochen mit dem Auto gependelt (als Fahrer oder Beifahrer)</b>, um zur Arbeit zu gelangen? <br> Bitte geben Sie die durchschnittlichen Kilometer <b> pro Arbeitstag </b> an")
                                                
    footprint_commute_car2 =  models.IntegerField( min=0, max=1000 , 
                                                 label= "Wie viele Kilometer sind Sie durchschnittlich <b>in den letzten 2 Wochen für andere Zwecke (als Fahrer oder Beifahrer) </b>für Freizeitaktivitäten, Besorgungen/Einkäufe oder andere Gründe gefahren? <br> Bitte geben Sie die durchschnittlichen Kilometer <b> pro Tag </b> an")
                                                
    footprint_commute_car_type=  models.StringField( label = 'Welche Art von Kraftstoff nutzt Ihr Auto?', widget=widgets.RadioSelectHorizontal ,
                                                    choices = [  ['none', 'Ich habe kein Auto' ],
                                                        ['Electric_green',  'Elektrisch (grüne Energie)'  ],
                                                        ['Eletric_conv', 'Elektrisch (konventionelle Energie)' ],
                                                        ['Biogas', 'Biogas' ],
                                                        ['NaturalGas',  'Erdgas' ],
                                                        ['Diesel', 'Benzin/Diesel/Hybrid' ]]
                                                   )
    footprint_commute_pt =  models.IntegerField(min=0, max=1000 , 
                                                label="Wie viele Kilometer sind Sie <br>in den letzten 2 Wochen pro Tag mit öffentlichen Verkehrsmitteln (Zug, Bus usw.) gependelt</b>? Bitte berechnen Sie alle privaten Fahrten einschließlich des Arbeitswegs, aber keine Geschäftsreisen <b>basierend auf einem Tag.</b>" )
                                               
                                  
                                                
    ## policy scales
    policy_commute =make_field('Erhöhung oder Einführung von Steuern auf Kraftstoff für Fahrzeuge (z. B. Diesel und Benzin). ')
    policy_flying =make_field(	'Erhöhung oder Einführung von Steuern auf Flugreisen.')
    policy_electricity =make_field('Erhöhung oder Einführung von Steuern auf fossile Brennstoffe als Energiequelle (z. B. Gas, Öl und Kohle).')
    policy_diet =	make_field('Erhöhung oder Einführung von Steuern auf rotes Fleisch (z. B. Rindfleisch, Lammfleisch, Kalbfleisch).')
    policy_recycling =	make_field('Erhöhung oder Einführung von Steuern auf nicht wiederverwertbare (=nicht recyclebare) Materialien.')
    policy_regional =	make_field('Erhöhung oder Einführung von Steuern auf Lebensmittelprodukte, die per Flugzeug importiert werden.')
    
    
## https://www.researchgate.net/publication/29870461_Need_for_cognition_Eine_Skala_zur_Erfassung_von_Engagement_und_Freude_bei_Denkaufgaben_Presentation_and_validation_of_a_German_version_of_the_Need_for_Cognition_Scale
    nfc_1 = make_field('Ich würde komplizierte Probleme einfachen Problemen vorziehen.')
    nfc_2 = make_field('Ich trage nicht gerne die Verantwortung für eine Situation, die sehr viel Denken erfordert.')
    nfc_3 = make_field('Denken entspricht nicht dem, was ich unter Spass verstehe.') # reverse coded
    nfc_4 = make_field('Ich würde lieber etwas tun, das wenig Denken erfordert, als etwas, das mit Sicherheit meine Denkfähigkeit herausfordert.') # reverse coded
    nfc_5 = make_field('Die Aufgabe, neue Lösungen für Probleme zu finden, macht mir wirklich Spass.')
    nfc_6 = make_field('Ich würde lieber eine Aufgabe lösen, die Intellegenz erfordert, schwierig und bedeutend ist, als eine Aufgabe, die zwar irgendwie wichtig ist, aber nicht viel Nachdenken erfordert.')

    numeracy1 = models.IntegerField(min=0, max=100,   blank=True)

    numeracy2a = models.IntegerField(min=0, max=50,   blank=True)
    numeracy2b = models.IntegerField(min=0, max=70,   blank=True)
    numeracy3 = models.IntegerField(min=0, max=100,   blank=True)

    responsibility =make_likert10()


    UnitUnderstanding =  models.IntegerField( widget=widgets.RadioSelect,  label="Wie schwierig war es für Sie, „kg CO<sub>2</sub> “ zu verstehen und sich vorzustellen? ",
                                          choices=[['1', ' gar nicht schwierig (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'sehr schwierig(10)'] ] ) 
    
    generalFeedback = models.StringField(max_length=3000, blank=True, label='Haben Sie irgendwelche Kommentare, Rückmeldungen oder Ideen? Danke für Ihre Ideen und Ihr Feedback.')
    
    
    
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     


class BehaviorsFood(Page):
    form_model = 'player'
    form_fields= ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5', 'footprint_food_overall6']
    
    
class BehaviorsTransport(Page):
    form_model = 'player'
    form_fields= ['footprint_commute_car', 'footprint_commute_car2',  'footprint_commute_car_type', 'footprint_commute_pt']
         
    
class Trust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2', 'responsibility']
    form_field_labels = ['lokale Regierung', 'nationale Regierung', '']

class NFC(Page):
    form_model = 'player'
    form_fields= ['nfc_1', 'nfc_2', 'nfc_3', 'nfc_4', 'nfc_5', 'nfc_6' ]

class Numeracy(Page):
    form_model = 'player'
    form_fields= ['numeracy1']


class Numeracy2a(Page):
    form_model = 'player'
    form_fields= ['numeracy2a']
    
    def is_displayed(player: Player):
        return player.field_maybe_none('numeracy1') not in [None, 25]
    
class Numeracy2b(Page):
    form_model = 'player'
    form_fields= ['numeracy2b']
    
    def is_displayed(player: Player):
        return player.field_maybe_none('numeracy1')  in [ 25]
    
    def before_next_page(player:Player, timeout_happened):
        player.numeracy2b= player.numeracy2b

class Numeracy3(Page):
    form_model = 'player'
    form_fields= ['numeracy3']

    def is_displayed(player: Player):
        num2b = player.field_maybe_none('numeracy2b')
        return num2b != 20
   

class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]
   

class unit(Page):
    form_model = 'player'
    form_fields= [ 'generalFeedback']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        gender = player.participant.vars.get('gender')
        age = player.participant.vars.get('age')

        # Gender update
        if gender == 'Female':
            session.num_female_de += 1
        elif gender == 'Male':
            session.num_male_de += 1

        # Age bin update
        if 18 <= age <= 29:
            session.num_age1_de += 1
        elif 30 <= age <= 44:
            session.num_age2_de += 1
        elif 45 <= age <= 59:
            session.num_age3_de += 1
        elif 60 <= age <= 80:
            session.num_age4_de += 1
       

class End(Page):
     form_model = 'player'
       


page_sequence = [ # BehaviorsFlying,  BehaviorsFood2,BehaviorsTransport, BehaviorsFood,
               policyScales, BehaviorsTransport, BehaviorsFood, Trust,NFC,  Numeracy, Numeracy2a, Numeracy2b, Numeracy3, 
               unit, End 
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]