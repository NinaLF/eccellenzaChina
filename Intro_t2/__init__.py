from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Introt2'
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

    subjectiveKnowledgePre = models.StringField(widget=widgets.RadioSelect,  
                                                 label= '  How knowledgeable do you feel about the effect of different behaviors on carbon footprints? That is, how much do you feel you know about how many CO<sub>2</sub> emissions are caused by differen actions?',
                                              choices=[['1', 'not much at all (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', 'A great deal (7)'] ]   )

    
    
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

class Baseline(Page):
    form_model = 'player'
    form_fields= [ 'subjectiveKnowledgePre' ]
    

# Page sequence
page_sequence = [
    Consent
    
]