from otree.api import *
from otree.api import BaseGroup
from statistics import mean

doc = """
Slider example
"""


class Constants(BaseConstants):
    name_in_url = "slider"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):


    def get_completed_count(self):
        players = self.get_players()
        return sum(1 for p in players if p.participant.group_assignment == "experimental" and p.field_maybe_none('meat') is not None and p.field_maybe_none('flying') is not None)



class Group(BaseGroup):
    def live_method(self, data): 
        participant_id = data['participant_id']
        field = data['field']
        value = data['value']

        player = self.get_player_by_id(participant_id)
        setattr(player, field, value)
        player.save()

        all_values = self.get_all_values()
        means = {field: mean(values) for field, values in all_values.items()}

        self.send('all', means)
        
    def get_all_values(self):
        fields = ['meat', 'flying', 'greenelectricity', 'recycling', 'nonRegionalFood', 'car']
        all_values = {}
        for field in fields:
            values = []
            for player in self.get_players():
                if player.participant.group_assignment == "experimental":
                    try:
                        value = getattr(player, field)
                        if value is not None:
                            values.append(value)
                    except TypeError:
                    # Handle the case where field is None
                        pass
            all_values[field] = values
        return all_values


def creating_session(subsession:Subsession):

    import itertools
    group_assignment = itertools.cycle(["control", "experimental"])
    for player in subsession.get_players():
        if subsession.round_number == 1:
            player.participant.group_assignment = next(group_assignment)

class Player(BasePlayer):
    flying = models.IntegerField( null=True)
    meat = models.IntegerField( null=True)
    greenelectricity = models.IntegerField( null=True)
    nonRegionalFood = models.IntegerField( null=True)
    car = models.IntegerField( null=True)
    recycling = models.IntegerField( null=True)

    # New fields to store the completed count and mean values
    completed_count = models.IntegerField(null=True)
    mean_flying = models.FloatField(null=True)
    mean_meat = models.FloatField(null=True)
    mean_greenelectricity = models.FloatField(null=True)
    mean_nonRegionalFood = models.FloatField(null=True)
    mean_car = models.FloatField(null=True)
    mean_recycling = models.FloatField(null=True)

   # group_assignment = models.StringField()

# PAGES

class TaskInfo(Page):
    pass

class TaskInfoExp(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "experimental"
    

    def is_displayed(self):
        return self.participant.group_assignment == "experimental"

    def vars_for_template(self):
        completed_count = self.subsession.get_completed_count()
        
        all_values = self.group.get_all_values()
        means = {}
        for field, values in all_values.items():
            valid_values = [v for v in values if v is not None]
            means[field] = mean(valid_values) if valid_values else 'no data yet'

        for field in means:
            if means[field] != 'no data yet':
                means[field] = round(means[field], 2)


        return {'means': means, 'completed_count': completed_count}
    
    def before_next_page(self, timeout_happened=False):

        completed_count = self.subsession.get_completed_count()
        
        all_values = self.group.get_all_values()
        means = {}
        for field, values in all_values.items():
            valid_values = [v for v in values if v is not None]
            means[field] = mean(valid_values) if valid_values else 'no data yet'
        
        # Round each mean value to 2 decimal places
        for field in means:
            if means[field] != 'no data yet':
                means[field] = round(means[field], 2)

        # Save the values to the player's fields
        self.completed_count = completed_count

        self.mean_flying = means['flying'] if means['flying'] != 'no data yet' else None
        self.mean_meat = means['meat'] if means['meat'] != 'no data yet' else None
        self.mean_greenelectricity = means['greenelectricity'] if means['greenelectricity'] != 'no data yet' else None
        self.mean_nonRegionalFood = means['nonRegionalFood'] if means['nonRegionalFood'] != 'no data yet' else None
        self.mean_car = means['car'] if means['car'] != 'no data yet' else None
        self.mean_recycling = means['recycling'] if means['recycling'] != 'no data yet' else None


class Input(Page):
    form_model = "player"
    form_fields = ["flying", "meat", "greenelectricity", "car", "nonRegionalFood", "recycling"]

    def is_displayed(self): 
        return self.participant.group_assignment == "control"

class ResultsWaitPage(WaitPage):
    wait_for_all_groups = False

    def after_all_players_arrive(self):
        pass  # Custom logic will be implemented here

    def is_displayed(self):
        players = self.subsession.get_players()
        completed_count = sum(1 for p in players if p.field_maybe_none('meat') is not None and p.field_maybe_none('flying') is not None) 
        # using p.meat to acces player.meat alw
        print(f"Completed count in is_displayed: {completed_count}")
        return completed_count >= 5

    def vars_for_template(self):
        players = self.subsession.get_players()
        completed_count = sum(1 for p in players if p.field_maybe_none('meat') is not None and p.field_maybe_none('flying') is not None)
        print(f"Completed count in vars_for_template: {completed_count}")
        return {
            'completed_count': completed_count,
            'required_count': 5
        }
    

class DisplayPage(Page):
#    fields = ['meat', 'flying', 'greenelectricity', 'recycling', 'nonRegionalFood', 'car']

    form_model = "player"
    form_fields = ["flying", "meat", "greenelectricity", "car", "nonRegionalFood", "recycling"]

    def is_displayed(self):
        return self.participant.group_assignment == "experimental"

    def vars_for_template(self):
        completed_count = self.subsession.get_completed_count()
        
        all_values = self.group.get_all_values()
        means = {}
        for field, values in all_values.items():
            valid_values = [v for v in values if v is not None]
            means[field] = mean(valid_values) if valid_values else 'no data yet'

        for field in means:
            if means[field] != 'no data yet':
                means[field] = round(means[field], 2)


        return {'means': means, 'completed_count': completed_count}
    
    def before_next_page(self, timeout_happened=False):

        completed_count = self.subsession.get_completed_count()
        
        all_values = self.group.get_all_values()
        means = {}
        for field, values in all_values.items():
            valid_values = [v for v in values if v is not None]
            means[field] = mean(valid_values) if valid_values else 'no data yet'
        
        # Round each mean value to 2 decimal places
        for field in means:
            if means[field] != 'no data yet':
                means[field] = round(means[field], 2)

        # Save the values to the player's fields
        self.completed_count = completed_count

        self.mean_flying = means['flying'] if means['flying'] != 'no data yet' else None
        self.mean_meat = means['meat'] if means['meat'] != 'no data yet' else None
        self.mean_greenelectricity = means['greenelectricity'] if means['greenelectricity'] != 'no data yet' else None
        self.mean_nonRegionalFood = means['nonRegionalFood'] if means['nonRegionalFood'] != 'no data yet' else None
        self.mean_car = means['car'] if means['car'] != 'no data yet' else None
        self.mean_recycling = means['recycling'] if means['recycling'] != 'no data yet' else None

class Transition(Page):
    pass 

page_sequence = [TaskInfo, TaskInfoExp, Input , DisplayPage, Transition
                 #MeanValuesPage, MeanValuesSlider,  Input, 
                ]

