import random

from otree.api import *


doc = """
How to translate an app to multiple languages (e.g. English and German).

There are 2 ways to define localizable strings:
(1) Put it in a "lexicon" file (see lexicon_en.py, lexicon_de.py).
    This is the easiest technique, and it allows you to easily reuse the same string multiple times.
(2) If the string contains variables, then it should to be defined in the template.
    Use an if-statement, like {{ if de }} Nein {{ else }} No {{ endif }}

When you change the LANGUAGE_CODE in settings.py, the language will automatically be changed.

Note: this technique does not require .po files, which are a more complex technique.    
"""


class C(BaseConstants):
    NAME_IN_URL = 'panel_study'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def creating_session(subsession:Subsession):
    
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon
        subsession.session.myLangCode = "_de"
    elif subsession.session.config['language'] == 'zh_hans':
        from .lexicon_zh_hans import Lexicon
        subsession.session.myLangCode = "_ch"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.scalesLexi = Lexicon 


#region many very redundant functions 
def make_likert7():
    return models.IntegerField(
        choices=[1,2,3,4,5,6,7],
            widget=widgets.RadioSelect,
    )

def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
        )
def make_likert11():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10, 22],
            widget=widgets.RadioSelect,
        )
def make_likert9():
        return models.IntegerField(
            choices=[-1,0,1,2,3,4,5,6,7],
            widget=widgets.RadioSelect,
        )
def make_likert8():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7, 8],
            widget=widgets.RadioSelect,
        )
def make_likert6():
        return models.IntegerField(
            choices=[1,2,3,4,5,6],
            widget=widgets.RadioSelect,
        )
def make_likert5():
        return models.IntegerField(
            choices=[1,2,3,4,5],
            widget=widgets.RadioSelect,
        )
def make_likert4():
        return models.IntegerField(
            choices=[1,2,3,4],
            widget=widgets.RadioSelect,
        )
#endregion



#region Knowledge Choices
def cknow1_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_1a],
    ['b_true',  Lexicon.know_1b],
    ['c_false', Lexicon.know_1c],
    ['dk',  Lexicon.dont_know]
]

def cknow2_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_2a],
    ['b_false',  Lexicon.know_2b],
    ['c_true', Lexicon.know_2c],
    ['dk',  Lexicon.dont_know]
]

def cknow3_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_true', Lexicon.know_3a],
    ['b_false',  Lexicon.know_3b],
    ['c_false', Lexicon.know_3c],
    ['dk',  Lexicon.dont_know]
]

def cknow4_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_4a],
    ['b_true',  Lexicon.know_4b],
    ['c_false', Lexicon.know_4c],
    ['dk',  Lexicon.dont_know]
]

def cknow5_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_5a],
    ['b_true',  Lexicon.know_5b],
    ['c_false', Lexicon.know_5c],
    ['dk',  Lexicon.dont_know]
]

def cknow6_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_6a],
    ['b_false',  Lexicon.know_6b],
    ['c_true', Lexicon.know_6c],
    ['dk',  Lexicon.dont_know]
]

def cknow7_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_7a],
    ['b_false',  Lexicon.know_7b],
    ['c_true', Lexicon.know_7c],
    ['d_false', Lexicon.know_7d],

    ['dk',  Lexicon.dont_know]
]

def cknow8_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_true', Lexicon.know_8a],
    ['b_false',  Lexicon.know_8b],
    ['c_false', Lexicon.know_8c],
    ['d_false',  Lexicon.know_8d],
    ['dk',  Lexicon.dont_know]
]

def cknow9_choices(player):
    Lexicon = player.session.scalesLexi
    return [
    ['a_false', Lexicon.know_9a],
    ['b_true',  Lexicon.know_9b],
    ['c_false', Lexicon.know_9c],
    ['d_false',  Lexicon.know_9d],
    ['dk',  Lexicon.dont_know],
]
#endregion


