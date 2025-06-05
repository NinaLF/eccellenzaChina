from os import environ

SESSION_CONFIGS = [
     dict(
         name='intervention',
         app_sequence=['Intervention_de'],
         num_demo_participants=10,
     ),
     dict(
         name='intervention_en',
         app_sequence=['Intervention'],
         num_demo_participants=10,
     ),
     dict(
         name='testQuota',
         app_sequence=['Intro_t1', 'Scales_t1' ],
         num_demo_participants=10,
     ),

      dict(
         name='scales',
         app_sequence=['Scales_t1_de', 'Scales_t2_de'],
         num_demo_participants=10,
     ),
     dict(
         name='carbontask',
         app_sequence=['Nina_carbontask'],
         num_demo_participants=10,
     ),
     
     dict(
         name='carbontask_de',
         app_sequence=['Nina_carbontask_de'],
         num_demo_participants=10,
     ),

      dict(
         name='study_t1',
         app_sequence=[ 'Intro_t1', 'Nina_instructions', 'Nina_carbontask', 'Scales_t1'],
         num_demo_participants=10,
     ),
      dict(
         name='study_t1_de',
         app_sequence=[ 'Intro_t1_de', 'Nina_instructions_de', 'Nina_carbontask_de', 'Scales_t1_de'],
         num_demo_participants=10,
     ),

     dict(
         name='study_t2',
         app_sequence=[ 'Intro_t2', 'Intervention', 'Nina_instructions', 'Nina_carbontask', 
                        'Scales_t2'],
         num_demo_participants=10,
     ),

     dict(
         name='study_t2_de',
         app_sequence=[ 'Intro_t2_de','Intervention_de', 'Nina_instructions_de', 'Nina_carbontask_de', 
                        'Scales_t2_de'],
         num_demo_participants=10,
     ),

      dict(
         name='study_t3_de',
         app_sequence=[ 'Intro_t3_de', 'Nina_instructions_de', 'Nina_carbontask_de', 
                        'Scales_t3_de'],
         num_demo_participants=10,
     ),
     dict(
         name='study_t3',
         app_sequence=[ 'Intro_t3',  'Nina_instructions', 'Nina_carbontask', 
                        'Scales_t3'],
         num_demo_participants=10,
     ),

 
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [ 'group_assignment', 'diet', 'electricity', 'recycling', 'food', 'commute', 'vacation',
                      'task_rounds', 'quota_full']
SESSION_FIELDS = [ 'num_female_de', 'num_male_de', 
                  'num_age1_de', 'num_age2_de', 'num_age3_de', 'num_age4_de',
                  'num_female_uk', 'num_male_uk',
                  'num_age1_uk', 'num_age2_uk', 'num_age3_uk', 'num_age4_uk']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5553960384234'
