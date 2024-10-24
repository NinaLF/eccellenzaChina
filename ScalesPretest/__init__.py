import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'study'
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

    def make_fieldQ(label):
        return models.IntegerField(
        choices=[['1', 'Not at all (1)'], ['2', '3'],['3', '3'],['4', '4'],
                 ['5', '5'], ['6', '6'],  ['7', '7'],
                   ['8', '8'],['9', '9'], ['10',  'Very much(10)'] ] ,
                           
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )
    ### Climate Change Concern Scale by Tobler et al. 2012



  
    ### Belief
    belief1Happening= make_likert_n(10)


    ## behaviors



    # further behavior items
    footprint_flying_short = models.IntegerField(min=0, max= 300, 
                                                 label = "How many <b> short-distance flights (<3 hours)</b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from San Francisco to Los Angeles and back this counts as 2 flights. </i> " )
    
    

    footprint_commute_car_type=  models.StringField( label = 'Which kind of fuel does your car operate on?', widget=widgets.RadioSelectHorizontal ,
                                                    choices = [  ['none', 'I do not have a car' ],
                                                        ['Electric_green',  'Electric (green energy)'  ],
                                                        ['Eletric_conv', 'Electric (conventional energy) ' ],
                                                        ['Biogas', 'Biogas' ],
                                                        ['NaturalGas',  'Natural gas' ],
                                                        ['Diesel', 'Gasoline/Diesel/Hybrid' ]]
                                                   )



    subjectiveKnowledge = models.StringField( label= '  How knowledgeable do you feel about the effect of different behaviors on carbon footprints. That is, how much do you feel you know about how many CO<sub>2</sub> emissions are caused by differen actions?',
                                              choices=[['1', 'not much at all (1)'], ['2', '3'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', '7'], ['8', '8'],['9', '9'], ['10', 'A great deal (10)'] ]   )

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
    
    ## questions about interventions
    intervention1 = make_fieldQ('How interesting did you find the information and the way it was presented?')
    intervention2 = make_fieldQ('How engaging did you find the material and the way it was presented?')  
    intervention3 = make_fieldQ('How understandable did you find the information and the way it was presented?')
    intervention4 = make_fieldQ('How helpful did you find the format of information presentation for understanding and remembering the information?')
    intervention5 = make_fieldQ('How interested are you in the information that was presented?')


    nfc1 = make_field('I would prefer complex to simple problem')
    nfc2 = make_field('I like to have the responsibility of handling a situation that requires a lot of thinking')
    nfc3 = make_field('Thinking is not my idea of fun.') # reverse coded
    nfc4 = make_field('I would rather do something that requires little thought than something that is sure to challenge my thinking abilities.') # reverse coded
    nfc5 = make_field('I really enjoy a task that involves coming up with new solutions to problems.')
    nfc6 = make_field('I would prefer a task that is intellectual, difficult, and important to one that is somewhat important but does not require much thought')

    numeracy1 = models.IntegerField(min=0, max=100, label='Please provide a percentage between 0 and 100')

    generalFeedback = models.StringField(max_length=3000, blank=True, label='Do you have any comments, feedback or ideas? Thanks for sharing.')
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     

class Belief(Page):
    form_model = 'player'
    form_fields= [ 'belief1Happening' , 'polOrientation']


class ClimateConcern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3', 'climate_change_concern4']


class NFC(Page):
    form_model = 'player'
    form_fields= ['nfc1', 'nfc2', 'nfc3', 'nfc4', 'nfc5', 'nfc6' ]

class Numeracy(Page):
    form_model = 'player'
    form_fields= ['numeracy1']
   
class QuestionsIntervention(Page):
     form_model = 'player'
     form_fields= [ 'intervention1', 'intervention2', 'intervention3', 'intervention4' , 'intervention5']

class Feedback(Page):
     form_model = 'player'
     form_fields= ['subjectiveKnowledge', 'generalFeedback']




class Demographics(Page):
     form_model = 'player'
     form_fields= [ 'age', 'gender', 'education', 'income', 'polOrientation' ]


class End(Page):
     form_model = 'player'
       



page_sequence = [ # BehaviorsFlying,  BehaviorsFood2,BehaviorsTransport, BehaviorsFood, BehaviorLaundry,
                   QuestionsIntervention, Feedback, NFC, ClimateConcern, Belief, Numeracy, End
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]