def food_frequencies(player):
    Lexicon = player.session.scalesLexi
    return [
        ['never', Lexicon.food_overall_A],
        ['oncePerMonth',  Lexicon.food_overall_B],
        ['2-3PerMonth', Lexicon.food_overall_C],
        ['oncePerWeek',  Lexicon.food_overall_D],
        ['2-3PerWeek',  Lexicon.food_overall_E],
        ['4-6PerWeek', Lexicon.food_overall_F],
        ['oncePerDay',  Lexicon.food_overall_G],
        ['MultiplePerDay',  Lexicon.food_overall_H]
]

def footprint_food_overall1_choices(player):
    return(food_frequencies(player))

def footprint_food_overall2_choices(player):
    return(food_frequencies(player))

def footprint_food_overall3_choices(player):
    return(food_frequencies(player))

def footprint_food_overall4_choices(player):
    return(food_frequencies(player))

def footprint_food_overall5_choices(player):
    return(food_frequencies(player))


def footprint_commute_car_choices(player):
    Lexicon = player.session.scalesLexi
    return [
        ['never', Lexicon.commute_car_never],
        ['lessA',  Lexicon.commute_car_less_than_A],
        ['AtoB', Lexicon.commute_car_A_to_B],
        ['BtoC',  Lexicon.commute_car_B_to_C],
        ['CtoD',  Lexicon.commute_car_C_to_D],
        ['most', Lexicon.commute_car_more_than_D]
]


def footprint_commute_car_type_choices(player):
    Lexicon = player.session.scalesLexi
    return [
        ['none', Lexicon.commute_car_type_none],
        ['Electric_green', Lexicon.commute_car_type_A],
        ['Eletric_conv', Lexicon.commute_car_type_B],
        ['Biogas', Lexicon.commute_car_type_C],
        ['NaturalGas', Lexicon.commute_car_type_D],
        ['Diesel', Lexicon.commute_car_type_E]
]

def footprint_commute_pt_choices(player):
    Lexicon = player.session.scalesLexi
    return [
        ['lessA', Lexicon.commute_pt_less_than_A],
        ['AtoB', Lexicon.commute_pt_A_to_B],
        ['BtoC', Lexicon.commute_pt_B_to_C],
        ['CtoD', Lexicon.commute_pt_C_to_D],
        ['DtoE', Lexicon.commute_pt_D_to_E],
        ['most', Lexicon.commute_pt_more_than_E]
]
     

#region demographics
## residential area
def residential_area_choices(player):
    residential_area_choices = []
    Lexicon = player.session.scalesLexi
    language_code = player.session.config['language']
    if language_code == 'de':
        residential_area_choices = [
            ["metropolitan", Lexicon.metropolitan_area],
            ["suburban", Lexicon.suburban],
            ["rural", Lexicon.rural]
        ]
    elif language_code == 'zh_hans':
        residential_area_choices = [
        ]
    else:
        residential_area_choices = [
            ["metropolitan", Lexicon.metropolitan_area],
            ["suburban", Lexicon.suburban],
            ["rural", Lexicon.rural]
        ]
    return residential_area_choices

