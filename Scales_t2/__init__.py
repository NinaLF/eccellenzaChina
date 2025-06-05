import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest2'
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
    policy_commute = make_field('Increase or introduce taxes on fuel for vehicles (i.e. diesel and gasoline)')
    policy_flying = make_field('Increase or introduce taxes on air travel.')
    policy_electricity = make_field('Increase or introduce taxes on fossil fuels as energy source (i.e. gas, oil, and coal)')  
    policy_diet = make_field('Increase or introduce taxes on red meat (e.g., beef, lamb, veal).')
    policy_recycling = make_field( 	'Increase or introduce taxes on non-recyclable materials')
    policy_regional = make_field('Increase or introduce taxes on food products imported via plane')
    


    UnitUnderstanding =  models.IntegerField( widget=widgets.RadioSelect,  label="How much difficulty did you have understanding and imagining 'kg' CO<sub>2</sub> ",
                                          choices=[['1', 'no problem with the unit (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', ' lots of difficulty (10)'] ] ) 
    
    generalFeedback = models.StringField(max_length=3000, blank=True, label='Do you have any comments, feedback or ideas? Thanks for sharing.')
    
    
    subjectiveKnowledgePost = models.IntegerField(widget=widgets.RadioSelect,  label= '  How knowledgeable do you feel about the effect of different behaviors on carbon footprints. That is, how much do you feel you know about how many CO<sub>2</sub> emissions are caused by differen actions?',
                                              choices=[['1', 'not much at all (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', 'A great deal (7)'] ]   )
    
    responsibility =make_likert10()




    
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     
   

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