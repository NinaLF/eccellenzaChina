class Lexicon:
    next = "Next"
    small = "small (1)"
    large = "large (10)"

   # Transition page 
    #these are the exact same 4 things as in the lexicon 'Nina instructions' => we will copy the translations here
    
    transitions_first_1 = 'Welcome to the study'
    transitions_first_2= 'Great, you fulfill all criteria to participate in this study. This study consists of four parts. Please make sure you have enough time to complete this study with attention and without distractions. </p> <p> You are about to begin with the first part. Please try to complete this part in one go without any breaks. We appreciate your time and interest in participating in this study. Click "Next" when you are ready.'
    transition_title = 'Welcome to the next part of the study'
    transitions_second_1 =  'You have completed'
    transitions_second_2 = 'out of four parts of this study. Part'
    transitions_second_3 = 'is about to begin.  If you need a short break before continuing with the study, now would be a good time. '
    transitions_second_4 = 'Please try to complete the next part in one go without any breaks. We appreciate your time for participating in this study. When you are ready to proceed, please click "Next".'


    # instructions
    instructions_title = "Instructions on the next task"
    instructions_pa = "In the following we will ask you to <b>judge the climate friendliness of different carbon footprints</b>.  <br> This means we ask you to give your best estimation of <b>the size of the personal carbon footprint of a series of people with different lifestyles.</b>  The presented persons will differ with respect to <b>their diets, commuting and travel behavior as well as their electricity supply and recycling behavior</b>. <br> "
    instructions_pb = "A personal carbon footprint refers to the total amount of greenhouse gases (including CO<sub>2</sub>  and methane) that are emitted into the atmosphere as a result of an individual,s behavior. <br> The carbon footprint thus includes emissions from driving, flying, using electricity, cooling or heating your home, purchasing goods and other sources. <br> It is measured in CO<sub>2</sub>  equivalents, so that other greenhouse gases additional to CO<sub>2</sub>  (e.g., methane) are also included. <br> <br> In other words, <b>a personal carbon footprint reflects an individual,s total impact on the climate system</b>. "
    instructions_pc = "Please note that the individual carbon footprints you will assess are <b>simplified</b>, based on only 6 behaviors, so they do not account for a person,s entire carbon footprint.  <br>     You will be asked to make this judgment on a <b>scale from 1 (low carbon footprint) to 10 (large carbon footprint).</b>   <br> This means you do not have to estimate any numbers. Based on the 6 behaviors, a small carbon footprint (for a person in the United States) would equal about 0.7 ton of CO<sub>2</sub>  per year and a large carbon footprint about 5.3 tons of CO<sub>2</sub> . On the scale of 1 to 10, each increase of 1 (e.g., from 2 to 3 or from 7 to 8) corresponds to an increase of about 500 kg of CO<sub>2</sub> . <br>  "
    instructions_pd = "Next you will see how the task will look like.<br> Then we ask you to <b>estimate the carbon footprints of 16 persons with different lifestyles </b> ."
    
    # task_example
    example_pa = 'This is how a carbon footprint of an individual looks like in our task. <br>'
    example_pb = 'The different lifestyles of these individuals refer to: <ul> <li> <b>Dietary behavior:</b> The respective person either follows a <b>meat-based diet (omnivorous)</b> or a <b>plant-based diet (vegetarian)</b> </li> <li> <b>Recycling behavior:</b> The respective person either <b>recycles comprehensively</b> or <b>does not recycle</b> </li>  <li> <b>Regionality of food purchases:</b> The respective person either buys and consumes <b>mainly regional food </b> or <b>also imported</b> food items </li><li> <b>Electricity supply based on 7000 kWh energy demand of a person:</b> The respective person either subscribed to an electricity supply that is <b>mixed, so includes fossil sources and 40% renewable sources </b> or <b>based 100% on renewable energy sources</b> </li> <li> <b>Commuting to work:</b> The respective person either commutes a total of 20km to and from work everyday, 5 days a week for 48 weeks per year <b>by bike</b>  or <b>by bus</b> </li> <li> <b>Traveling on vacation:</b> The respective person either <b>takes two medium distance flights a year (=3-6hours)</b> or <b>or takes the train (e.g. Boston-New York or LA-San Francisco)</b> </li>'
    example_pc = ' <i>That is, in the example above, the person follow a vegetarian diet, does not recycle, eats regional and imported food,subscribed to a mixed electricity supply, commutes every weekday to work by bus, and takes the train to go on vacation.</i>  <br> '
    example_pd = 'Next, you will estimate the carbon footprint of <b>16</b> persons with different lifestyles. <br> Please look at each individual carbon footprint carefully and take some time to provide your estimation. <br> The order in which the 6 behaviors are presented will change across the 16 examples you will see.'
    example_pic = '/static/global/images/example_en.png '

    ## comprehension
    comprehension_title = 'Since you have just read a lot of information, we would like to ensure that you have understood one key aspect: Please indicate how many kg CO<sub>2</sub> are associated with each increase of one unit on the scale:'
    
    comprehension_a= 'each increase of 1 on the scale corresponds to 200 kg CO2  '
    comprehension_b= 'each increase of 1 on the scale corresponds to 500 kg CO2  '
    comprehension_c = 'each increase of 1 on the scale corresponds to 900 kg CO2  '

    ## attention check study is about what screenout
    interlude_title = "Brief Interruption"
    interlude_header = "This study has one superordinate topic. Have you paid attention and do you know what this study is about? Please choose the correct answer carefully."
    aboutWhatLabel = "What is this study about?"

    about_a = "City Tourism"
    about_b = "Climate Change"
    about_c = "Washing Machines"
    about_d = "Preference for spicy food"


    ## screenouts 
    screenout_title = "Participation not possible."
    screenout_sentence = "Sorry, your previous results indicated that you did not pay enough attention. You therefore cannot participate in this study."

   