# def states / provinces
def states_choices(player):
    Lexicon = player.session.scalesLexi
    language_code =  player.session.config['language']
    states_choices = []
    if language_code == 'de':
        states_choices = [    
            ["Baden-Württemberg" , Lexicon.BW],
            ["Bayern" , Lexicon.Bayern],
            ["Berlin" , Lexicon.Berlin],
            ["Brandenburg" , Lexicon.Brandenburg],
            ["Bremen" , Lexicon.Bremen],
            ["Hamburg" , Lexicon.Hamburg],
            ["Hessen" , Lexicon.Hessen],
            ["MecklenburgVorpommern" , Lexicon.MV],
            ["Niedersachsen" , Lexicon.Niedersachsen],
            ["NordrheinWestfalen" , Lexicon.NRW],
            ["RheinlandPfalz" , Lexicon.RP],
            ["Saarland" , Lexicon.Saarland],
            ["Sachsen" , Lexicon.Sachsen],
            ["SachsenAnhalt" , Lexicon.SA],
            ["SchleswigHolstein" , Lexicon.SH],
            ["Thüringen" , Lexicon.Thueringen]
        ]

    elif language_code == "zh_hans":
        states_choices = [    
            ["Anhui" , Lexicon.Anhui],
            ["Peking" , Lexicon.Peking],
            ["Chongqing" , Lexicon.Chongqing],
            ["Fujian" , Lexicon.Fujian],
            ["Guangdong" , Lexicon.Guangdong],
            ["Guangxi" , Lexicon.Guangxi],
            ["Gansu" , Lexicon.Gansu],
            ["Guizhou" , Lexicon.Guizhou],
            ["Henan" , Lexicon.Henan],
            ["Hebei" , Lexicon.Hebei],
            ["Hunan" , Lexicon.Hunan],
            ["Hubei" , Lexicon.Hubei],
            ["Hainan" , Lexicon.Hainan],
            ["Heilongjiang" , Lexicon.Heilongjiang],
            ["Jilin" , Lexicon.Jilin],
            ["Jiangsu" , Lexicon.Jiangsu],
            ["Jiangxi" , Lexicon.Jiangxi],
            ["Liaoning" , Lexicon.Liaoning],
            ["InnereMongolei" , Lexicon.InnereMongolei],
            ["Ningxia" , Lexicon.Ningxia],
            ["Qinghai" , Lexicon.Qinghai],
            ["Sichuan" , Lexicon.Sichuan],
            ["Shandong" , Lexicon.Shandong],
            ["Shanxi" , Lexicon.Shanxi],
            ["Shannxi" , Lexicon.Shannxi],
            ["Schanghai" , Lexicon.Schanghai],
            ["Tianjin" , Lexicon.Tianjin],
            ["Xinjiang" , Lexicon.Xinjiang],
            ["Tibet" , Lexicon.Tibet],
            ["Yunnan" , Lexicon.Yunnan],
            ["Zhejiang" , Lexicon.Zhejiang],
            ["Hongkong" , Lexicon.Hongkong],
            ["Taiwan" , Lexicon.Taiwan],
            ["Macao" , Lexicon.Macao]
        ]
   
    else: 
        states_choices = [            
            ["Alabama" , Lexicon.Alabama],
            ["Alaska" , Lexicon.Alaska],
            ["Arizona" , Lexicon.Arizona],
            ["Arkansas" , Lexicon.Arkansas],
            ["California" , Lexicon.California],
            ["Colorado" , Lexicon.Colorado],
            ["Connecticut" , Lexicon.Connecticut],
            ["Delaware" , Lexicon.Delaware],
            ["Florida" , Lexicon.Florida],
            ["Georgia" , Lexicon.Georgia],
            ["Hawaii" , Lexicon.Hawaii],
            ["Idaho" , Lexicon.Idaho],
            ["Illinois" , Lexicon.Illinois],
            ["Indiana" , Lexicon.Indiana],
            ["Iowa" , Lexicon.Iowa],
            ["Kansas" , Lexicon.Kansas],
            ["Kentucky" , Lexicon.Kentucky],
            ["Louisiana" , Lexicon.Louisiana],
            ["Maine" , Lexicon.Maine],
            ["Maryland" , Lexicon.Maryland],
            ["Massachusetts" , Lexicon.Massachusetts],
            ["Michigan" , Lexicon.Michigan],
            ["Minnesota" , Lexicon.Minnesota],
            ["Mississippi" , Lexicon.Mississippi],
            ["Missouri" , Lexicon.Missouri],
            ["Montana" , Lexicon.Montana],
            ["Nebraska" , Lexicon.Nebraska],
            ["Nevada" , Lexicon.Nevada],
            ["NewHampshire" , Lexicon.NewHampshire],
            ["NewJersey" , Lexicon.NewJersey],
            ["NewMexico" , Lexicon.NewMexico],
            ["NewYork" , Lexicon.NewYork],
            ["NorthCarolina" , Lexicon.NorthCarolina],
            ["NorthDakota" , Lexicon.NorthDakota],
            ["Ohio" , Lexicon.Ohio],
            ["Oklahoma" , Lexicon.Oklahoma],
            ["Oregon" , Lexicon.Oregon],
            ["Pennsylvania" , Lexicon.Pennsylvania],
            ["RhodeIsland" , Lexicon.RhodeIsland],
            ["SouthCarolina" , Lexicon.SouthCarolina],
            ["SouthDakota" , Lexicon.SouthDakota],
            ["Tennessee" , Lexicon.Tennessee],
            ["Texas" , Lexicon.Texas],
            ["Utah" , Lexicon.Utah],
            ["Vermont" , Lexicon.Vermont],
            ["Virginia" , Lexicon.Virginia],
            ["Washington" , Lexicon.Washington],
            ["WestVirginia" , Lexicon.WestVirginia],
            ["Wisconsin" , Lexicon.Wisconsin],
            ["Wyoming" , Lexicon.Wyoming]
            
        ]
    return states_choices

