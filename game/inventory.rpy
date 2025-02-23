default player_inventory = []

define items_data = {
    "anketa": {
        "name": "Анкета Battle Brothers", 
        "image": "anketa.png",
        "image_hover": "anketa_hover.png",
        "description": "Анкета для вступления в клан Battle Brothers. Мне нужно её заполнить чтобы вступить в клан...",
        "state": "empty"
    }
}

init python:
    def hide_interact():
        renpy.hide_screen("inventory_screen")
        renpy.hide_screen("item_tooltip")
    
    def changeItemState(item_id, state):
        items_data[item_id]["state"] = state
    
    def handle_item(item_id):
        _item = items_data[item_id]

        if item_id == "anketa":
            if _item["state"] == "empty":
                changeItemState(item_id, "process")
                hide_interact()
                renpy.jump("anketa")
            else:
                renpy.notify("Вы уже заполняете анкету...")
        else:
            renpy.notify("Этот предмет не имеет действий в текущем контексте.")
    
    def add_item(item_id):
        if item_id not in player_inventory:
            player_inventory.append(item_id)
            renpy.notify(f"Добавлен предмет: {items_data[item_id]['name']}")
        else:
            renpy.notify(f"Предмет {items_data[item_id]['name']} уже в инвентаре.")

    def remove_item(item_id):
        if item_id in player_inventory:
            player_inventory.remove(item_id)
            renpy.notify(f"Удален предмет: {items_data[item_id]['name']}")
        else:
            renpy.notify(f"Предмет {items_data[item_id]['name']} не найден.")

screen inventory_screen():
    modal True  # Делаем экран модальным
    frame:
        xfill True
        yfill True
        background "#1E1E2E"  # Тёмный фон
        padding (20, 20)

        imagebutton:
            xalign 1.0
            yalign 0.0
            idle "close_button.png"
            hover "close_button.png"
            action Hide("inventory_screen")  # Закрываем инвентарь

        text "Инвентарь":
            size 50 
            xalign 0.5 
            yalign 0.1
            color "#89B4FA"  # Голубой цвет для заголовка
            font "DejaVuSans-Bold.ttf"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 50
            for item_id in player_inventory:
                $ item = items_data[item_id]
                vbox:
                    imagebutton:
                        xalign 0.5
                        idle item["image"]
                        hover item["image_hover"]
                        action Function(handle_item, item_id)  # Вызов функции handle_item
                        hovered Show("item_tooltip", item=item)
                        unhovered Hide("item_tooltip")
                    text item["name"]: 
                        size 30 
                        xalign 0.5
                        color "#FFFFFF"

screen item_tooltip(item):
    frame:
        xpos renpy.get_mouse_pos()[0] + 20
        ypos renpy.get_mouse_pos()[1] + 20
        padding (10, 10)
        background "#000000"
        vbox:
            text item["name"] size 25 color "#FFFFFF"
            text item["description"] size 20 color "#FFFFFF"

screen inventory_show():
    imagebutton:
        xalign 0.99
        yalign 0.01
        idle "inventory_button.png"
        hover "inventory_button_hover.png"
        action Show("inventory_screen")