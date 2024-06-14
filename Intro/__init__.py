from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

   
# consent
    
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)
    
    
# FUNCTIONS
# PAGES


class Consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']

    @staticmethod
    def vars_for_template(player: Player):
        # while testing this experiment do not check for prolificID (replace False with commented code) (make nolabel and prolificID Missing false for testing)
        return {
            "particpantlabel": player.participant.label,
            }


class Instructions(Page):
    form_model = 'player'
    

# Page sequence
page_sequence = [
    Consent,
    Instructions
]