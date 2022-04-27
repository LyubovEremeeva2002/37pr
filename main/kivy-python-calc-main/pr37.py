import re
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from numpy import number

#Builder.load_file("my.kv")

# Declare both screens
class CalcScreen(Screen):
    def addNumberToInput(self, button):
        if (self.ids['input'].text == "0"):
            self.ids['input'].text = '' # Убирает ничего не значащий ноль
        self.ids['input'].text += str(button.text) # Добавит число из Button.text в окно ввода

    def addCharToInput(self, button):
        textInput = self.ids['input'].text
        l = len(textInput)
        if (l > 0):
            lastChar = textInput[-1]
            thisChar = button.text
            if (lastChar not in ("-", "+", ".") or thisChar is '-' and lastChar is '+'):
                self.ids['input'].text += str(thisChar) # Добавит число из Button.text в окно ввода

    def addDotToInput(self):
        textInput = self.ids['input'].text
        l = len(textInput)
        if (l > 0):
            numbers = re.split("[+-]", textInput)
            lastChar = textInput[-1]
            if (not re.search('\.', numbers[-1]) and lastChar not in (".", "+", "-")):
                self.ids['input'].text += "."

    def getResult(self):
        textInput = self.ids['input'].text
        l = len(textInput)
        if (l > 0):
            lastChar = textInput[-1]
            if (lastChar not in ('-', '+')):
                self.ids['input'].text = str(eval(self.ids['input'].text)) # Исполняет строку и вставляет в вывод

    def getSqrt(self):
        textInput = self.ids['input'].text
        l = len(textInput)
        if (l > 0):
            if (textInput.isdigit()):
                a = int(textInput) ** 0.5
                self.ids['input'].text = str(a)

    def deleteLastFromInput(self):
        self.ids['input'].text = self.ids['input'].text[:-1]

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(CalcScreen(name='calc'))
        self.title = "Калькулятор"
        self.icon = 'image/icon.png'
        self.kv_file = 'my.kv'
        return sm

if __name__ == '__main__':
    MyApp().run()