import random
from otree.api import *
import numpy as np
import json
# import scipy.stats as stats



author = 'Zahra Rahmani'
doc = """
Debrief for Sampling
"""


# def truncnorm(lower, upper, mean, std):
#     return stats.truncnorm((lower - mean) / std, (upper - mean) / std, loc=mean, scale=std).rvs()

class C(BaseConstants):
    NAME_IN_URL = 'Goodbye'
    PLAYERS_PER_GROUP = None
    ROUNDS_PER_CONDITION = 1
    NUM_ROUNDS = 1
    

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

#PLAYER FUNCTION 
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
    subsession.session.GoodbyeLexi = Lexicon 

class Player(BasePlayer):
    generalFeedback = models.StringField(max_length=3000, blank=True)

    
  # FUNCTIONS
    





# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


    



class goodbye (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.GoodbyeLexi)
    def vars_for_template(player: Player):
       return{
            #Lexicon': player.session.introLexi
            'u': player.participant.label,
            'participantlabel':player.participant.label,
            'Lexicon': player.session.GoodbyeLexi

        } 

class Feedback(Page):
    form_model = 'player'
    form_fields = ["generalFeedback"]
    @staticmethod
    def vars_for_template(player: Player):
        print("this should be the lixicon")
        return dict(Lexicon=player.session.GoodbyeLexi)



page_sequence = [

    Feedback,
    goodbye
]
