class Title:
    def __init__(self, text, x, y, visible=True):
        self.text = text
        self.x = x
        self.y = y
        self.visible = visible

    def print_info(self):
        visibility = "відображається" if self.visible else "приховано"
        print(f"Напис: '{self.text}', Координати: ({self.x}, {self.y}), Видимість: {visibility}")

    def hide(self):
        if self.visible:
            self.visible = False
            print(f"{self.text} - приховано")

    def show(self):
        if not self.visible:
            self.visible = True
            print(f"{self.text} - відображається")

# Створюємо два написи
title1 = Title("Дізнатися переможця прямо зараз!", 150, 50)
title2 = Title("Переможець може бути тільки один", 150, -100)

# Друкуємо інформацію про написи
title1.print_info()
title2.print_info()

# Приховуємо другий напис
title2.hide()

# Друкуємо інформацію про написи після приховування
title1.print_info()
title2.print_info()
