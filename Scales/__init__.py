import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'panel_study'
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

def make_likert9():
        return models.IntegerField(
            choices=[-1,0,1,2,3,4,5,6,7],
            widget=widgets.RadioSelect,
            label= 'label'
        )

def make_likert5():
        return models.IntegerField(
            choices=[1,2,3,4,5],
            widget=widgets.RadioSelect,
            label= 'label'
        )
def make_likert4():
        return models.IntegerField(
            choices=[1,2,3,4],
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
    ### Climate Change Concern Scale by Tobler et al. 2012
  
    ### Climate Change Emotions Scale based on Knauf 2022 and Truelove 2012
    emoAng1 = make_likert10() ## Anger
    emoAng2 = make_likert10() ## Anger
    emoAng3 = make_likert10() ## Anger
    emoSad1 = make_likert10() ## Sadness
    emoSad2 = make_likert10() ## Sadness
    emoSad3 = make_likert10() ## Sadness
    emoFear1 = make_likert10() ## Fear/
    emoFear2 = make_likert10() ## Fear
    emoFear3 = make_likert10() ## Fear
    emoHope1 = make_likert10() ## Hope
    emoHope2 = make_likert10() ## Hope
    emoHope3 = make_likert10() ## Hope
    emoGuilt1 = make_likert10() ## guilt
    emoGuilt2 = make_likert10() ## guilt
    emoGuilt3 = make_likert10() ## guilt
    emoConcern1 = make_likert10() ## concern
    emoConcern2 = make_likert10() ## concern
    emoConcern3 = make_likert10() ## concern

    
    
    ### IB Values
    ibv1 = make_likert9()
    ibv2 = make_likert9()
    ibv3 = make_likert9()
    ibv4 = make_likert9()

    ## trust in own and foreign governments
    
    pit1 = make_likert10()
    pit2 = make_likert10()


    ### Belief
    belief1Happening= make_likert_n(10)

    beliefHuman1 = make_likert_n(10)
    beliefHuman2 = make_likert_n(10)
    beliefHuman3 = make_likert_n(10)

    beliefConseqences1 = make_likert_n(10)
    beliefConseqences2 = make_likert_n(10)
    beliefConseqences3 = make_likert_n(10)


    ## behaviors


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
    footprint_flying_short = models.IntegerField(min=0, max= 300, label = "How many <b> short-distance flights (<3 hours)</b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from San Francisco to Los Angeles and back this counts as 2 flights. </i> " )
    footprint_flying_mid = models.IntegerField(min=0, max= 300 , label = "How many <b> mid-distance flights (3-6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from New York to San Francisco and back this counts as 2 flights. </i> ")
    footprint_flying_long = models.IntegerField(min=0, max= 300, label= "How many <b> long-distance flights (>6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from Miami to London and back this counts as 2 flights. </i> " )

    footprint_commute_car =  models.StringField(label= "How many miles do you annually drive in a car  or on a motorcycle (outside of work times, both driving and as a passenger)?", widget=widgets.RadioSelect,
                                                choices = [['never' , ' I never use a car or motorcycle'],
                                                           ['less_than_A', '1 - 1,244 miles'], 
                                                           ['A_to_B',  '1,245 - 4,659 miles'],
                                                           ['B_to_C' ,'4,660 - 7,769 miles'],
                                                           ['C_to_D' , '7,770 - 18,640 miles'],
                                                           ['more_than_D',  'more than 18,640 miles']],
                                                  )
    

    footprint_commute_car_type=  models.StringField( label = 'Which kind of fuel does your car operate on?', widget=widgets.RadioSelect ,
                                                    choices = [  ['none', 'I do not have a car' ],
                                                        ['Electric_green',  'Electric (green energy)'  ],
                                                        ['Eletric_conv', 'Electric (conventional energy) ' ],
                                                        ['Biogas', 'Biogas' ],
                                                        ['NaturalGas',  'Natural gas' ],
                                                        ['Diesel', 'Gasoline/Diesel/Hybrid' ]]
                                                   )
    footprint_commute_pt =  models.StringField(label="How many miles do you commute weekly in public transport (train, bus, etc.)or an e-bike? Please calculate all private journeys including the work commute, but not business travels." ,
                                                widget=widgets.RadioSelect , 
                                               choices = [ ['lessA', '1 - 39 miles' ],
                                               ['AtoB',  '40 - 50 miles' ],
                                               ['BtoC', '50 -149 miles'  ],
                                               ['CtoD', '150 - 224 miles' ],
                                               ['DtoE',  '225 - 370 miles' ],
                                               ['most', 'more than 370 miles'  ] ] )

    footprint_regional =  models.StringField(label = ' What percentage of your food is regional (from within your country or region, not imported) ? ', widget=widgets.RadioSelect ,
                                             choices = [  [ 'less_than' , 'Less than a quarter'],
                                                        ['quarter' , 'About a quarter'  ],
                                                        [  'half' , 'About half'  ],
                                                        [  'three_quarter' , 'About three quarters' ],
                                                        [  'more_than' , 'the largest part is regional'] ]
                                             
                                             )
    
    footprint_electricity =  models.StringField( label = 'This question is about your electricity supply. What does your electricity supply look like?',
                                             choices = [  [ 'A' , 'I dont know'],
                                                        ['B',  ' I have a conventional (fossil) supply'] ,
                                                        ['C',  'I partly have green electricity (mixed)' ] ,
                                                        ['D',  'I have green electricity entirely ' ] 
                                                        ], 
                                                        widget=widgets.RadioSelect ,
                                                       
                                                )

    ## policy scales
    policy_commute = make_field('Increase or introduce taxes on fuel for vehicles (i.e. diesel and gasoline)')
    policy_flying = make_field('Increase or introduce taxes on air travel.')
    policy_electricity = make_field('Increase or introduce taxes on fossil fuels as energy source (i.e. gas, oil, and coal)')  
    policy_diet = make_field('Increase or introduce taxes on red meat (e.g., beef, lamb, veal).')
    policy_recycling = make_field( 	'Increase or introduce taxes on non-recyclable materials')
    policy_regional = make_field('Increase or introduce taxes on food products imported via plane')
    

 # demographics
    age = models.IntegerField(label='How old are you', min=18, max=90)
    
    gender = models.StringField( label='How do you identify?',
        choices=[['Male', 'Male'], ['Female', 'Female'], 
        ['prefer not to answer/ diverse', 'prefer not to answer/ diverse']],
        widget = widgets.RadioSelect
    )
    education = models.StringField( label='What is your <b>highest education</b>?',
        choices=[['No formal education', 'No formal education'],
                ['Compulsory education', 'Compulsory education (secondary school)'], 
                 ['Further education', 'Further education'],
                 ['Higher education (Bachelor, Master, PhD)', 'Higher education (Bachelor, Master, PhD)']],
                 widget = widgets.RadioSelect
    )

    income = models.StringField(
                                label='How high is your <b>yearly personal income before tax </b>?',
        choices=[['< 18.000£', '< 18.000£'],
                 ['18.000£ to 23.000£', '18.000£ to 23.000£'], 
                 ['23.001£ to 30.500£', '23.001£ to 30.500£'], 
                 ['30.501£ to 45.000£', '30.500£ to 45.000£'], 
                 ['> 45.001£', '> 45.001£']],
                  widget = widgets.RadioSelect
    )
    polOrientation =  models.IntegerField( widget=widgets.RadioSelect,  
                                          choices=[['1', 'extremely left (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'extremely right (10)'] ] ) 

    climate_change_concern1 = make_field('I worry about the climate´s state.')
    climate_change_concern2 = make_field('Climate protection is important for our future.')
    climate_change_concern3 = make_field('We must protect the climate´s delicate equilibrium.')
    climate_change_concern4 = make_field('Climate change has severe consequences for humans and nature.')

    UnitUnderstanding =  models.IntegerField( widget=widgets.RadioSelect,  label="How much difficulty did you have understanding and imaging 'kg' ",
                                          choices=[['1', 'no problem with the unit (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', ' lots of difficulty (10)'] ] ) 

    
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     

class Belief(Page):
    form_model = 'player'
    form_fields= [ 'belief1Happening' ]

class Belief1(Page):
     form_model = 'player'
     form_fields= [ 'beliefHuman1', 'beliefHuman2', 'beliefHuman3',
                   'beliefConseqences1', 'beliefConseqences2', 'beliefConseqences3']

class ClimateConcern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3', 'climate_change_concern4']


class CCEmotion(Page):
    form_model = 'player'
    form_fields= ['emoAng1', 'emoAng2', 'emoAng3', 'emoSad1','emoSad2', 'emoSad3', 'emoFear1', 'emoFear2', 'emoFear3', 'emoHope1', 'emoHope2', 'emoHope3', 'emoGuilt1', 'emoGuilt2', 'emoGuilt3', 'emoConcern1', 'emoConcern2', 'emoConcern3']
  
    
class BehaviorsFood(Page):
    form_model = 'player'
    form_fields= ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5', 'footprint_food_overall6']
    
class BehaviorsFood2(Page):
    form_model = 'player'
    form_fields= [ 'footprint_regional', 'footprint_electricity']
    
class BehaviorsTransport(Page):
    form_model = 'player'
    form_fields= ['footprint_commute_car', 'footprint_commute_car_type', 'footprint_commute_pt']
    

class BehaviorsFlying(Page):
    form_model = 'player'
    form_fields= [ 'footprint_flying_short', 'footprint_flying_mid', 'footprint_flying_long']
   

class IBValues(Page):
    form_model = 'player'
    form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4']
    
class PITrust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2']
   
class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]
   
class unit(Page):
    form_model = 'player'
    form_fields= ['UnitUnderstanding']
    
class Demographics(Page):
     form_model = 'player'
     form_fields= [ 'age', 'gender', 'education', 'income', 'polOrientation' ]
       

class End(Page):
     form_model = 'player'
       



page_sequence = [  BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, policyScales, ClimateConcern, unit, Demographics, End
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]