define cypeppypep_room_items = [
    {
        "xpos": 100,
        "ypos": 200,
        "idle": "item1.png",
        "hover": "item1_hover.png",
        "action": Call("item1_selected")
    }
]

label item1_selected:
    "Вы выбрали первый предмет."
    return

screen item_selection(items):
    for item in items:
        imagebutton:
            xpos item["xpos"]
            ypos item["ypos"]
            idle item["idle"]
            hover item["hover"]
            action item["action"]