#endregion

class Player(BasePlayer):
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

    # new knowledge questions Allianz
    cknow1 = models.StringField( choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect)
    cknow2 = models.StringField(choices=["a_false", "b_false", "c_true", "dk"], widget=widgets.RadioSelect)
    cknow3 = models.StringField(choices=["a_true", "b_false", "c_false", "dk"], widget=widgets.RadioSelect,)
    cknow4 = models.StringField(choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect,)  
    cknow5 = models.StringField(choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect,)     
    cknow6 = models.StringField(choices=["a_false", "b_false", "c_true", "dk"], widget=widgets.RadioSelect,) 
    cknow7 = models.StringField(choices=["a_false", "b_false", "c_true","d_false", "dk"], widget=widgets.RadioSelect,)     
    cknow8 = models.StringField(choices=["a_true", "b_false", "c_false", "d_false", "dk"], widget=widgets.RadioSelect,)     
    cknow9 = models.StringField(choices=["a_false", "b_true", "c_false", "d_false", "dk"], widget=widgets.RadioSelect,)

    
    ### IB Values
    ibv1 = make_likert9()
    ibv2 = make_likert9()
    ibv3 = make_likert9()
    ibv4 = make_likert9()

    ## trust in own and foreign governments
    
    pit1 = make_likert10()
    pit2 = make_likert10()

   

    ### Belief
    belief1Happening= make_likert10()

    beliefHuman1 = make_likert11()
    beliefHuman2 = make_likert11()
    beliefHuman3 = make_likert11()

    beliefConseqences1 = make_likert11()
    beliefConseqences2 = make_likert11()
    beliefConseqences3 = make_likert11()

    belief1Solutions = make_likert10()
    belief2Solutions = make_likert10()
    belief3Solutions = make_likert10()
    belief4Solutions = make_likert10()
    belief5Solutions = make_likert10()

    beliefConsensus = models.IntegerField(min=0,max = 100)

    ## behaviors


    footprint_food_overall1 =  models.StringField(widget=widgets.RadioSelect )
    footprint_food_overall2 =  models.StringField(widget=widgets.RadioSelect )
    footprint_food_overall3 =  models.StringField(widget=widgets.RadioSelect )
    footprint_food_overall4 =  models.StringField(widget=widgets.RadioSelect )
    footprint_food_overall5 =  models.StringField(widget=widgets.RadioSelect )
    # further behavior items
    footprint_flying_short = models.IntegerField(min=0, max= 300 )
    footprint_flying_mid = models.IntegerField(min=0, max= 300)
    footprint_flying_long = models.IntegerField(min=0, max= 300)

    footprint_commute_car =  models.StringField(widget=widgets.RadioSelect )
    footprint_commute_car_type=  models.StringField(widget=widgets.RadioSelect )
    footprint_commute_pt =  models.StringField(widget=widgets.RadioSelect )

    footprint_regional =  make_likert5()
    footprint_electricity =  make_likert4()

    ## policy scales
    policy_commute = make_likert10()
    policy_flying = make_likert10()
    policy_electricity = make_likert10()
    policy_diet = make_likert10()
    policy_recycling = make_likert10()
    policy_regional = make_likert10()


    ### Demographics
    
    householdsize = models.IntegerField(min=1,max = 20) 

    residential_area = models.StringField()
    zip_code = models.StringField(blank=True)
    block_order = models.IntegerField()
    #party_affiliation = models.StringField(choices=get_party_choices(LANGUAGE_CODE, Lexicon) )
    states = models.StringField()




    

