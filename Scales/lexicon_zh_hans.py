class Lexicon:
    next = "下一个"
    instructions = "指示"
    no = "No"
    round_number = "Round no."

    yes = "Yes"
    not_at_all = "一点也不"
    very_much = "非常"
    
    completely_agree = "完全同意"
    completely_disagree = "完全不同意"

    do_not_believe =  "我不相信气候变化正在发生"
    
    dont_know = "不知道"
    
  
    #Scale anchors 

    opposed_to_values = "违背我的价值观"
    not_important = "不重要"
    extremely_important = "极其 <br> 重要"
    
    no_trust_at_all = "完全不信任"
    full_trust = "完全信任"



     ## belief in climate change 
    beliefCC_intro = "气候变化是指世界平均气温在过去150年里一直在上升, 未来还会上升更多，从而导致世界气候发生变化。" #您怎么？您认为气候变化正在 发生吗？"
    belief1HappeningLabel = "我相信气候变化是真实存在的"

    ### belief in (human) causes taken from  Valkengoed
    beliefHuman_title = "你相信什么？"
    beliefHuman_header = "您对以下说法的同意程度如何？"
    beliefHuman1Label = "人类活动<b>不是</b>气候变化的主要原因。" # reversed (originally not)
    beliefHuman2Label = "气候变化完全是人类活动造成的。"
    beliefHuman3Label = "气候变化的主要原因是人类活动。"

    beliefConseqences1Label = "当前，气候变化是人类面临的最大威胁。"
    beliefConseqences2Label = "气候变化将带来严重的负面后果。"
    beliefConseqences3Label = "气候变化的后果<b>不会</b>非常严重。"# reversed (originally not)

    beliefConsensLabel = "有多少比例的气候科学家同意气候变化是真实存在的并且是由人类活动引起的？"
    ##belief in solutions

    beliefSolutions1Label = "向可持续发展和气候友好型社会转型将会降低我们国家的生活水平。"
    beliefSolutions2Label = "可持续技术和解决方案还处于起步阶段，逐步淘汰化石燃料尚不可行。"
    beliefSolutions3Label = "我认为高收入国家比中低收入国家有更大的责任减少温室气体排放。"
    beliefSolutions4Label = "在减少温室气体排放方面，工业界比个人负有更大的责任。"
    beliefSolutions5Label = "我宁愿准备适应气候变化，也不愿意与气候变化作斗争。"


    #Climate Change Emotion

    cce_title = "对气候变化的态度"
    cce_header = "当我想到气候变化时，我感觉……"
    emoAng1Label = "气愤"
    emoAng2Label = "愤恨"
    emoAng3Label = "愤怒"
    emoFear1Label = "可怕"
    emoFear2Label = "害怕"
    emoFear3Label = "恐惧"
    emoSad1Label = "伤心"
    emoSad2Label = "悲伤"
    emoSad3Label = "不开心"
    emoHope1Label = "充满希望"
    emoHope2Label = "乐观"
    emoHope3Label = "信心满满"
    emoGuilt1Label = "有罪的"
    emoGuilt2Label = "遗憾"
    emoGuilt3Label = "悔恨"
    emoConcern1Label = "担心"
    emoConcern2Label = "忧虑"
    emoConcern3Label = "沮丧"

   
    
   # Importance of biospheric values van der Linden, 2015   
    ibv_title = "环境问题的指导原则"
    ibv_header = "以下价值作为你生活的指导原则对你来说有多重要？"
    ibv1Label = "尊重地球（与其他物种和谐相处"
    ibv2Label = "保护环境（保全自然"
    ibv3Label = "防止污染（保护自然资源"
    ibv4Label = "与自然合一（融入自然"

    # Trust  in institutions in terms of cc Based on (Pan et al., 2023)
    pit_title = "对气候变化的信任"
    pit_header = "在气候变化问题上，你对这些行动者有多信任？"
    pit1Label = "当地政府"
    pit2Label =  "国家政府 (中央政府)"
  # 

    # Knowledge Question from Allianz Climate Literacy Report
    cck_title = "你对气候变化了解多少？"
    cck_header = '请尽您所知回答所有这些问题，而无需查找任何信息。如果您不确定或不知道，您可以选择"我不知道"选项 '
    know_dontknow = "我不知道。"

    know_1qu = "什么是COP ?" 
    know_1a = "联合国倡议分配资金以减少气候变化对贫困的影响。"
    know_1b ="年度正式会议讨论气候变化并制定缓解行动。"
    know_1c = "欧盟针对有组织犯罪开展跨国合作的倡议。"

    know_2qu = "净零是什么意思？"
    know_2a = "通过加息来对抗通胀的货币策略。"
    know_2b ="在特定日期（通常是 2050 年）之前不会排放温室气体。"
    know_2c ="碳排放的中和，大气中温室气体浓度的稳定。"

    know_3qu = "政府间气候变化专门委员会 (IPCC) 在全球气候政策中发挥着重要作用。是哪一个？"
    know_3a = "提供与了解气候变化相关的客观科学信息。"
    know_3b = "决定全球气候政策，特别是设定全球碳价格。"
    know_3c = "联合国气候司法法庭的东道主，负责仲裁国家之间的气候争端。"

    know_4qu = "什么是碳市场？"
    know_4a = "欧盟支持的天然气购买卡特尔供应渠道，旨在向因乌克兰战争而难以获得供应的欧盟国家提供负担得起的天然气。"
    know_4b = "排放者可以通过一个交易系统购买或出售温室气体排放配额单位，以满足国家对总排放量的限制。"
    know_4c = "一个在线市场，您可以在其中购买再生的碳纤维和炭黑。"

    know_5qu = "二氧化碳在大气中停留多长时间？"
    know_5a ="10年"
    know_5b ="长达1000年"
    know_5c ="5000多年"

    know_6qu = "以下哪一选项描述了温室气体效应"

    know_6a = "森林砍伐和塑料污染导致许多生态系统崩溃。生物多样性和野生动植物群的日益丧失被称为温室气体效应。"
    know_6b = "温室气体造成空气污染。它们会产生更多的细小颗粒和更多的细尘，从而减少换气。如果没有新鲜空气的循环，地球就会变得越来越温暖。"
    know_6c = "过量的温室气体在大气中积聚。由于其分子结构，来自地球的红外辐射被反射并重新辐射到地球。这样，热量就被困住了。"

    know_7qu = "按照目前的速度，多少年后我们会耗尽二氧化碳预算才能将气温上升限制在 1.5 摄氏度以内？"
    know_7a = "不到1年"
    know_7b = "1-2年"
    know_7c = "2-4年"
    know_7d = "4年多"

    know_8qu = "哪个国家/地区的二氧化碳年绝对排放量最高？"
    know_8a = "中国"
    know_8b="美国"
    know_8c ="欧洲联盟"
    know_8d = "印度"

    know_9qu = "哪个国家/地区的人均二氧化碳排放量最高？"
    know_9a = "中国"
    know_9b ="美国"
    know_9c ="欧洲联盟"
    know_9d = "印度"

    
    ### Behaviors ###
    behaviors_title = '行为'
    intro_a = '在下一部分中，我们将收集有关您的一些实际行为的信息。 <br>请尽可能准确地回答。 先感谢您！'
    regional_label = '您的食品中有多少比例是区域性的（来自您所在国家或地区，而非进口）？'
    regional_less_than = '不到四分之一'
    regional_quarter= '大约四分之一'
    regional_half = '大约一半'
    regional_3_quarter = '大约四分之三'
    regional_more_than = '最大的部分是区域性的'

    electricity_label = '这个问题是关于你们的电力供应的。你们的电力供应情况如何？'
    electricity_D = '我完全拥有绿色电力'
    electricity_C = '我有部分绿色电力（混合）'
    electricity_B = ' 我有传统（化石）供应'
    electricity_A = '我不知道'

    food_overall_text = ' 在过去的一个月里，您吃了多少次下列食物......'
    food_overall_label1 = '牛肉'
    food_overall_label2 = '羔羊肉或羊肉'
    food_overall_label3 = '猪肉'
    food_overall_label4 = '家禽（例如鸡肉）'
    food_overall_label5 = '鱼'
    food_overall_label6 = '乳制品（例如牛奶或奶酪）'

    food_overall_A = '绝不'
    food_overall_B = '每月一次'
    food_overall_C= '每月 2-3 次'
    food_overall_D = '一个星期一次'
    food_overall_E = '每周 2-3 次'
    food_overall_F = '每周 4-6 次'
    food_overall_G = '一天一次'
    food_overall_H = '每天 2 次或以上'



    commute_pt_label = '您<b>每周乘坐公共交通工具</b>（火车、公共汽车等）或电动自行车通勤多少公里？ 请计算所有私人旅程，包括工作通勤，但不包括商务旅行。'
    commute_pt_never = '我从不使用公共交通工具'
    commute_pt_less_than_A = '1 - 60 公里'
    commute_pt_A_to_B= '60 - 80 公里'
    commute_pt_B_to_C = '80 -239 公里'
    commute_pt_C_to_D = '240 - 359 公里'
    commute_pt_D_to_E = '360 - 600 公里'
    commute_pt_more_than_E = '超过 600 公里'

    commute_car_label = '您<b>每年驾驶汽车</b>或摩托车（工作时间之外，无论是驾驶还是作为乘客）行驶多少公里？'
    commute_car_never = '我从不使用汽车或摩托车'
    commute_car_less_than_A = '1 - 2,000 公里'
    commute_car_A_to_B= '2,000 - 7,499 公里'
    commute_car_B_to_C = '7,500 - 12,499 公里'
    commute_car_C_to_D = '12,500 - 30,000 公里'
    commute_car_more_than_D = '超过  30,000 公里'

    commute_car_type_label = '您的汽车使用哪种燃料？'
    commute_car_type_none = '我没有车'
    commute_car_type_E = '汽油/柴油/混合动力'
    commute_car_type_D = '天然气'
    commute_car_type_C = '沼气'
    commute_car_type_B = '电力（常规能源）'
    commute_car_type_A = '电力（绿色能源）'

    flying_short_label = '过去两年您平均乘坐了多少次<b>短途航班（<3 小时）</b>？<i> i：一个往返航班算作两个航班。 因此，如果您从上海飞往北京并返回，则算作 2 趟航班。</i>'
    # for chinese version example:  from Shanghai to Beijing and back
    flying_mid_label ='过去两年您平均乘坐了多少次<b>中程航班（3-6 小时）</b>？<i> i：一个往返航班算作两个航班。 因此，如果您从广州飞往北京并返回，则算作 2 趟航班。</i>'
    #for chinese version example:  from Guangzhou to Beijing and back
    flying_long_label = '过去两年您平均乘坐了多少次<b>长途航班（>6 小时）</b>？<i> i：一个往返航班算作两个航班。因此，如果您从北京飞往雅克拉达（印度尼西亚）并返回，则算作 2 趟航班。</i>'
    # for  chinese version example: from Beijing to Jakarta (Indonesia) and back

    ### policies scales translations here
    policies_title = ' 关于政策的一些补充问题 '

    policy1Label =	'对车辆燃料（即柴油和汽油）增加或开始征收税。'
    policy2Label =	'对航空旅行增加或开始征收。'
    policy3Label =	'对作为能源的化石燃料（即天然气、石油和煤炭）增加或开始征收税。'
    policy4Label =	'对红肉（例如牛肉、羊肉、小牛肉）增加或开始征收税。'
    policy5Label =	'对不可回收材料增加或开始征收税。'
    policy6Label =	'对通过飞机进口的食品增加或开始征收税。'
	
    strongly_opoose =	'强烈反对'
    strongly_support =	'强烈支持'
	
    intro_policies1 ='接下来，我们将征求您对不同公共政策的看法。 请尽可能如实回答。 <br> '
    intro_policies2 ='许多国家出台了新政策来降低气候变化风险。 这包括要求或制定激励措施以减少跨领域和实体的温室气体排放的政策。 <br>'


 
    
    ### Demographics
    demographics_title = "个人数据" 
    demographics_header = "请输入以下有关您自己的信息。"

    ageYear_label = "你是哪一年出生的？"


    residential_area_label = "什么最能描述您的居住区？"
    metropolitan_area = "大都市区"
    suburban = "郊区"
    rural = "农村"
    
    #not relevant for China 
    party_affiliation_label = "Which party would you be most likely to vote for?"
    republicans = "Republicans"
    democrats = "Democrats"
    independent_party = "Independent Party"
    other_party = "Other"

    zip_code_label = "邮政编码（自愿）"


    # Transition page these are the exact same 4 things as in the lexicon 'Nina instructions' => we will copy the translations here
    transition_title = "欢迎来到研究的最后一个部分"
  
    transitions_a = '非常感谢您迄今为止的回答。如果您在继续学习之前需要短暂休息，那么现在是个好时机。 <br> 单击此页面上的下一个按钮后，我们要求您一次性完成此块'
    # we will need to add a counter and then display that variable in the page, not sure how to integrate it in the lexicon 
    transitions_b = '这是区块号 '
    transitions_c = '共 3 个区块。 再次感谢您花时间回答所有问题。 <br>一旦你准备好了，请继续。'

    
    
    
    # goodbye page 
    comment_label = '如果您对本研究有任何意见或建议，请在此注明：'
    goodbye_text = '感谢您参与我们的研究！ <br> 您现在处于研究结束阶段。如需获得补偿，请点击下一步。'
  
    # adapt link
    link = 'https://www.innofact-umfrage.de/sample_only/ub3/cn/danke_f.php'


    householdsize_label = '你家里有多少人住？'


    
    states_label = '请指出你住在哪个省份。'
    BW = 'Baden-Württemberg'
    Bayern = "Bayern"
    Berlin = "Berlin"
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

    Anhui= "安徽"
    Peking= "北京"
    Chongqing= "重庆"
    Fujian= "福建"
    Guangdong= "广东"
    Guangxi= "广西"
    Gansu= "甘肃"
    Guizhou= "贵州"
    Henan= "河南"
    Hebei= "河北"
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
 


    
    

