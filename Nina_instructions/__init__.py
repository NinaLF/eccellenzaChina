import random
import json

from otree.api import *
from settings import LANGUAGE_CODE


class C(BaseConstants):
    NAME_IN_URL = 'instructions_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


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
    subsession.session.introNinaLexi = Lexicon 


def comprehensionQ_choices(player):
    Lexicon = player.session.introNinaLexi 
    return [
    ['200g_false', Lexicon.comprehension_a],
    ['true',  Lexicon.comprehension_b],
    ['900g_false', Lexicon.comprehension_c]
]    


def aboutWhat_choices(player): 
    Lexicon = player.session.introNinaLexi 
    return [
    ['tourism_false', Lexicon.about_a],
    ['true',  Lexicon.about_b],
    ['washingMachine_false', Lexicon.about_c],
    ['spicy_false',  Lexicon.about_d]
]



class Player(BasePlayer):
    block_order = models.IntegerField()
    already_counted = models.BooleanField(initial=False)

    aboutWhat = models.StringField()
    screenoutAboutWhat = models.BooleanField(initial= False)
    comprehensionQ = models.StringField()
   

# FUNCTIONS

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        if player.already_counted == False:
            try: 
                player.participant.task_counter
            except:   
                player.participant.task_counter = 0
            player.participant.task_counter += 1 
            player.block_order = player.participant.task_counter
            player.already_counted = True
        return dict(Lexicon=player.session.introNinaLexi,blocknumber = player.block_order, blockaccomplished = player.block_order -1)
   
    
class instructions(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi)
    
    
class comprehension(Page):
    form_model = 'player'
    form_fields = ['comprehensionQ']

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.introNinaLexi
        
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.introNinaLexi
        return dict(
        form_fields = ['comprehensionQ'],
        form_field_labels = [Lexicon.comprehension_title]

    )
 
   
   
    
class task_example(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi)
    
class interlude (Page): 
    form_model = 'player'
    form_fields = ['aboutWhat']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if(player.aboutWhat != "true" ):
               player.screenoutAboutWhat = True
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.task_counter == 1)
    


class Screenout(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'Lexicon': player.session.introNinaLexi,
             'participantlabel':player.participant.label
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.screenoutAboutWhat)
   
    
   
        

# Page sequence
page_sequence = [ transition,
                  instructions, 
                  interlude, 
                  Screenout,
                  task_example,
                  comprehension
                  ]