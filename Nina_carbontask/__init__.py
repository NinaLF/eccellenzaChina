import random
import json

from otree.api import *
from settings import LANGUAGE_CODE


class C(BaseConstants):
    NAME_IN_URL = 'task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16
    FOOTPRINT_COMBINATIONS_TABLE_de = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_de.json')
    FOOTPRINT_COMBINATIONS_TABLE_en = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_en.json')
    FOOTPRINT_COMBINATIONS_TABLE_zh_hans = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_zh_hans.json')
    FootprintTable_de = json.load(FOOTPRINT_COMBINATIONS_TABLE_de)['FootprintTable']
    FootprintTable_en = json.load(FOOTPRINT_COMBINATIONS_TABLE_en)['FootprintTable']
    FootprintTable_zh_hans = json.load(FOOTPRINT_COMBINATIONS_TABLE_zh_hans)['FootprintTable']

    FOOTPRINT_COMBINATIONS_IMAGES = [
        ['diet_image_1', 'household_image_1', 'recycling_image_1', 'regional_image_1', 'commute_image_1', 'vacation_image_1'],
        ['diet_image_1', 'household_image_1', 'recycling_image_1', 'regional_image_2', 'commute_image_2', 'vacation_image_1'],
        ['diet_image_2', 'household_image_1', 'recycling_image_2', 'regional_image_2', 'commute_image_1', 'vacation_image_1'],
        ['diet_image_2', 'household_image_1', 'recycling_image_2', 'regional_image_1', 'commute_image_2', 'vacation_image_1'],
        ['diet_image_1', 'household_image_2', 'recycling_image_2', 'regional_image_1', 'commute_image_1', 'vacation_image_1'],
        ['diet_image_1', 'household_image_1', 'recycling_image_2', 'regional_image_2', 'commute_image_1', 'vacation_image_2'],
        ['diet_image_1', 'household_image_2', 'recycling_image_2', 'regional_image_2', 'commute_image_2', 'vacation_image_1'],
        ['diet_image_2', 'household_image_2', 'recycling_image_1', 'regional_image_2', 'commute_image_1', 'vacation_image_1'],
        ['diet_image_1', 'household_image_1', 'recycling_image_2', 'regional_image_1', 'commute_image_2', 'vacation_image_2'],
        ['diet_image_2', 'household_image_1', 'recycling_image_2', 'regional_image_1', 'commute_image_1', 'vacation_image_2'],
        ['diet_image_2', 'household_image_2', 'recycling_image_1', 'regional_image_1', 'commute_image_2', 'vacation_image_1'],
        ['diet_image_2', 'household_image_1', 'recycling_image_1', 'regional_image_2', 'commute_image_2', 'vacation_image_2'],
        ['diet_image_1', 'household_image_2', 'recycling_image_1', 'regional_image_2', 'commute_image_1', 'vacation_image_2'],
        ['diet_image_1', 'household_image_2', 'recycling_image_1', 'regional_image_1', 'commute_image_2', 'vacation_image_2'],
        ['diet_image_2', 'household_image_2', 'recycling_image_2', 'regional_image_1', 'commute_image_1', 'vacation_image_2'],
        ['diet_image_2', 'household_image_2', 'recycling_image_2', 'regional_image_2', 'commute_image_2', 'vacation_image_2']

    ]
    
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
    subsession.session.carbonTaskLexi = Lexicon 
    #subsession.session.myLangCode = subsession.session.config['language']
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(0, C.NUM_ROUNDS))
            random.shuffle(round_numbers)
            p.participant.task_rounds = round_numbers


def get_behavior_types(player):
        if player.session.config['language'] == 'de':
            return ["Ernährung", "Elektrizität", "Recycling", "Lebensmittel", "Arbeitsweg", "Urlaub"]
        elif player.session.config['language'] == 'zh_hans':
            return ["饮食" , "电力", "回收", "食物", "通勤", "假期"]
        else:
            return ["Diet", "Electricity", "Recycling", "Food", "Commute", "Vacation"]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rating0 = models.IntegerField(choices=[['1', 'small footprint (1)'], ['2', '2'], ['3', '3'], ['4', '4'],
                                           ['5', '5'],['6', '6'], ['7', '7'], ['8', '8'],['9', '9'], ['10', 'large footprint (10)']], 
                                  widget=widgets.RadioSelectHorizontal,
                                  label='How large or small do you think this persons footprint is?')
    vignetteNumber = models.IntegerField(initial= 0)
    order_behavior_types = models.StringField()
   
   

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class task_page00(Page):

    # 0 is diet, 1 is electricity, 2 is recycling, 3 is regional food, 4 is commute, 5 vacation
    form_model = 'player'
    form_fields = ['rating0']
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        # this determines which vignette
        task_in_round = player.participant.task_rounds[player.round_number - 2]
        player.vignetteNumber = task_in_round
        if player.session.config['language'] == "de":
            my_vignette_table = C.FootprintTable_de[task_in_round]
        elif player.session.config['language'] == 'zh_hans':
            my_vignette_table = C.FootprintTable_zh_hans[task_in_round]
        else :
            my_vignette_table =  C.FootprintTable_en[task_in_round]
        my_vignette_table_images = C.FOOTPRINT_COMBINATIONS_IMAGES[task_in_round]
        # this determines which order within vignette
        random_behavior_order = list(range(0,6))
        random.shuffle(random_behavior_order)
        current_footprint_table_shuffled = []
        current_footprint_table_images_shuffled = []
        behavior_types= get_behavior_types(player)
        order_behavior_types = []
        for i in random_behavior_order:
            current_footprint_table_shuffled.append(my_vignette_table[i])
            current_footprint_table_images_shuffled.append(my_vignette_table_images[i])
            order_behavior_types.append(behavior_types[i])
        player.order_behavior_types = str(order_behavior_types)
        return {
            "current_footprint_table": current_footprint_table_shuffled,
            "current_footprint_table_images": current_footprint_table_images_shuffled,
            "random_behavior_order": random_behavior_order,
            'Lexicon': player.session.carbonTaskLexi,
            'behaviorTYPES' : behavior_types,
            'round_number': round_number
        }
    

# Page sequence
page_sequence = [task_page00]
