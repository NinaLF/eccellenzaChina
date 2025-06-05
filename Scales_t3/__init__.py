import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest3'
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
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ]] , label='Beef')
    
    footprint_food_overall2 =  models.StringField(widget=widgets.RadioSelect,
                                                    choices = [
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ]] , label = 'Lamb or mutton' )
    footprint_food_overall3 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ]] , label= 'Pork')
    footprint_food_overall4 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ]] , label= 'Poultry (e.g. chicken)')
    footprint_food_overall5 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ] ] , label= 'Fish')
    footprint_food_overall6 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Never'],
        ['oncePerMonth', 'Once a month' ],
        ['2-3PerMonth',  '2-3 times per month'],
        ['oncePerWeek',  'Once a week' ],
        ['2-3PerWeek', '2-3 times per week' ],
        ['4-6PerWeek',  '4-6 times per week' ],
        ['oncePerDay',  'Once a day'  ],
        ['MultiplePerDay', '2 or more times per day'  ]] , label= 'Dairy products (e.g milk or cheese)' )

    # further behavior items

    footprint_commute_car =  models.IntegerField( min=0, max=1000 , 
                                                 label= "How many miles by <b>car did you commute on a typical working day in the past 2 weeks </b>(as a driver or passenger) to get to work? <br> Please enter the average miles <b> per working day </b>")
                                               
    footprint_commute_car2 =  models.IntegerField( min=0, max=1000 , 
                                                 label= "How many miles by <b>car did you drive on average for other purposes </b>(as a driver or passenger) for leisure activities, chores/groceries or other reasons? <br> Please enter the average miles <b> per day </b>")
                                                                                     

    footprint_commute_car_type=  models.StringField( label = 'Which kind of fuel does your car operate on?', widget=widgets.RadioSelectHorizontal ,
                                                    choices = [  ['none', 'I do not have a car' ],
                                                        ['Electric_green',  'Electric (green energy)'  ],
                                                        ['Eletric_conv', 'Electric (conventional energy) ' ],
                                                        ['Biogas', 'Biogas' ],
                                                        ['NaturalGas',  'Natural gas' ],
                                                        ['Diesel', 'Gasoline/Diesel/Hybrid' ]]
                                                   )
    footprint_commute_pt =  models.IntegerField(min=0, max=1000 ,
                                                 label="How many miles did you <b>commute per week in the past 2 weeks using public transport (train, bus, etc.) </b>or an e-bike? Please calculate all private journeys including the work commute, but not business travels <b>based on one week.</b>" )
                            
    ## policy scales
    policy_commute = make_field('Increase or introduce taxes on fuel for vehicles (i.e. diesel and gasoline)')
    policy_flying = make_field('Increase or introduce taxes on air travel.')
    policy_electricity = make_field('Increase or introduce taxes on fossil fuels as energy source (i.e. gas, oil, and coal)')  
    policy_diet = make_field('Increase or introduce taxes on red meat (e.g., beef, lamb, veal).')
    policy_recycling = make_field( 	'Increase or introduce taxes on non-recyclable materials')
    policy_regional = make_field('Increase or introduce taxes on food products imported via plane')
    



    generalFeedback = models.StringField(max_length=3000, blank=True, label='Do you have any comments, feedback or ideas? Thanks for sharing.')
    




    
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     
   
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