class Belief(Page):
    form_model = 'player'
    form_fields= [ 'belief1Happening' , 'beliefConsensus' ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields= [ 'belief1Happening' , 'beliefConsensus'  ],
        form_field_labels = [Lexicon.belief1HappeningLabel , Lexicon.beliefConsensLabel ]
    )

# class Belief1(Page):
#     form_model = 'player'
#     form_fields= [ 'beliefHuman1', 'beliefHuman2', 'beliefHuman3',
#                   'beliefConseqences1', 'beliefConseqences2', 'beliefConseqences3']
#     @staticmethod
#     def vars_for_template(player: Player):
#         return dict(Lexicon=player.session.scalesLexi)
#     @staticmethod
#     def js_vars(player):
#         Lexicon = player.session.scalesLexi
#         return dict(
#         form_fields= [ 'beliefHuman1','beliefHuman2', 'beliefHuman3',
#                   'beliefConseqences1', 'beliefConseqences2', 'beliefConseqences3'],
#         form_field_labels = [ Lexicon.beliefHuman1Label, Lexicon.beliefHuman2Label, Lexicon.beliefHuman3Label, 
#                              Lexicon.beliefConseqences1Label, Lexicon.beliefConseqences2Label, Lexicon.beliefConseqences3Label ]
#     )

class Belief2 (Page):
    form_model = 'player'
    form_fields= [ 'belief1Solutions','belief2Solutions', 'belief3Solutions', 'belief4Solutions', 'belief5Solutions']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields= [ 'belief1Solutions','belief2Solutions', 'belief3Solutions', 'belief4Solutions', 'belief5Solutions' ],
        form_field_labels = [Lexicon.beliefSolutions1Label, Lexicon.beliefSolutions2Label, Lexicon.beliefSolutions3Label,
                              Lexicon.beliefSolutions4Label, Lexicon.beliefSolutions5Label ]
    )

class CCEmotion(Page):
    form_model = 'player'
    form_fields= ['emoAng1', 'emoAng2', 'emoAng3', 'emoSad1','emoSad2', 'emoSad3', 'emoFear1', 'emoFear2', 'emoFear3', 'emoHope1', 'emoHope2', 'emoHope3', 'emoGuilt1', 'emoGuilt2', 'emoGuilt3', 'emoConcern1', 'emoConcern2', 'emoConcern3']
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.scalesLexi
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields = ['emoAng1', 'emoAng2', 'emoAng3', 'emoSad1','emoSad2', 'emoSad3', 'emoFear1', 'emoFear2', 'emoFear3',
                        'emoHope1', 'emoHope2', 'emoHope3', 'emoGuilt1', 'emoGuilt2', 'emoGuilt3', 'emoConcern1', 'emoConcern2', 'emoConcern3'],
        form_field_labels = [Lexicon.emoAng1Label, Lexicon.emoAng2Label , Lexicon.emoAng3Label, Lexicon.emoSad1Label,Lexicon.emoSad2Label, Lexicon.emoSad3Label,  Lexicon.emoFear1Label , Lexicon.emoFear2Label , Lexicon.emoFear3Label,
                            Lexicon.emoHope1Label , Lexicon.emoHope2Label , Lexicon.emoHope3Label , Lexicon.emoGuilt1Label, Lexicon.emoGuilt2Label, Lexicon.emoGuilt3Label, Lexicon.emoConcern1Label, Lexicon.emoConcern2Label, Lexicon.emoConcern3Label]
    )
    
