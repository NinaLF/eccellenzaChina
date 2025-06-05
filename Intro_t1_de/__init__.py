from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Introt1_de'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    if subsession.round_number == 1:
        session.num_female_de = 0
        session.num_male_de = 0
        session.num_age1_de = 0
        session.num_age2_de = 0
        session.num_age3_de = 0
        session.num_age4_de = 0


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    quota_full = models.IntegerField(initial=0)

    def make_field(label):
        return models.IntegerField(
        choices=[1,2,3,4,5,6,7,8,9,10],                           
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

# consent
    
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)

    
    subjectiveKnowledgePre = models.IntegerField(widget=widgets.RadioSelect,  label= 'Wie kenntnisreich fühlen Sie sich über die Auswirkungen verschiedener Verhaltensweisen auf den CO<sub>2</sub>-Fußabdruck? Das heißt, wie viel denken Sie wissen Sie, über die Menge an CO<sub>2</sub>-Emissionen, die durch verschiedene Handlungen verursacht wird?',
                                              choices=[['1', 'überhaupt nicht viel (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', '7'], ['8', '8'],['9', '9'], ['10', 'sehr viel (10)'] ]   )
    
     # demographics
    age = models.IntegerField(label='Wie alt sind Sie', min=18, max=90)
    
    gender = models.StringField( label='Welchem Geschlecht fühlen Sie sich zugehörig?',
        choices=[['Male', 'Männlich'], ['Female', 'Weiblich'], 
        ['prefer not to answer/ diverse', 'divers/keine Angabe']],
        widget = widgets.RadioSelect
    )
    education = models.StringField( label='Was ist Ihr höchster Bildungsabschluss?',
        choices=[['No formal education', 'keine formelle Bildung abgeschlossen'],
                ['Compulsory education', 'obligatorische Schule'], 
                 ['Further education', 'Sekundarstufe: Matura / Berufsbildung / Allgemeinbildung '],
                 ['Higher education (Bachelor, Master, PhD)', 'höhere Berufsbildung: Hochschulabschluss / Bachelor / Master / Doktor']],
                 widget = widgets.RadioSelect
    )

    income = models.StringField(
                                label='Wie hoch ist Ihr <b>persönliches monatliches Nettoeinkommen </b> (d.h. nach Abzügen und Steuern)?',
        choices=[['<  3.000 CHF', '<  3.000 CHF'],
                  [' 3.001 CHF bis 5.000 CHF',  ' 3.001 CHF bis 5.000 CHF'], 
                   [' 5.001 CHF bis 6.000 CHF',  ' 5.001 CHF bis 6.000 CHF'], 
                 [' 6.001 CHF bis 7.000 CHF',  ' 6.001 CHF bis 7.000 CHF'], 
                 [' 7.001 CHF bis 9.000 CHF',  ' 7.001 CHF bis 9.000 CHF'], 
                 ['> 9.001 CHF', '> 9.001 CHF']],
                  widget = widgets.RadioSelect
    )
    polOrientation =  models.IntegerField( widget=widgets.RadioSelect,  
                                          choices=[['1', 'extremely left (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'extremely right (10)'] ] ) 


    climate_change_concern1 = make_field('Ich mache mir Sorgen, dass sich das Klima verändert. ')
    climate_change_concern2 = make_field('Klimaschutz ist wichtig für unsere Zukunft.')
    climate_change_concern3 = make_field('Wir müssen das Gleichgewicht des Klimas schützen.')
    climate_change_concern4 = make_field('Der Klimawandel hat schwerwiegende Folgen für Mensch und Natur.')
    
    attention_check = make_field('Um zu zeigen, dass Sie aufmerksam lesen, wählen Sie bitte die Auswahl ganz rechts ("Stimme absolut zu").')

    screenoutWV = models.BooleanField(initial=False)

    
    
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
    
class Demographics(Page):
    form_model = 'player'
    form_fields= [ 'age', 'gender', 'education', 'income', 'polOrientation' ]
     
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        participant = player.participant

        if player.gender == 'Female' and session.num_female_de >= 560:
            player.quota_full = 1
            participant.quota_full = 1
        elif player.gender == 'Male' and session.num_male_de >= 560:
            player.quota_full = 1
            participant.quota_full = 1
        
        age = player.age
        if 18 <= age <= 29 and session.num_age1_de >= 210:
            player.quota_full = 1
        elif 30 <= age <= 44 and session.num_age2_de >= 330:
            player.quota_full = 1
        elif 45 <= age <= 59 and session.num_age3_de >= 310:
            player.quota_full = 1
        elif 60 <= age <= 80 and session.num_age4_de >= 300:
            player.quota_full = 1

        participant.quota_full = player.quota_full
        participant.vars['gender'] = player.gender
        participant.vars['age'] = player.age


class QuotaFull(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.quota_full == 1
    
class ClimateConcern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'attention_check',  'climate_change_concern3', 'climate_change_concern4']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        correct = player.attention_check == 10
        if( correct == False ):
               player.screenoutWV = True


class Screenout(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'participantlabel':player.participant.label
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.screenoutWV )


# Page sequence
page_sequence = [
    Consent, Demographics, QuotaFull, ClimateConcern, Screenout, Baseline
    
]