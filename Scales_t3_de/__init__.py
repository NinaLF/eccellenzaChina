import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest3_de'
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
    

       
    generalFeedback = models.StringField(max_length=3000, blank=True, label='Haben Sie irgendwelche Kommentare, Rückmeldungen oder Ideen? Danke für Ihre Ideen und Ihr Feedback.')
    
    

     
class BehaviorsFood(Page):
    form_model = 'player'
    form_fields= ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5', 'footprint_food_overall6']
    
    
class BehaviorsTransport(Page):
    form_model = 'player'
    form_fields= ['footprint_commute_car', 'footprint_commute_car2',  'footprint_commute_car_type', 'footprint_commute_pt']
         
class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]

class End(Page):
     form_model = 'player'
     
       



page_sequence = [ # BehaviorsFlying,  BehaviorsFood2,BehaviorsTransport, BehaviorsFood, BehaviorLaundry,
                  policyScales, BehaviorsFood, BehaviorsTransport, End 
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]