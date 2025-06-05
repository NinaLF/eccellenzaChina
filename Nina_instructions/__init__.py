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







class Player(BasePlayer):

    comprehensionQ = models.StringField()
   

# FUNCTIONS

# PAGES


class instructions(Page):
    form_model = 'player'
   
   

class instructionsUnit(Page):
    form_model = 'player'
   
    
class task_example(Page):
    form_model = 'player'

    

   
        

# Page sequence
page_sequence = [ instructions, instructionsUnit, 
                  task_example #, comprehension
                  ]