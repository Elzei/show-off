from kivy.app import App
from kivy.uix.button import Button


class DndCharacterSheetEditor(App):
    def build(self):
        return Button(text='Pointless button')


def main():
    DndCharacterSheetEditor().run()
