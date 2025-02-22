default player_name = "Рекрут"  # Ник игрока

default player_money = 0  # Баланс денег

default player_skills = {
    "strength": 0,  # Сила
    "agility": 0,   # Ловкость
    "luck": 0,      # Удача
    "intellect": 0, # Интеллект
    "charisma": 0   # Харизма
}

screen player_profile():
    modal True  # Делаем экран модальным
    zorder 100  # Убедимся, что экран поверх других элементов

    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        background "#1E1E2E"  # Тёмный фон
        vbox:
            spacing 15

            # Заголовок
            text "Профиль игрока":
                size 40
                color "#89B4FA"  # Голубой цвет для заголовка
                font "DejaVuSans-Bold.ttf"
                xalign 0.5

            # Ник игрока
            text "Ник: [player_name]":
                size 30
                color "#FFFFFF"  # Белый цвет для текста
                font "DejaVuSans.ttf"

            # Баланс денег
            text "Баланс: [player_money] $":
                size 30
                color "#FFFFFF"
                font "DejaVuSans.ttf"

            # Навыки
            text "Навыки:":
                size 30
                color "#89B4FA"  # Голубой цвет для заголовка
                font "DejaVuSans-Bold.ttf"

            hbox:
                spacing 30
                vbox:
                    text "Сила: [player_skills[strength]]":
                        size 25
                        color "#FFFFFF"
                        font "DejaVuSans.ttf"
                    text "Ловкость: [player_skills[agility]]":
                        size 25
                        color "#FFFFFF"
                        font "DejaVuSans.ttf"
                    text "Удача: [player_skills[luck]]":
                        size 25
                        color "#FFFFFF"
                        font "DejaVuSans.ttf"
                vbox:
                    text "Интеллект: [player_skills[intellect]]":
                        size 25
                        color "#FFFFFF"
                        font "DejaVuSans.ttf"
                    text "Харизма: [player_skills[charisma]]":
                        size 25
                        color "#FFFFFF"
                        font "DejaVuSans.ttf"

            # Кнопка закрытия
            textbutton "Закрыть":
                xalign 0.5
                background "#89B4FA"  # Голубой фон кнопки
                hover_background "#A6D5FA"  # Светло-голубой при наведении
                text_color "#1E1E2E"  # Тёмный текст
                text_hover_color "#1E1E2E"  # Тёмный текст при наведении
                action Hide("player_profile")  # Закрываем экран

screen profile_show():
    imagebutton:
        xalign 0.01
        yalign 0.01
        idle "profile_button.png"  # Изображение кнопки
        hover "profile_button_hover.png"  # Изображение при наведении
        action Show("player_profile")  # Открываем экран профиля