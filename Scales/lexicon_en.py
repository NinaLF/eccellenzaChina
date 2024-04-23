class Lexicon:
    instructions = "Instructions"
    next = "Next"
    no = "No"
    results = 'Results'
    round_number = "Round no."
    start = "Start"
    stop = "Stop"
    yes = "Yes"
    your_decision = "Your decision"
    not_at_all = "not at all"
    very_much = "very much"
    
    completely_agree = "completely agree"
    completely_disagree = "completely disagree"

    do_not_believe = "I do not believe that climate change is happening"
    
    dont_know = "Don't know"
    opposed_to_values = "opposed to my values"
    not_important = "not <br> important"
    not_at_all_important = "not at all important"
    extremely_important = "extremely <br>  important"

   
    somewhat_liberal = "Somewhat Liberal"
    moderate = "Moderate"
    somewhat_conservative = "Somewhat Conservative"
    no_trust_at_all = "Totally distrust"
    full_trust = "Totally trust"
    completely_false = "Completeley False"
    completely_true = "Completely True"

    
    ## belief in climate change 
    beliefCC_intro = "Climate change refers to the idea that the world’s average temperature has been increasing over the past 150 years, will increase more in the future, and that the world’s climate will change as a result. What do you think: Do you think climate change is happening?"
    belief1HappeningLabel = "I believe that climate change is real."

    ### belief in (human) causes taken from  Valkengoed
    beliefHuman_title = "What do you believe?"
    beliefHuman_header = "How much do you agree with the following statements?"
    beliefHuman1Label = "Human activities are <b> not </b> a major cause of climate change." # reversed (originally not)
    beliefHuman2Label = "Climate change is entirely caused by human activities."
    beliefHuman3Label = "The main causes of climate change are human activities." 

    beliefConseqences1Label = "Climate change currently is the greatest threat to humankind."
    beliefConseqences2Label = "Climate change will bring about serious negative consequences."
    beliefConseqences3Label = "The consequences of climate change will <b> not </b> be very serious." # reversed (originally not)

    beliefConsensLabel = "Which percentage of climate scientists agree that climate change is real and caused by human activity?"

    ##belief in solutions

    beliefSolutions1Label = "Transforming to a sustainable and climate-friendly society would reduce our national standards of living."  # reversed
    beliefSolutions2Label = "Sustainable technologies and solutions are in their infancy, and a phase-out of fossil fuels is not yet feasible." # reversed
    beliefSolutions3Label = "I think high-income countries have a greater responsibility to reduce greenhouse gas emissions than low and middle-income countries." #responsibility national
    beliefSolutions4Label = "Industry has a greater responsibility to reduce greenhouse gas emissions than individuals."  #responsibility systemic
    beliefSolutions5Label = "I would rather prepare to live with climate change than fight climate change." # adaptation


    #Climate Change Emotion Knauf/Truelove
    cce_title = "Attitudes about Climate Change"
    cce_header = "When I think of Climate Change I feel..."
    emoAng1Label = "angry"
    emoAng2Label = "mad"
    emoAng3Label = "irritated"
    emoFear1Label = "fearful"
    emoFear2Label = "afraid"
    emoFear3Label = "scared"
    emoSad1Label = "sad"
    emoSad2Label = "sorrowful"
    emoSad3Label = "unhappy"
    emoHope1Label = "hopeful"
    emoHope2Label = "optimistic"
    emoHope3Label = "upbeat"
    emoGuilt1Label = "guilty"
    emoGuilt2Label = "regretful"
    emoGuilt3Label = "remorseful"
    
    emoConcern1Label = "worried"
    emoConcern2Label = "concerned"
    emoConcern3Label = "upset"


  


   # Importance of biospheric values van der Linden, 2015   
    ibv_title = "Guiding principles in enviromental issues"
    ibv_header = "How important are the following values to you as guiding principles of your life?"
    ibv1Label = "Respecting the Earth (harmony with other species)"
    ibv2Label = "Protecting the Environment (preserving nature)"
    ibv3Label = "Preventing Pollution (protecting natural resources)"
    ibv4Label = "Unity with Nature (fitting into nature)"

  

    # Trust  in institutions in terms of cc Based on (Pan et al., 2023)
    pit_title = "Trust with regards to climate change"
    pit_header = "How much do you trust these actors in climate change?"
    pit1Label = "the local government"
    pit2Label = "the national government"


    # Knowledge Question from Allianz Climate Literacy Report
    cck_title = 'What do you know about climate change?'
    cck_header = 'Please answer all these questions to the best of your knowledge, without looking up any information. You may choose the "I do not know" option if you are unsure or do not know'
    know_dontknow = "I don't know."

    know_1qu = "What is the COP?" ## This is maybe too easy given that the whole study is about CC???
    know_1a = "UN initiative for distributing funds to reduce the impact of climate change on poverty."
    know_1b = "An annual formal meeting to discuss climate change and establish mitigation actions."
    know_1c = "An EU initiative for multinational cooperation against organized crime." 
    
    know_2qu = "What does Net-Zero mean?"
    know_2a = "Monetary strategy of increasing interest rate to fight inflation."
    know_2b = "No greenhouse gas emission by a specific date, typically 2050."
    know_2c = "Carbon emission neutrality, stabilization of greenhouse gas concentrations in the atmosphere."
    
    know_3qu = "The Intergovernmental Panel on Climate Change (IPCC) plays an important role in global climate policy. Which one?"
    know_3a = "Providing objective scientific information relevant to understanding climate change."
    know_3b = "Deciding on global climate policies, particularly setting the global carbon price."
    know_3c = "Host of the UN climate justice court which arbitrates climate disputes between states."
    
    know_4qu = "What is the carbon market?"
    know_4a = "The supply channel of the EU backed gas-buying cartel that aims to supply affordable natural gas to EU countries struggling to get supply because of the war in Ukraine."
    know_4b = "A trading system through which emitters may buy or sell units of greenhouse-gas emission allowances to meet national restrictions on total emissions."
    know_4c = "An online marketplace where you can buy recycled carbon fiber and carbon black."
    

    ## I suggest a modification of tis question:
    #Rising temperatures pose no existential threat. Even if the rise exceeds 3°C, humans and nature can adapt. Do you agree with this statement?"
    know_5qu = "How long does CO2 stay in the atmosphere?"
    know_5a = "10 years"
    know_5b = "up to 1000 years"
    know_5c = "more than 5000 years"

    
    ## I suggest a modification of this question
    know_6qu = "Which of the following options describes the greenhouse gas effect"
    # old was Climate change cannot be stopped. Average temperatures will continue to increase in the near future. The only thing we can possible do is to limit the increase to 1.5°C."
    know_6a = "Deforestation and plastic pollution cause a collapse of many ecosystems. The increasing loss of biodiversity and the loss of flora and fauna in the wild is called the greenhouse gas effect."
    know_6b = "Greenhouse gasses cause air pollution. They lead to more fine particulars and more fine dust which in turn decreases the ventilation. Without the circulation of fresh air, the earth gets increasingly warmer. "
    know_6c = "Excess greenhouse gases accumulate in the atmosphere. Because of their molecular structure, the infrared radiation from the earth is reflected and is re-radiated to the earth. This way, heat is trapped."
    
    
    know_7qu = "At current rates, after how many years we will have burnt our CO2-budget to limit the temperature rise to 1.5C?" # this will be September 2026 (Stand 2023)
    know_7a = "less than 1 year"
    know_7b = "1-2 years"
    know_7c = "2-4 years"
    know_7d = "More than 4 years"
    

    know_8qu = "Which country/region causes the highest absolute CO2-emissions per year?"
    know_8a = "China"
    know_8b = "USA"
    know_8c = "EU"
    know_8d = "India"

    know_9qu = "Which country/region causes the highest per-capita CO2-emissions per year?"
    know_9a = "China"
    know_9b = "USA"
    know_9c = "EU"
    know_9d = "India"
    
    ### Behaviors ###
    behaviors_title = ' Behavior '
    intro_a = 'In this section we ask about your habits and actual behavior. Please answer as accurately as possible. Thank you very much!'
    regional_label = ' What percentage of your food is regional (from within your country or region, not imported) ? '
    regional_less_than = 'Less than a quarter'
    regional_quarter= 'About a quarter' 
    regional_half = 'About half' 
    regional_3_quarter = 'About three quarters'
    regional_more_than = 'the largest part is regional'

    electricity_label = 'This question is about your electricity supply. What does your electricity supply look like?'
    electricity_D = 'I have green electricity entirely '
    electricity_C = 'I partly have green electricity (mixed)' 
    electricity_B = ' I have a conventional (fossil) supply'
    electricity_A = 'I don,t know'

    food_overall_text = ' In the last month, how many times did you eat the following food items...'
    food_overall_label1 = 'Beef'
    food_overall_label2 = 'Lamb or mutton'
    food_overall_label3 = 'Pork'
    food_overall_label4 = 'Poultry (e.g. chicken)'
    food_overall_label5 = 'Fish'
    food_overall_label6 = 'Dairy products (e.g milk or cheese)'

    food_overall_A = 'Never'
    food_overall_B = 'Once a month'
    food_overall_C= '2-3 times per month'
    food_overall_D = 'Once a week'
    food_overall_E = '2-3 times per week'
    food_overall_F = '4-6 times per week'
    food_overall_G = 'Once a day'
    food_overall_H = '2 or more times per day'



    commute_pt_label = 'How many kilometers do you <b> commute weekly in public transport </b> (train, bus, etc.)or an e-bike? Please calculate all private journeys including the work commute, but not business travels.'
    commute_pt_never = 'I never use public transport'
    commute_pt_less_than_A = '1 - 39 miles'
    commute_pt_A_to_B= '40 - 50 miles'
    commute_pt_B_to_C = '50 -149 miles'
    commute_pt_C_to_D = '150 - 224 miles'
    commute_pt_D_to_E = '225 - 370 miles'
    commute_pt_more_than_E = 'more than 370 miles'

    commute_car_label = 'How many kilometers do you <b> annually drive in a car </b> or on a motorcycle (outside of work times, both driving and as a passenger)?'
    commute_car_never = 'I never use a car or motorcycle'
    commute_car_less_than_A = '1 - 1,244 miles'
    commute_car_A_to_B= '1,245 - 4,659 miles'
    commute_car_B_to_C = '4,660 - 7,769 miles'
    commute_car_C_to_D = '7,770 - 18,640 miles'
    commute_car_more_than_D = 'more than 18,640 miles'

    commute_car_type_label = 'Which kind of fuel does your car operate on?'
    commute_car_type_none = 'I do not have a car'
    commute_car_type_E = 'Gasoline/Diesel/Hybrid'
    commute_car_type_D = 'Natural gas'
    commute_car_type_C = 'Biogas'
    commute_car_type_B = 'Electric (conventional energy) '
    commute_car_type_A = 'Electric (green energy)'

    flying_short_label = 'How many <b>short-distance flights (<3 hours)</b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from San Francisco to Los Angeles and back this counts as 2 flights. </i> '
    # for chinese version example:  from Shanghai to Beijing and back
    flying_mid_label ='How many <b>mid-distance flights (3-6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from New York to San Francisco and back this counts as 2 flights. </i> '
    #for chinese version example:  from Guangzhou to Beijing and back
    flying_long_label = 'How many <b>long-distance flights (>6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from Miami to London and back this counts as 2 flights. </i> '
    # for  chinese version example: from Beijing to Jakarta (Indonesia) and back


    ### policies scales
    policies_title = ' Some additional questions on Policies '

    policy1Label =	'Increase or introduce taxes on fuel for vehicles (i.e. diesel and gasoline)'
    policy2Label =	'Increase or introduce taxes on air travel.'
    policy3Label =	'Increase or introduce taxes on fossil fuels as energy source (i.e. gas, oil, and coal)'
    policy4Label =	'Increase or introduce taxes on red meat (e.g., beef, lamb, veal).'
    policy5Label =	'Increase or introduce taxes on non-recyclable materials'
    policy6Label =	'Increase or introduce taxes on food products imported via plane'
	
    strongly_opoose =	'strongly oppose'
    strongly_support =	'strongly support'
	
    intro_policies1 ='In the following, we will ask for your views on different public policies. Please answer them as truthfully as possible. <br> '
    intro_policies2 ='Many countries have introduced new policies to reduce the risk of climate change. This includes policies that require or create incentives for reductions in greenhouse gas emissions across domains and actors. <br>'

 
    ### Demographics
    demographics_title = "Personal data"
    demographics_header = "Please enter the following information about yourself."
    
    ageYear_label = "In which year were you born?"

    residential_area_label = "What describes your residential area best?"
    metropolitan_area = "Metropolitan Area"
    suburban = "Suburban Area"
    rural = "Rural Area"

    zip_code_label = "What is your Zip Code? (Answering this question is optional.)"
    
    party_affiliation_label = "Which party would you be most likely to vote for?"
    republicans = "Republicans"
    democrats = "Democrats"
    independent_party = "Independent Party"
    other_party = "Other"

    # Transition page
    transition_title = 'Welcome to the last block of the study'
    
    # these are the exact same 4 things as in the lexicon 'Nina instructions' => we will copy the translations here
    transitions_a = 'Thank you very much for your responses so far. If you need a short break before continuing with the study, now would be a good time. <br> Once you click on the next button on this page, we ask you to please complete this block in one go.'
    # add counter (Zahra)
    transitions_b =' This is the last  '
    transitions_c = 'out of 4 blocks. Thank you for taking the time to complete everything so far. <br> When you are ready to proceed, please click "Next".'


    householdsize_label = 'How many people live in your household?'

    
    states_label = 'Please indicate in which state you live'
    BW = 'Baden-Württemberg'
    Bayern = "Bayern"
    Berlin = "Brtlin"
    Brandenburg = "Brandenburg"
    Bremen = "Bremen",
    Hamburg = "Hamburg"
    Hessen = "Hessen"
    MV = "Mecklenburg-Vorpommern"
    Niedersachsen = "Niedersachsen"
    NRW = "Nordrhein-Westfalen"
    RP = "Rheinland-Pfalz"
    Saarland = "Saarland"
    Sachsen = "Sachsen"
    SA = "Sachsen-Anhalt"
    SH = "Schleswig-Holstein"
    Thüringen = "Thüringen"
   
    Alabama = "Alabama"
    Alaska=    "Alaska"
    Arizona=    "Arizona"
    Arkansas=    "Arkansas"
    California=    "California"
    Colorado=    "Colorado"
    Connecticut=    "Connecticut"
    Delaware=    "Delaware"
    Florida=    "Florida"
    Georgia=    "Georgia"
    Hawaii=    "Hawaii"
    Idaho=    "Idaho"
    Illinois=    "Illinois"
    Indiana=    "Indiana"
    Iowa=    "Iowa"
    Kansas=    "Kansas"
    Kentucky=    "Kentucky"
    Louisiana=    "Louisiana"
    Maine=    "Maine"
    Maryland=    "Maryland"
    Massachusetts=    "Massachusetts"
    Michigan=    "Michigan"
    Minnesota=    "Minnesota"
    Mississippi=    "Mississippi"
    Missouri=    "Missouri"
    Montana=    "Montana"
    Nebraska=    "Nebraska"
    Nevada=    "Nevada"
    NewHampshire=   " New Hampshire"
    NewJersey=   "New Jersey"
    NewMexico=  "New Mexico"
    NewYork=    "New York"
    NorthCarolina=    "North Carolina"
    NorthDakota=    "North Dakota"
    Ohio=    "Ohio"
    Oklahoma=    "Oklahoma"
    Oregon=    "Oregon"
    Pennsylvania=    "Pennsylvania"
    RhodeIsland=   " Rhode Island"
    SouthCarolina=   " South Carolina"
    SouthDakota=   " South Dakota"
    Tennessee=    "Tennessee"
    Texas=    "Texas"
    Utah=    "Utah"
    Vermont=    "Vermont"
    Virginia=    "Virginia"
    Washington=    "Washington"
    WestVirginia=    "West Virginia"
    Wisconsin=    "Wisconsin"
    Wyoming=    "Wyoming"

    Anhui="安徽"
    Peking="北京"
    Chongqing="重庆"
    Fujian="福建"
    Guangdong="广东"
    Guangxi="广西"
    Gansu="甘肃"
    Guizhou="贵州"
    Henan="河南"
    Hebei="河北"
    Hunan="湖南"
    Hubei="湖北"
    Hainan="海南"
    Heilongjiang="黑龙江"
    Jilin="吉林"
    Jiangsu="江苏"
    Jiangxi="江西"
    Liaoning="辽宁"
    InnereMongolei="内蒙古"
    Ningxia="宁夏"
    Qinghai="青海"
    Sichuan="四川"
    Shandong="山东"
    Shanxi="山西"
    Shannxi="陕西"
    Schanghai="上海"
    Tianjin="天津"
    Xinjiang="新疆"
    Tibet="西藏"
    Yunnan="云南"
    Zhejiang="浙江"
    Hongkong="香港"
    Taiwan="台湾"
    Macao="澳门"

    

