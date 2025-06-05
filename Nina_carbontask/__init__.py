import random
import json

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16
    #FOOTPRINT_COMBINATIONS_TABLE_de = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_de.json')
    FOOTPRINT_COMBINATIONS_TABLE_en = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_en.json')
    #FOOTPRINT_COMBINATIONS_TABLE_zh_hans = open('Nina_carbontask/FOOTPRINT_COMBINATIONS_TABLE_zh_hans.json')
    #FootprintTable_de = json.load(FOOTPRINT_COMBINATIONS_TABLE_de)['FootprintTable']
    FootprintTable_en = json.load(FOOTPRINT_COMBINATIONS_TABLE_en)['FootprintTable']
    #FootprintTable_zh_hans = json.load(FOOTPRINT_COMBINATIONS_TABLE_zh_hans)['FootprintTable']

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
    
    #subsession.session.myLangCode = subsession.session.config['language']
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(0, C.NUM_ROUNDS))
            random.shuffle(round_numbers)
            p.participant.task_rounds = round_numbers



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rating0 = models.FloatField( label='How large or small do you think this persons footprint is?', mix=1820, max=5540)

    attention_rating = models.FloatField( label='To demonstrate that you are reading the text attentively, please move the range slider all the way to the right (i.e. towards 5540).', mix=1820, max=5540)
  
   
    vignetteNumber = models.IntegerField(initial= 0)
    order_behavior_types = models.StringField()
   
   

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class task_page00(Page):

    # 0 is diet, 1 is electricity, 2 is recycling, 3 is regional food, 4 is commute, 5 vacation
    form_model = 'player'
    form_fields = ['rating0']
    
    def error_message(self, values):
        rating = str(values['rating0'])
        # Ensure the number has a decimal part
        if '.' not in rating or len(rating.split('.')[1]) < 1:
            return 'Please enter a number with at least one decimal place.'

   
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        # this determines which vignette
        task_in_round = player.participant.task_rounds[player.round_number - 2]
        player.vignetteNumber = task_in_round
        my_vignette_table =  C.FootprintTable_en[task_in_round]
        my_vignette_table_images = C.FOOTPRINT_COMBINATIONS_IMAGES[task_in_round]
        # this determines which order within vignette
        random_behavior_order = list(range(0,6))
        random.shuffle(random_behavior_order)
        current_footprint_table_shuffled = []
        current_footprint_table_images_shuffled = []
        behavior_types= ["Diet", "Laundry", "Recycling", "Food", "Commute", "Vacation"]
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
            'behaviorTYPES' : behavior_types,
            'round_number': round_number
        }
    

class Attention(Page):
    form_model = 'player'
    form_fields = ['attention_rating' ]
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        # this determines which vignette
        my_vignette_table =  ['<b>meat-based diet</b>', '<b>air dry laundry</b>', '<b> slider to 5540 </b>', '<b>only regional</b>', '<b>by bus</b>', '<b> slider to 5540 </b>' ]
        my_vignette_table_images = ['diet_image_2', 'household_image_1', 'attention', 'regional_image_1', 'commute_image_2', 'attention']
        # this determines which order within vignette
       
        behavior_types = ["Diet", "Laundry", "Move", "Food", "Commute", "Move"]
        
        player.order_behavior_types = str(behavior_types)
        return {
            "current_footprint_table": my_vignette_table,
            "current_footprint_table_images": my_vignette_table_images,
            'behaviorTYPES' : behavior_types,
            'round_number': round_number
        }
    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number == 7)
    
   
    

# Page sequence
page_sequence = [task_page00, Attention]
