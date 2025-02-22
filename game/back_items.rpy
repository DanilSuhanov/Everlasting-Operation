# Словарь для хранения позиций (position: (xpos, ypos))
define positions = {
    1: (650, 160)
}

# Данные для cypeppypep_room_items
define cypeppypep_room_items = [
    {
        "position": 1,  # Используем position вместо xpos и ypos
        "idle": "cyper_item.png",
        "hover": "cyper_item_hover.png",
        "action": Call("cyper_toom_label")
    }
]

# Функция для получения xpos и ypos по position
init python:
    def get_position(item):
        position = item.get("position")
        if position in positions:
            return positions[position]
        return (0, 0)  # Возвращаем значения по умолчанию, если позиция не найдена

# Экран для отображения элементов
screen item_selection(items):
    for item in items:
        $ xpos, ypos = get_position(item)  # Получаем xpos и ypos по position
        imagebutton:
            xpos xpos
            ypos ypos
            idle item["idle"]
            hover item["hover"]
            action item["action"]

label cyper_toom_label:
    show cyper standart at cyptrans
    cyp "Рекрут, ты тут?"
    "Супер демонстративно потряс бумажкой в воздухе."
    "Этот человек будто излучал ауру безоговорочного авторитета, и его воле было невозможно противиться."
    hide cyper
    return