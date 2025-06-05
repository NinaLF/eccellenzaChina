class Lexicon:
    next = "Weiter"

    # transition
    transitions_first_1 = 'Willkommen zu der Studie'
    transitions_first_2= 'Sehr schön! Sie erfüllen alle Kriterien, um an dieser Studie teilzunehmen. Diese Studie besteht aus vier Teilen. Bitte stellen Sie sicher, dass Sie ausreichend Zeit haben, um die Studie konzentriert zu bearbeiten.</p> <p>Der erste Teil beginnt gleich. Bitte versuchen Sie, diesen Teil ohne Unterbrechung zu bearbeiten. Herzlichen Dank für Ihre Zeit und Ihr Interesse an der Studie.'
    transition_title = 'Willkommen zum nächsten Teil der Studie. '
    transitions_second_1 =  'Sie haben jetzt '
    transitions_second_2 = 'von insgesamt 4 Teilen abgeschlossen. Teil'
    transitions_second_3 = 'wird gleich beginnen. Wenn Sie eine Pause benötigen, wäre jetzt eine gute Zeit dafür.'
    transitions_second_4 = 'Sobald Sie mit dem nächsten Teil beginnen, bitten wir Sie, diesen möglichst ohne Unterbrechung zu bearbeiten. Vielen Dank für Ihre Zeit. Wenn Sie bereit sind, klicken Sie auf "Weiter".'
    

    # instructions
    instructions_title = "Anweisungen zur nächsten Aufgabe"
    instructions_pa = "Im Folgenden werden wir Sie bitten, <b>die Klimafreundlichkeit verschiedener CO<sub>2</sub> -Fußabdrücke zu beurteilen</b>. <br> Das bedeutet, wir bitten Sie, Ihre beste Einschätzung <b>über die Größe des persönlichen CO<sub>2</sub> -Fußabdrucks einer Reihe von Personen mit unterschiedlichen Lebensstilen zu geben.</b> Die vorgestellten Personen werden sich hinsichtlich <b>ihrer Ernährung, ihres Pendel- und Reiseverhaltens sowie ihrer Stromversorgung und Recycling-Verhaltens</b> unterscheiden. <br> "
    instructions_pb = "Ein persönlicher CO<sub>2</sub> -Fußabdruck bezieht sich auf die Gesamtmenge an Treibhausgasen (einschließlich CO<sub>2</sub>  und Methan), die aufgrund des Verhaltens einer Person in die Atmosphäre ausgestoßen wird. <br> Der CO<sub>2</sub> -Fußabdruck umfasst somit Emissionen aus dem Fahren, Fliegen, dem Verbrauch von Strom, der Kühlung oder Heizung Ihres Zuhauses, dem Kauf von Waren und anderen Quellen. <br> Er wird in CO<sub>2</sub> -Äquivalenten gemessen, sodass andere Treibhausgase zusätzlich zu CO<sub>2</sub>  (z. B. Methan) ebenfalls einbezogen werden. <br> <br> Mit anderen Worten, <b>ein persönlicher CO<sub>2</sub> -Fußabdruck spiegelt die gesamte Auswirkung einer Person auf das Klimasystem wider</b>."
    instructions_pc = "Bitte beachten Sie, dass die individuellen CO<sub>2</sub> -Fußabdrücke, die Sie bewerten werden, <b>vereinfacht</b> sind und nur auf 6 Verhaltensweisen basieren, daher berücksichtigen sie nicht den gesamten CO<sub>2</sub> -Fußabdruck einer Person. <br> Sie werden gebeten, diese Einschätzung auf einer <b>Skala von 1 (geringer CO<sub>2</sub> -Fußabdruck) bis 10 (hoher CO<sub>2</sub> -Fußabdruck)</b> vorzunehmen. <br> Das bedeutet, Sie müssen keine konkreten Zahlen schätzen. Basierend auf den 6 Verhaltensweisen würde ein geringer CO<sub>2</sub> -Fußabdruck (für eine Person in Deutschland) etwa 0,7 Tonnen CO<sub>2</sub>  pro Jahr und ein hoher CO<sub>2</sub> -Fußabdruck etwa 5,3 Tonnen CO<sub>2</sub>  entsprechen. Auf der Skala von 1 bis 10 entspricht jeder Anstieg um 1 (z. B. von 2 auf 3 oder von 7 auf 8) einem Anstieg von etwa 500 kg CO<sub>2</sub>.  <br> "

    instructions_pd = "Als Nächstes werden Sie sehen, wie die Aufgabe aussehen wird. <br> Dann bitten wir Sie, <b>den CO<sub>2</sub> -Fußabdruck von 16 Personen mit unterschiedlichen Lebensstilen zu schätzen</b>."
    # task_example
    example_pa = 'So sieht der CO<sub>2</sub> -Fußabdruck einer Person in unserer Aufgabe aus. <br>'

    example_pb = 'Die unterschiedlichen Lebensstile dieser Personen beziehen sich auf: <ul> <li> <b>Ernährungsverhalten:</b> Die betreffende Person folgt entweder einer <b>Fleisch-basierten Ernährung </b> oder einer <b>Pflanzen-basierten Ernährung (vegetarisch)</b> </li> <li> <b>Recycling Verhalten:</b> Die betreffende Person <b>recycelt alles</b> oder <b>recycelt nicht</b> </li>  <li> <b>Regionalität der Lebensmittel:</b> Die betreffende Person kauft und konsumiert entweder <b>hauptsächlich regionale Lebensmittel </b> oder <b>auch importierte</b> Lebensmittel </li><li> <b>Stromvertrag basierend auf 7000 kWh Stromverbrauch einer Person:</b> Die betreffende Person hat entweder einen Stromvertrag abgeschlossen der <b>gemischt ist, also fossile Quellen und 40% erneuerbare Quelen beinhaltet</b> oder <b> 100% erneuerbare Quellen beinhaltet</b> </li> <li> <b>Arbeitsweg:</b> Die betreffende Person fährt jeden Tag die 20km zur und von der Arbeit, 5 Tage die Woche für 48 Wochen in Jahr <b>mit dem Fahrrad</b> oder <b>mit dem Bus</b> </li> <li> <b>Urlaubsreisen:</b> Die betreffende Person nimmt entweder <b>2 Mittelstreckenflüge pro Jahr (=3-6 Stunden)</b> oder <b>nimmt den Zug(z.B. London-Basel oder London-Amsterdam)</b> </li>'
    example_pc = ' <i>Das heißt, im obigen Beispiel ernährt sich die Person vegetarisch, recycelt nicht, isst regionale und importierte Lebensmittel, hat einen gemischten Stromvertrag abgeschlossen, pendelt jeden Wochentag mit dem Bus zur Arbeit und fährt mit dem Zug in den Urlaub.</i>  <br> '
    example_pd = 'Als Nächstes werden Sie den CO<sub>2</sub> -Fußabdruck von <b>16</b> Personen mit unterschiedlichen Lebensstilen einschätzen. <br> Bitte betrachten Sie jeden einzelnen CO<sub>2</sub> -Fußabdruck genau und nehmen Sie sich etwas Zeit, um Ihre Schätzung abzugeben. <br> Die Reihenfolge, in der die 6 Verhaltensweisen dargestellt werden, wird sich innerhalb der 16 gezeigten Beispielen, ändern.'
    example_pic = '/static/global/images/example_de.png '

    ## comprehension
    comprehension_title = ' Da Sie soeben eine Menge Informationen gelesen haben, möchten wir sicherstellen, dass Sie einen wichtigen Aspekt verstanden haben: Bitte geben Sie an, wie viel kg CO<sub>2</sub> mit jedem Anstieg um eine Einheit auf der Skala verbunden sind: '
    
    comprehension_a= ' 200 kg CO2 pro Anstieg um 1 auf der Skala'
    comprehension_b= ' 500 kg CO2 pro Anstieg um 1 auf der Skala'
    comprehension_c = ' 900 kg CO2 pro Anstieg um 1 auf der Skala'

    ## attention check study is about what screenout
    interlude_title = "Eine Zwischenfrage"
    interlude_header = "In dieser Studie gibt es ein übergeordnetes Thema. Haben Sie aufgepasst und können sagen, worum es in dieser Studie geht? Bitte seien Sie sorgfältig und wählen die richtige Antwort aus."
    aboutWhatLabel = "Worum geht es in dieser Studie?"

    about_a = "Städtetourismus"
    about_b = "Klimawandel"
    about_c = "Waschmaschinen"
    about_d = "Vorliebe für scharfes Essen"

    
    ## screenouts 
    screenout_title = "Teilnahme nicht möglich."
    screenout_sentence = "Leider deuteten Ihre Eingaben darauf hin, dass Sie nicht aufmerksam gelesen haben. Daher können Sie nicht an der Studie teilnehmen."



