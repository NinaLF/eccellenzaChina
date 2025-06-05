import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest2_de'
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
  

    ## policy scales
    policy_commute =make_field('Erhöhung oder Einführung von Steuern auf Kraftstoff für Fahrzeuge (z. B. Diesel und Benzin). ')
    policy_flying =make_field(	'Erhöhung oder Einführung von Steuern auf Flugreisen.')
    policy_electricity =make_field('Erhöhung oder Einführung von Steuern auf fossile Brennstoffe als Energiequelle (z. B. Gas, Öl und Kohle).')
    policy_diet =	make_field('Erhöhung oder Einführung von Steuern auf rotes Fleisch (z. B. Rindfleisch, Lammfleisch, Kalbfleisch).')
    policy_recycling =	make_field('Erhöhung oder Einführung von Steuern auf nicht wiederverwertbare (=nicht recyclebare) Materialien.')
    policy_regional =	make_field('Erhöhung oder Einführung von Steuern auf Lebensmittelprodukte, die per Flugzeug importiert werden.')
    

       
    UnitUnderstanding =  models.IntegerField( widget=widgets.RadioSelect,  label="Wie schwierig war es für Sie, „kg CO<sub>2</sub> “ zu verstehen und sich vorzustellen? ",
                                          choices=[['1', ' gar nicht schwierig (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'sehr schwierig(10)'] ] ) 
    
    generalFeedback = models.StringField(max_length=3000, blank=True, label='Haben Sie irgendwelche Kommentare, Rückmeldungen oder Ideen? Danke für Ihre Ideen und Ihr Feedback.')
    
    

    subjectiveKnowledgePost = models.IntegerField(widget=widgets.RadioSelect,  label= 'Wie kenntnisreich fühlen Sie sich über die Auswirkungen verschiedener Verhaltensweisen auf den CO<sub>2</sub>-Fußabdruck? Das heißt, wie viel denken Sie wissen Sie, über die Menge an CO<sub>2</sub>-Emissionen, die durch verschiedene Handlungen verursacht wird?',
                                              choices=[['1', 'überhaupt nicht viel (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', 'sehr viel (7)'] ]   )
    responsibility =make_likert10()

     

class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]
   
class unit(Page):
    form_model = 'player'
    form_fields= [ 'subjectiveKnowledgePost', 'generalFeedback', 'responsibility']
    

class End(Page):
     form_model = 'player'
     
       



page_sequence = [ # BehaviorsFlying,  BehaviorsFood2,BehaviorsTransport, BehaviorsFood, BehaviorLaundry,
                  policyScales, unit, End 
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]