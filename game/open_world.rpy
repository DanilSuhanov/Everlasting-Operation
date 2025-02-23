style exit_button_style:
    outlines [ (2, "#000000", 0, 0) ]
    hover_outlines [ (2, "#000000", 0, 0) ]
    xmargin 5
    ymargin 5
    xpadding 20
    ypadding 10

define exit_buttom = {
    "position": 2,
    "text": "Выход",
    "action": ""
}


define cyper_item = {
    "position": 1,
    "idle": "cyper/item/cyper_item.png",
    "hover": "cyper/item/cyper_item_hover.png",
    "action": Call("cyper_start_scene")
}

define vhod_v_stab = {
    "position": 3,
    "idle": "bg/item/vhod_v_shtab_item.png",
    "hover": "bg/item/vhod_v_shtab_item_hover.png",
    "action": Call("stab_open_world")
}

# Словарь для хранения позиций (position: (xpos, ypos))
define positions = {
    1: (650, 160), # Супер в кабинете
    2: (200, 10), # Кнопка выхода
    3: (830, 735) # Расположение двери
}

# Инициализируем места с пустыми списками предметов
define places = {
    "cyper_shtab": {
        "place_items": {}
    },
    "out_shtab": {
        "place_items": {}
    },
    "empty": {
        "place_items": {}
    }
}

# Добавляем предметы в места
init python:
    # Функция для добавления предмета в место
    def add_item_to_place(place_name, item_key, item):
        if item_key not in places[place_name]["place_items"]:
            places[place_name]["place_items"][item_key] = item

    # Функция для удаления предмета из места
    def remove_item_from_place(place_name, item_key):
        if item_key in places[place_name]["place_items"]:
            del places[place_name]["place_items"][item_key]

    # Функция для перемещения предмета между местами
    def move_item_between_places(from_place, to_place, item_key):
        if item_key in places[from_place]["place_items"]:
            item = places[from_place]["place_items"][item_key]
            remove_item_from_place(from_place, item_key)
            add_item_to_place(to_place, item_key, item)
    
    def getExitButton(action):
        exit_buttom["action"] = action
        return exit_buttom

    # Добавляем предметы в начальные места
    add_item_to_place("cyper_shtab", "cyper", cyper_item)

# Функция для получения xpos и ypos по position
init python:
    def get_position(item):
        position = item.get("position")
        if position in positions:
            return positions[position]
        return (0, 0)  # Возвращаем значения по умолчанию, если позиция не найдена

# Экран для отображения элементов
screen world_screen(place_name):
    for item_key, item in places[place_name]["place_items"].items():
        $ xpos, ypos = get_position(item)  # Получаем xpos и ypos по position
        if "idle" in item:
            imagebutton:
                xpos xpos
                ypos ypos
                idle item["idle"]
                hover item["hover"]
                action item["action"]
        else:
            textbutton item["text"]:
                xpos xpos
                ypos ypos
                xpadding 20
                ypadding 10
                text_color "#FFFFFF"
                text_hover_color "#FFFFFF"
                background "#1E3A8A"
                hover_background "#3B82F6"
                style "exit_button_style"
                action item["action"]

label cyper_start_scene:
    if "call_count" not in places["cyper_shtab"]:
        $ places["cyper_shtab"]["call_count"] = 0
    
    if places["cyper_shtab"]["call_count"] < 2:
        show cyper standart at cyptrans
        cyp "Рекрут, ты тут?"
        "Супер демонстративно потряс бумажкой в воздухе."
        "Этот человек будто излучал ауру безоговорочного авторитета, и его воле было невозможно противиться."
    elif places["cyper_shtab"]["call_count"] < 4:
        show cyper standart at cyptrans
        cyp "Долго ты ещё собираешься смотреть на меня?"
    else:
        show cyper standart at cyptrans
        cyp "..."
        $ remove_item_from_place("cyper_shtab", "cyper")

    hide cyper
    $ places["cyper_shtab"]["call_count"] += 1
    call screen world_screen("cyper_shtab")

label cyper_after_anket:
    "Наверное, мне стоит выйти"
    call screen world_screen("cyper_shtab")