from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

def on_button_press():
    print('boton presionado')

class ScrButton(Button):
    def __init__(self, screen, goal= 'main',  direction='left', **kwargs):
        super().__init__(**kwargs)
        self.goal = goal
        self.direction = direction
        self.cscreen = screen
    def on_press(self):
        self.cscreen.manager.transition.direction = self.direction
        self.cscreen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwards):
        super().__init__(**kwards)
        box1 = BoxLayout()
        box2 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box1.add_widget(Label(text='Elije un boton'))
        btn1 = ScrButton(screen=self, goal='first', direction='up', text='1')
        btn2 = ScrButton(screen=self, goal='second', direction='left', text='2')
        btn3 = ScrButton(screen=self, goal='third', direction='down', text='3')
        btn4 = ScrButton(screen=self, goal='fourth', direction='right', text='4')
        box2.add_widget(btn1)
        box2.add_widget(btn2)
        box2.add_widget(btn3)   
        box2.add_widget(btn4)
        box1.add_widget(box2)
        self.add_widget(box1)


class Pantalla1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        bton1 = Button(text='Eleccion 1', size_hint=(0.5, 1), pos_hint={'left':0 })
        bton2 = ScrButton(screen=self, goal='main', direction='down', text='Eleccion 2', size_hint=(0.5, 1), pos_hint={'right':0 })
        layout.add_widget(bton1)
        layout.add_widget(bton2)
        self.add_widget(layout)

class second(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Regresar')
        btn1.on_press = self.next_screen
        self.add_widget(btn1)
    def next_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Pantalla1(), name='first')
        sm.add_widget(second(), name='second')
        sm.add_widget(MainScreen(name='main')) 
        sm.current = 'main'
        return sm


app = MyApp()
app.run()
