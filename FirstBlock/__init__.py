import random
import os


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



# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}
#which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
#which_language[LANGUAGE_CODE[:2]] = True

class C(BaseConstants):
    NAME_IN_URL = 'startofstudy'
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
    subsession.session.firstBlockLexi = Lexicon 
    

#region Choices for demographics
# Nina: added gender german at beginning
def education_choices(player):
    Lexicon = player.session.firstBlockLexi
    language_code =  player.session.config['language']
    education_choices = []
    if language_code == 'de':
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]

    elif language_code == 'zh_hans':
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]
   
    else:
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]
    return education_choices

def party_choices(player):
    party_choices = []
    Lexicon = player.session.firstBlockLexi
    language_code =  player.session.config['language']
    if language_code == 'de':
        party_choices = [    
            ["cdcsu", Lexicon.cdcsu],
            ["spd", Lexicon.spd],
            ["gruene", Lexicon.gruene],
            ["fdp", Lexicon.fdp],
            ["linke", Lexicon.linke],
            ["afd", Lexicon.afd],
            ["other_party", Lexicon.other_party]
        ]
    elif language_code == 'en':
        party_choices = [
            ["republicans", Lexicon.republicans], 
            ["democrats", Lexicon.democrats], 
            ["independent_party", Lexicon.independent_party], 
            ["other_party", Lexicon.other_party]
        ]
    else:
        party_choices = [
        ]
    return party_choices

def gender_choices(player):
    gender_choices = []
    Lexicon = player.session.firstBlockLexi
    language_code = player.session.config['language']
    if language_code == 'de':
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["diverse", Lexicon.diverse], 
            ["other", Lexicon.other]
        ]
    elif language_code == 'zh_hans':
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["other", Lexicon.other]
        ]
    else:
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["diverse", Lexicon.diverse], 
            ["other", Lexicon.other]
        ]
    return gender_choices

# region start
# def income_choices(player):
#     income_choices = []
#     Lexicon = player.session.firstBlockLexi
#     language_code = player.session.config['language']
#     if language_code == 'de':
#         income_choices = [    
#             ["quintile1", Lexicon.income_quintile1],
#             ["quintile2", Lexicon.income_quintile2],
#             ["quintile3", Lexicon.income_quintile3],
#             ["quintile4", Lexicon.income_quintile4],
#             ["quintile5", Lexicon.income_quintile5],
#             ["NoAnswer", Lexicon.prefer_not_to_say],
#         ]
#     elif language_code == 'zh_hans':
#         income_choices = [    
#             ["quintile1", Lexicon.income_quintile1],
#             ["quintile2", Lexicon.income_quintile2],
#             ["quintile3", Lexicon.income_quintile3],
#             ["quintile4", Lexicon.income_quintile4],
#             ["quintile5", Lexicon.income_quintile5],
#             ["NoAnswer", Lexicon.prefer_not_to_say],
#         ]
#     else:
#         income_choices = [    
#             ["quintile1", Lexicon.income_quintile1],
#             ["quintile2", Lexicon.income_quintile2],
#             ["quintile3", Lexicon.income_quintile3],
#             ["quintile4", Lexicon.income_quintile4],
#             ["quintile5", Lexicon.income_quintile5],
#             ["NoAnswer", Lexicon.prefer_not_to_say],
#         ]
#     return income_choices
#endregion


def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
        )

class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012


    ### Demographics
    age = models.IntegerField(min=18,max = 99)
    education = models.StringField()
    party = models.StringField()

    
    yearOfBirth = models.IntegerField(min=1900,max = 2008)  # change in different waves
    

    # Worldviews and values - Hierarchy-Egalitarianism & Individualism-Communitarianism  
    hie1 = make_likert10()
    hie2 = make_likert10()
    hie3 = make_likert10()
    ind1 = make_likert10()
    ind2 = make_likert10()
    ind3 = make_likert10()
    polOrientation = make_likert10()
    attentionWV = make_likert10()

    screenoutBirthyear = models.BooleanField(initial=False)
    screenoutWV = models.BooleanField(initial=False)
    discrepancy = models.IntegerField()


  
class Demographics(Page):
    @staticmethod
    def get_form_fields(player):
        if player.session.config['language'] == "zh_hans":
            return ['age',  'education']
        else:
            return ['age',  'education', 'party']
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.firstBlockLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.firstBlockLexi
        if  player.session.config['language'] == "zh_hans":
            return dict(
            form_fields= ['age',  'education'],
            form_field_labels = [Lexicon.age_label,Lexicon.education_label ],
            langcode= "zh_hans")
        else:
            return dict(
            form_fields= ['age',  'education', 'party'],
            form_field_labels = [Lexicon.age_label,Lexicon.education_label ,Lexicon.party_affiliation_label ],
            langcode="west")


class Demographics2(Page):
    form_model = 'player'
    form_fields = ['yearOfBirth']
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'Lexicon': player.session.firstBlockLexi
        
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.firstBlockLexi
        return dict(
        form_fields = ['yearOfBirth'],
        form_field_labels = [Lexicon.ageYear_label]
    )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        discrepancy = (player.yearOfBirth + player.age) - 2024
        player.discrepancy = discrepancy
        if(abs(discrepancy) > 2 ):
               player.screenoutBirthyear = True

    

class Screenout(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'Lexicon': player.session.firstBlockLexi,
             'participantlabel':player.participant.label
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.screenoutBirthyear or player.screenoutWV )
   
    

class WVValues(Page):
    @staticmethod
    def get_form_fields(player):
        if player.session.config['language'] == "zh_hans":
            return ['hie1', 'hie2', 'hie3', 'ind1', 'attentionWV',  'ind2', 'ind3']
        else:
            return ['hie1', 'hie2', 'hie3', 'ind1', 'attentionWV', 'ind2', 'ind3', "polOrientation"]
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.firstBlockLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.firstBlockLexi
        if  player.session.config['language'] == "zh_hans":
            return dict(
            form_fields= ['hie1', 'hie2','attentionWV', 'ind2', 'ind3'],
            form_field_labels = [Lexicon.hie1Label, Lexicon.hie2Label ,  Lexicon.attentionWVLabel, Lexicon.ind2Label, Lexicon.ind3Label],
            langcode= "zh_hans")
        else:
            return dict(
            form_fields= ['hie1', 'hie2',  'attentionWV', 'ind2', 'ind3', "polOrientation"],
            form_field_labels = [Lexicon.hie1Label, Lexicon.hie2Label , Lexicon.attentionWVLabel, Lexicon.ind2Label, Lexicon.ind3Label, Lexicon.polOrientationLabel],
            langcode="west")
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        correct = player.attentionWV == 10
        if( correct == False ):
               player.screenoutWV = True






page_sequence = [Demographics, Demographics2, Screenout, WVValues, Screenout]