class CCKnowledge(Page):
    form_model = 'player'
    form_fields= ['cknow1', 'cknow2', 'cknow3', 'cknow4', 'cknow5', 'cknow6','cknow7','cknow8', 'cknow9']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields= ['cknow1', 'cknow2', 'cknow3', 'cknow4', 'cknow5', 'cknow6','cknow7','cknow8', 'cknow9'],
        form_field_labels = [Lexicon.know_1qu, Lexicon.know_2qu, Lexicon.know_3qu, Lexicon.know_4qu, Lexicon.know_5qu, Lexicon.know_6qu,  Lexicon.know_7qu, Lexicon.know_8qu, Lexicon.know_9qu]
    )
    
class BehaviorsFood(Page):
    form_model = 'player'
    form_fields= ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields=  ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5' ], 
        form_field_labels = [Lexicon.food_overall_label1, Lexicon.food_overall_label2, Lexicon.food_overall_label3, Lexicon.food_overall_label4, Lexicon.food_overall_label5  ]
    )
class BehaviorsFood2(Page):
    form_model = 'player'
    form_fields= [ 'footprint_regional', 'footprint_electricity']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields=  [ 'footprint_regional', 'footprint_electricity'], 
        form_field_labels = [ Lexicon.regional_label, Lexicon.electricity_label ]
    )
class BehaviorsTransport(Page):
    form_model = 'player'
    form_fields= ['footprint_commute_car', 'footprint_commute_car_type', 'footprint_commute_pt']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields=  ['footprint_commute_car', 'footprint_commute_car_type', 'footprint_commute_pt' ], 
        form_field_labels = [Lexicon.commute_car_label, Lexicon.commute_car_type_label, Lexicon.commute_pt_label ]
    )

class BehaviorsFlying(Page):
    form_model = 'player'
    form_fields= [ 'footprint_flying_short', 'footprint_flying_mid', 'footprint_flying_long']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields=  [ 'footprint_flying_short', 'footprint_flying_mid', 'footprint_flying_long'], 
        form_field_labels = [  Lexicon.flying_short_label, Lexicon.flying_mid_label, Lexicon.flying_long_label ]
    )


class IBValues(Page):
    form_model = 'player'
    form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4'],
        form_field_labels = [Lexicon.ibv1Label, Lexicon.ibv2Label , Lexicon.ibv3Label, Lexicon.ibv4Label]
    )
        
class PITrust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2']
    @staticmethod

    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields = ['pit1', 'pit2' ],
        form_field_labels = [Lexicon.pit1Label, Lexicon.pit2Label]
    )
        
class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]
    @staticmethod

    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        return dict(
        form_fields = ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ],
        form_field_labels = [Lexicon.policy1Label, Lexicon.policy2Label, Lexicon.policy3Label, Lexicon.policy4Label, Lexicon.policy5Label, Lexicon.policy6Label  ]
    )

class DemographicsEnd(Page):
    @staticmethod
    def get_form_fields(player):
        if player.session.config['language'] == "de":
            return [ 'householdsize', 'residential_area', 'zip_code', 'states' ]
        else:
            return [ 'householdsize', 'zip_code', 'states' ]
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.scalesLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.scalesLexi
        if  player.session.config['language'] == "de":
            return dict(
            form_fields= [ 'householdsize', 'residential_area', 'zip_code', 'states' ], 
            form_field_labels = [Lexicon.householdsize_label,Lexicon.residential_area_label , Lexicon.zip_code_label , Lexicon.states_label],
            langcode= "de")
        else:
            return dict(
            form_fields= [ 'householdsize', 'zip_code', 'states' ],
            form_field_labels = [Lexicon.householdsize_label, Lexicon.zip_code_label , Lexicon.states_label ],
            langcode="other")

class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        try: 
            player.participant.task_counter
            print("none is true")
        except:   
            player.participant.task_counter = 0
        player.participant.task_counter += 1 
        player.block_order = player.participant.task_counter
        return dict(Lexicon=player.session.scalesLexi)
    


page_sequence = [ transition, Belief, Belief2, CCKnowledge, CCEmotion,
                 BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
                 PITrust, IBValues ,
                 policyScales,
                 DemographicsEnd
                 ]