﻿define rek = Character('Рекрут', color="#1890FF")
define cyp = Character('cypeppypep', color='#E52B50')
define anc = Character('Анкета', color='#CD9575', what_color='#1E1112', kind=nvl)
define anon_ant = Character('?', color='#AF2B1E')
define pod = Character('Подводный', color='#531A50')
define anon_pod = Character('?', kind=pod)

screen stats():
    style_prefix "metal"
    frame:
        xalign 1 ypos 50
        vbox:
            text "Сила - [power]"
            text "Ловкость - [agility]"
            text "Удача - [fortune]"
            text "Выносливость - [endurance]"
            text "Скрытность - [stealth]"
            text "Интеллект - [intellect]"
            text "Харизма - [charisma]"
            textbutton "Закрыть статы":
                action Hide("stats")

screen open_stats():
    style_prefix "metal"
    frame:
        xalign 1 ypos 50
        textbutton "Открыть статы":
             action Show("stats")
 

style metal_frame:
    background "#434B4D"

style metal_text:
    color "#F5E6CB"

transform cyptrans:
    xalign 0.5
    yalign 0.5


label start:

    $ power = 0
    $ agility = 0
    $ fortune = 0
    $ endurance = 0
    $ stealth = 0
    $ intellect = 0
    $ charisma = 0

    scene bg shtab
    with Dissolve(.5)

    "Передо мной предстала массивная обитая кожей дверь."

    "Табличка, не такая обветшалая, как все вокруг, гласила: 'Комиссар Cypeppepep'."

    rek "Ну, вроде сюда…"

    "Дверь открылась на удивление легко. В кабинете было значительно темнее, чем снаружи, и мне показалось, будто я прервал некое таинство."

    show cyper standart at cyptrans
    with Dissolve(.5)

    "В дальнем конце комнаты за резным столом сидел человек. Он сделал едва заметное движение головой."

    "И хотя его лицо полностью закрывала маска, я был уверен, что он буквально пожирает меня глазами."

    "Несложно было догадаться, что это и есть тот самый cypeppypep."

    cyp "Садись."

    "Перед столом стоял самый обычный деревянный стул."

    "Я сел и окинул взглядом рабочее место комиссара."

    "Стол был чистым, а все бумаги были аккуратно разложены по стопкам: либо он очень аккуратный человек, либо просто нихуя не делает."

    rek "Здравствуйте."

    cyp "Ну здравствуй."

    "Супер открыл один из ящиков стола и достал оттуда какую-то бумажку."

    cyp "Заполни"

    "Он говорил очень спокойно, и в нем не было ни нотки агрессии, но это ничуть не успокаивало. Скорее наоборот: я не знал, что от него ожидать."

    "Да еще и эта маска…"

    "Вдруг он какой-нибудь псих? Война же меняет людей."

    "На секунду я усомнился в своем решении вступить в бб."

    cyp "Рекрут, ты тут?"

    "Супер демонстративно потряс бумажкой в воздухе."

    "Этот человек будто излучал ауру безоговорочного авторитета, и его воле было невозможно противиться."

    "Я взял лист в руки. “Анкета для вступления в Battle Brothers”. Комиссар протянул мне ручку."

    show screen open_stats

    rek "Ну что ж."

    hide cyper standart
    with Dissolve(0.5)

    "Я взял ручку и принялся изучать анкету: надо же хотя бы знать, на что подписываюсь."

    "Анкета оказалось довольно маленькой, размером примерно с половину тетрадного листка."

    python:
        name = renpy.input("Первым делом от меня требуется указать имя.")

        name = name.strip() or "Рекрут"
    
    "Далее шел какой-то текст. “Подписывая данную анкету, я соглашаюсь с тем, что у меня нет личной жизни и/или я готов полностью отказаться от нее и посвятить всего себя Battle Brothers”..."

    "Без тени сомнения я поставил подпись и положил бумажку на стол. Супер взглянул на нее и поставил печать."
    
    cyp "Очень хорошо. Теперь заполни вот это."

    "Он протянул еще одну бумажку, на этот раз побольше. Я прочитал заголовок. “Тест на профпригодность”."

    "Только я хотел начать отвечать на вопросы этого теста, как услышал из коридора приглушенные голоса."

    anon_pod "Короче, я подумал и решил, что я там должен быть.  Но прописывать сам себя не собираюсь, а то кринж получится."

    anon_pod "Надеюсь, никто не будет против?"

    anon_ant "Соси попу."

    anon_pod "Понятно… Надеюсь, ты хотя бы догадаешься вырезать этот диалог, если не захочешь его добавлять."

    "Шаги удалялись. Их разговор меня озадачил. И что за этот диалог, о котором они говорили?"

    cyp "Не отвлекайся."

    "Тон его голоса не изменился, но я готов был поклясться, что он был недоволен."

    "Мой взгляд упал на бумажку с тестом у меня в руках. Я принялся отвечать на вопросы."

    menu:

        anc "Ситуация: в части вы случайно услышали разговор двух человек. Они весьма нелестно отзывались о нашем комиссаре. Ваши действия?"

        "Набил бы им обоим морды за такие слова!":
            $ power += 1
            $ endurance += 1
        
        "Подкрался бы поближе и постарался записать все, что они говорят.":
            $ agility += 1
            $ stealth += 1
        
        "Доходчиво объяснил бы им, что они неправы и какое наказание ждет их за такие слова.":
            $ intellect += 1
            $ charisma += 1

    nvl clear
    
    menu:

        anc "Как бы то ни было, эти двое разбили вам лицо, а также поломали парочку костей. Вы попали в госпиталь, но вот беда: про вас забыли и не приносят еду! Ваши действия?"

        "Превозмогая боль, сам пополз бы в столовую, как настоящий варден!":
            $ power += 1
            $ endurance += 1
        
        "Скрытно заполз бы в соседнюю палату и стащил бы еду оттуда.":
            $ agility += 1
            $ stealth += 1
        
        "Шантажировал бы своего соседа чтобы тот приносил мне еду.":
            $ intellect += 1
            $ charisma += 1

    nvl clear

    menu:

        anc "Вы не умерли с голоду в госпитале, быстро пошли на поправку и вскоре оказались на сборе. Более того, вы пришли раньше всех, и офицер поинтересовался, чем бы вы хотели заняться! Что же вы ответите?"

        "Я хочу сражаться вместе со всеми на фронте!":
            $ power += 1
            $ endurance += 1
        
        "Я хочу партизанить в тылу!":
            $ agility += 1
            $ stealth += 1
        
        "Я убиваю офицера и командую сбором сам!":
            $ intellect += 1
            $ charisma += 1

    nvl clear

    menu:

        anc "Вы видите как ваш соклановец истекает кровью на линии фронта, ваши действия?"
        
        "Возьму винтовку и буду отстреливаться от врагов, защищая раненного.":
            $ agility += 1
            $ power += 1

        "Окажу первую медицинскую помощь и оттащу раненного в тыл.":
            $ endurance += 1
            $ intellect += 1
        
        "Позову на помощь товарищей":
            $ charisma += 1
            $ intellect += 1

    nvl hide

    scene bg load
    with Dissolve(.5)

    scene bg shtab
    with Dissolve(.5)

    show cyper standart at cyptrans
    with Dissolve(.5)

    "Я заполнил бумажку и отдал Суперу. Тот принялся внимательно изучать ее, попутно делая записи в каком-то документе."

    "Наступила тишина."

    "От нечего делать я начал осматривать внутреннее убранство кабинета: шкафы, заполненные разными книгами и папками, огромную потрепанную временем карту, висевшую за спиной Супера и занимавшую бо́льшую часть стены, его кожаное кресло, стол, лампа…"

    "Я обратил внимание на модель канонерки, стоявшую на краю стола. Не подумал бы, что наш комиссар увлекается кораблями."

    "Хотя, сама модель казалась гораздо более пыльной, чем любой другой предмет в комнате. Может, недавно этот кабинет занимал кто-то другой?"

    show cyper happy at cyptrans

    cyp "Все готово."

    "Я оторвал взгляд от канонерки и не поверил своим глазам. Маска Супера… менялась? Я пришел в ступор, все тело сковал страх, а голову заполонили мысли."

    "Маска ли это, или его настоящее лицо?  Все ли в BB такие? Или только комиссары? И вообще, если Супер на этом посту относительно недавно, то какой псих был до него?"

    "Супер заметил мой страх, и его улыбка как будто стала еще шире."

    cyp "Добро пожаловать в Battle Brothers, [name]. Ты cделал правильный выбор. Поверь, будет весело."

    "На удивление его слова не звучали как-то угрожающе. Он не излучал ни злобы, ни недовольства. Мне хотелось бы верить своему комиссару, но где-то в глубине души я понимал, что я совершил ужасную ошибку…"

    "Продолжение следует..."


    return