# Imports
import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        # columns
        self.cols = 2
        
        # all widgets
        self.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False) # how many lines it take up
        self.add_widget(self.name)

        self.add_widget(Label(text = "Age : "))
        self.age = TextInput(multiline = False) # how many lines it take up
        self.add_widget(self.age)

        self.add_widget(Label(text = "Favourite color : "))
        self.color = TextInput(multiline = False) # how many lines it take up
        self.add_widget(self.color)

        self.submit = Button(text = "Submit", font_size = 32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self,instance):
        name = self.name.text
        age = self.age.text
        color = self.color.text
        self.add_widget(Label(text = f"Name : {name} \nAge : {age} \nFavourite color : {color}"))
        self.name.text = ""
        self.age.text = ""
        self.color.text = ""



class MyApp(App):
    def build(self):
        # Label
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()

