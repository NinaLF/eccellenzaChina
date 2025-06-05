class Lexicon:
    next = "下一个"
    small = "小 (1)"
    large = "大 (10)"

    # transition
    #transition_title = '欢迎来到研究的下一个部分'

    #transitions_a = '非常感谢您迄今为止的回答。如果您在继续学习之前需要短暂休息，那么现在是个好时机。 <br> 单击此页面上的下一个按钮后，我们要求您一次性完成此块'
    # we will need to add a counter and then display that variable in the page, not sure how to integrate it in the lexicon 
    #transitions_b = '这是区块号 '
    #transitions_c = '共 4 个区块。 再次感谢您花时间回答所有问题。 <br>一旦你准备好了，请继续。'

    transitions_first_1 = '欢迎参加本研究'
    transitions_first_2= '太好了，你满足了参与这项研究的所有标准。本学习包括三个部分。您即将开始第一部分。请尽量一次性完成这一部分，不要间断。感谢您抽出时间参与本研究。准备好后，请单击 "下一个"。'
    transition_title = '欢迎来到研究的下一个部分'
    transitions_second_1 =  '您已完成本研究三个部分中的  '
    transitions_second_2 = '部分。第 '
    transitions_second_3 = '部分即将开始。 如果你在继续这项研究之前需要短暂休息，现在是个好时机。 '
    transitions_second_4 = '请尽量一次性完成下一部分，不要中断。感谢您抽出时间参与本研究。 准备就绪后，请点击 "下一个"。'

    

    # instructions
    instructions_title = '关于下一步任务的指示'
    instructions_pa =  "接下来我们将要求您<b>判断不同碳足迹的气候友好性</b>。<br>这意味着我们要求您对<b>一系列具有不同生活方式的人的个人碳足迹的大小做出最佳估计。</b>所呈现的人在<b>他们的饮食、通勤和旅行行为以及电力供应和回收行为方面会有所不同</b>。<br>"
    instructions_pb =   "个人碳足迹是指因个人行为而排放到大气中的温室气体（包括二氧化碳和甲烷）总量。<br>因此，碳足迹包括驾驶、飞行、使用电力、家庭制冷或供暖、购买商品和其他来源。<br>它以 CO<sub>2</sub>  当量衡量，因此除 CO<sub>2</sub>  之外的其他温室气体（例如甲烷）也包括在内。<br> <br>换句话说，<b>个人碳足迹反映了个人对气候系统的总体影响</b> 。"
    instructions_pc =   "请注意，您将评估的个人碳足迹是<b>简化的</b>，仅基于 6种行为，因此它们不会考虑一个人的整个碳足迹。<br>您将被要求从1（低碳足迹）到10（大碳足迹）这个范围做出此判断。</b><br>这意味着您不必估计任何数字。根据6种行为，小碳足迹（对于中华人民共和国的一个人来说）每年大约相当于0.7吨二氧化碳，而较大的碳足迹大约相当于5.3吨二氧化碳。 在 1 到 10 的范围内，每增加 1（如从 2 到 3 或从 7 到 8）就相当于增加约 500 千克二氧化碳 。 <br>"
    instructions_pd =  "接下来您将看到任务会是怎样。<br>然后我们要求您<b>估算 16 名不同生活方式的人的碳足迹</b>。"
    
    # task_example
    example_pa = '这就是我们任务中个人碳足迹的样子。<br>'
    ##for chinese version please adapte this example:  "takes the train (e.g.from Shanghai to Beijing" or Beijing to Guangzhou)" rather than "takes the train (e.g. Boston-New York or LA-San Francisco)"
    example_pb = '这些人的不同生活方式是指：<ul> <li> <b>饮食行为：</b>相关人要么遵循<b>以肉为主的饮食（杂食性）</b>，要么 <b> 植物性饮食（素食）</b> </li> <li> <b> 回收行为：</b>相关人<b> 全面回收 </b> 或 <b> 不回收 </b> </li> <li> <b> 食品购买的地区性：</b>相关人购买和消费<b>主要是地区食品</b>或<b>也进口</b>食品项目</li><li> <b>基于个人 7000 千瓦时能源需求的电力供应 : </b>  相关人员要么订购了混合电力供应， <b> 即包括化石能源和 40% 的可再生能源，</b> <b> 要么 100% 使用可再生能源</b> </li> <li> <b>通勤：</b> 相关人每周 5 天，每天上下班总计 20 公里，每年持续 48 周 <b>骑自行车</b>或<b>乘坐公共汽车</b> </li> <li> <b>度假旅行：</b>相关人<b>每年乘坐两次中等距离 的飞行（=3-6小时）</b>或<b>或乘坐火车（例如上海-北京或北京-广州）</b> </li>'
   #    example_pb = <b>Electricity supply based on 7000 kWh energy demand of a person:</b> The respective person either subscribed to an electricity supply that is <b>mixed, so includes fossil sources and 40% renewable sources </b> or <b>based 100% on renewable energy sources</b> 

    example_pc = '<i>也就是说，在上面的例子中，这个人遵循素食、不回收、吃当地和进口食品、订购混合电力供应、每个工作日乘公共汽车上班、乘火车去度假。</i> <br> '
    example_pd = '接下来，您将估算<b>16</b>位不同生活方式的人的碳足迹。<br>请仔细查看每个碳足迹，并花一些时间提供您的估计。 <br>在您将看到的16个示例中，6种行为的呈现顺序将发生变化。'
    example_pic = '/static/global/images/example_zh_hans.png '  # no need to change the link

     ## comprehension
    comprehension_title = '由于您刚刚阅读了大量信息，我们希望确保您已了解一个关键方面：请指出级别上每增加一个单位与多少千克 CO<sub>2</sub> 相关：'
    
    comprehension_a= '刻度每增加 1 相当于 200 千克二氧化碳'
    comprehension_b= '刻度上每增加 1 相当于 500 千克二氧化碳'
    comprehension_c='刻度上每增加 1 相当于 900 千克二氧化碳 '

     ## attention check study is about what screenout
    interlude_title = "短暂中断"
    interlude_header = "这项研究有一个上位主题。 你有注意过吗？你知道这项研究是关于什么的吗？ 请仔细选择正确答案。"
    aboutWhatLabel = "这项研究是关于什么的？"

    about_a = "城市旅游"
    about_b = "气候变化"
    about_c = "洗衣机"
    about_d = "对辛辣食物的偏好"
    
    ## screenouts 
    screenout_title = "不可能参与。"
    screenout_sentence = "抱歉，您之前的结果表明您没有足够地重视，因此您不能参与这项研究。"
