class Button(object):
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


buton_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(buton_obj.create_button(b).get_html())
