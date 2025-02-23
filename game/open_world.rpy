# Определяем предметы как отдельные переменные
define cyper_item = {
    "position": 1,  # Используем position вместо xpos и ypos
    "idle": "cyper_item.png",
    "hover": "cyper_item_hover.png",
    "action": Call("cyper_toom_label")
}

# Словарь для хранения позиций (position: (xpos, ypos))
define positions = {
    1: (650, 160)
}

# Инициализируем места с пустыми списками предметов
define places = {
    "cyper_shtab": {
        "place_items": {}
    },
    "empty": {
        "place_items": {}
    }
}

# Добавляем предметы в места
init python:
    # Функция для добавления предмета в место
    def add_item_to_place(place_name, item_key, item, position):
        item["position"] = position
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

    # Добавляем предметы в начальные места
    add_item_to_place("cyper_shtab", "cyper", cyper_item, 1)

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
        imagebutton:
            xpos xpos
            ypos ypos
            idle item["idle"]
            hover item["hover"]
            action item["action"]

label cyper_toom_label:
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