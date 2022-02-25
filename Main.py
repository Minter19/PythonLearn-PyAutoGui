from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()
        
MyApp().run()