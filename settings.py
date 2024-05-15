from os import environ

SESSION_CONFIGS = [
     
      dict(
         name='Intro_Redirection_ch',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "zh_hans",
         num_demo_participants=10,
     ),
     dict(
         name='new_Order_Nina_Jessi__zh',
         app_sequence=['FirstBlock',  'Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax', 'Scales', 'Goodbye'],
         language = "zh_hans",
         num_demo_participants=10,
     ), 
     dict(
         name='new_Order_Jessi_Nina_zh',
         app_sequence=['FirstBlock', 'Jessi_Instructions',  'Jessi_carbonTax', 'Nina_instructions', 'Nina_carbontask', 'Scales', 'Goodbye' ],
         language = "zh_hans",
         num_demo_participants=10,
     ),
     dict(
         name='testEnd',
         app_sequence=['FirstBlock', 'Goodbye' ],
         language = "zh_hans",
         num_demo_participants=10,
     ),
     dict(
         name='EnglishVersion',
         app_sequence=['FirstBlock', 'Jessi_Instructions',  'Jessi_carbonTax', 'Nina_instructions', 'Nina_carbontask', 'Scales', 'Goodbye' ],
         language = "en",
         num_demo_participants=10,
     ),
     dict(
         name='EnglishVersionForPDF',
         app_sequence=['FirstBlock', 'Jessi_Instructions', 'Scales', 'Goodbye' ],
         language = "en",
         num_demo_participants=10,
     ),
      dict(
         name='Intro_Redirection_en',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "en",
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

PARTICIPANT_FIELDS = [

    ## Overall Structure
    'order_tasks',
    'pLangCode',
    'task_counter',

     #CC SAMPLING FIELDS
    
     #'telling_box_label',

    ## carbon footprint task
    'task_rounds',

    # carbonTaxTask
    'task_rounds_J'
    
    ]
SESSION_FIELDS = [
    'introLexi',
    'firstBlockLexi',
    

    'introNinaLexi',
    'carbonTaskLexi',

    'JessiTaskLexicon',
    'JessiIntroLexi',
    
    'scalesLexi',

    'GoodbyeLexi',

    'myLangCode'
]

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
