import random
import json
from os import environ
from otree.api import *
from settings import LANGUAGE_CODE

#LANGUAGE_CODE = environ.get('LANGUAGE_CODE')
#from settings import LANGUAGE_CODE


author = 'Zahra Rahmani'


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}




class C(BaseConstants):
    NAME_IN_URL = 'carbon_taxtask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 12


    POLICY_COMBINATIONS_TABLE_de = open('Jessi_carbonTax/Policy_Combinations_Table_de.json')
    POLICY_COMBINATIONS_TABLE_us =  open('Jessi_carbonTax/Policy_Combinations_Table_en.json')
    POLICY_COMBINATIONS_TABLE_zh_hans =  open('Jessi_carbonTax/Policy_Combinations_Table_zh_hans.json')
    PolicyTable_de = json.load(POLICY_COMBINATIONS_TABLE_de)['PolicyTable']
    PolicyTable_zh_hans = json.load(POLICY_COMBINATIONS_TABLE_zh_hans)['PolicyTable']
    PolicyTable_us = json.load(POLICY_COMBINATIONS_TABLE_us)['PolicyTable']


class Subsession(BaseSubsession):
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
    subsession.session.JessiTaskLexicon = Lexicon 
    
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(0, C.NUM_ROUNDS))
            random.shuffle(round_numbers)
            p.participant.task_rounds_J = round_numbers
                
class Group(BaseGroup):
    pass


def get_attributes(player):
        if player.session.config['language'] == 'de':
            return ["Sektor", "Preis", "Einnahmenverwendung", "Inkrafttreten"]
        elif player.session.config['language'] == 'zh_hans':
            return ["行业", "价格", "收入机制", "实施时间"]
        else:
            return ["Sector", "Price", "Revenue mechanism", "Implementation timing"]

#()

class Player(BasePlayer):
    accept = models.IntegerField(choices = [['1', 'yes'], ['2', 'no']])
    vignetteNumber = models.IntegerField(initial= 0)
    order_behavior_types = models.StringField()
    filler_ITI = models.StringField()

# FUNCTIONS
# for random order of tasks

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class task_page00(Page):

    # 0 is diet, 1 is electricity, 2 is recycling, 3 is regional food, 4 is commute, 5 vacation
    form_model = 'player'
    form_fields = ['accept']
    @staticmethod
    def vars_for_template(player: Player):
        # this determines which vignette
        task_in_round = player.participant.task_rounds_J[player.round_number - 2]
        player.vignetteNumber = task_in_round
        if player.session.config['language'] == "de":
            my_vignette_table = C.PolicyTable_de[task_in_round]
        elif player.session.config['language'] == 'zh_hans':
            my_vignette_table = C.PolicyTable_zh_hans[task_in_round]
        else :
            my_vignette_table =  C.PolicyTable_us[task_in_round]        
        
        # this determines which order within vignette
        random_attribute_order = list(range(0,4))
        random.shuffle(random_attribute_order)
        current_policy_table_shuffled = []
        attributes = get_attributes(player)
        order_attributes = []
        for i in random_attribute_order:
            current_policy_table_shuffled.append(my_vignette_table[i])
            order_attributes.append(attributes[i])
        player.order_behavior_types = str(order_attributes)
        return {
            "current_policy_table": current_policy_table_shuffled,
            "random_attribute_order": random_attribute_order,
            'Attributes' : attributes ,
            'Lexicon': player.session.JessiTaskLexicon
        }
   
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.JessiTaskLexicon
        return dict(
        form_fields = ['accept'] ,
        form_field_labels = [Lexicon.would_accept ]
    )

class inter_trial(Page):
    form_model = 'player'
    form_fields = ['filler_ITI']
    timeout_seconds = 0.2

    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.JessiTaskLexicon)
     
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.JessiTaskLexicon
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.JessiTaskLexicon
        return dict(
        form_fields = ['filler_ITI'] 
    )


# Page sequence
page_sequence = [
    task_page00,
    inter_trial
    ]

