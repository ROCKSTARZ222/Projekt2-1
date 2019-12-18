import kivy
import pyads

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


akEntre = 19.4
akKokken = 21.1
akKontor1 = 22.3
akKontor2 = 23.1
akGang = 22
akToiletter = 18


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2


        self.venstreside = GridLayout()
        self.venstreside.cols = 4

        self.venstreside.add_widget(Label(text="Rum"))
        self.venstreside.add_widget(Label(text="Setpunkt"))
        self.venstreside.add_widget(Label(text="Aktuel"))
        self.venstreside.add_widget(Label(text="Varmekilde aktiv"))



        self.venstreside.add_widget(Label(text="Entre"))
        self.tempentreSP = TextInput(multiline=False)
        self.venstreside.add_widget(self.tempentreSP)
        self.tempentre = TextInput(multiline = False, background_color = (174,169,169,1))
        self.venstreside.add_widget(self.tempentre)
        self.entrevarmekilde = Image(source='orange.png')     
        self.venstreside.add_widget(self.entrevarmekilde)


        self.venstreside.add_widget(Label(text="Koekken"))
        self.tempkokkenSP = TextInput(multiline=False)
        self.venstreside.add_widget(self.tempkokkenSP)
        self.tempkokken = TextInput(multiline=False, background_color=(174, 169, 169, 1))
        self.venstreside.add_widget(self.tempkokken)
        self.kokkenvarmekilde = Image(source='orange.png')
        self.venstreside.add_widget(self.kokkenvarmekilde)


        self.venstreside.add_widget(Label(text="Kontor1"))
        self.tempkontor1SP = TextInput(multiline=False)
        self.venstreside.add_widget(self.tempkontor1SP)
        self.tempkontor1 = TextInput(multiline = False, background_color = (174,169,169,1))
        self.venstreside.add_widget(self.tempkontor1)
        self.kontor1varmekilde = Image(source='bb.jpg')
        self.venstreside.add_widget(self.kontor1varmekilde)


        self.venstreside.add_widget(Label(text="Kontor2"))
        self.tempkontor2SP = TextInput(multiline=False)
        self.venstreside.add_widget(self.tempkontor2SP)
        self.tempkontor2 = TextInput(multiline = False, background_color = (174,169,169,1))
        self.venstreside.add_widget(self.tempkontor2)
        self.kontor2varmekilde = Image(source='bb.jpg')
        self.venstreside.add_widget(self.kontor2varmekilde)

        self.venstreside.add_widget(Label(text="Gang"))
        self.tempgangSP = TextInput(multiline=False)
        self.venstreside.add_widget(self.tempgangSP)
        self.tempgang = TextInput(multiline=False, background_color=(174, 169, 169, 1))
        self.venstreside.add_widget(self.tempgang)
        self.gangvarmekilde = Image(source='bb.jpg')
        self.venstreside.add_widget(self.gangvarmekilde)

        self.venstreside.add_widget(Label(text="Toiletter"))
        self.temptoiletterSP = TextInput(multiline=False)
        self.venstreside.add_widget(self.temptoiletterSP)
        self.temptoiletter = TextInput(multiline=False, background_color=(174, 169, 169, 1))
        self.venstreside.add_widget(self.temptoiletter)
        self.toilettervarmekilde = Image(source='orange.png')
        self.venstreside.add_widget(self.toilettervarmekilde)
        
        self.venstreside.add_widget(Label(text="StartTid: Timer"))
        self.venstreside.add_widget(Label(text="StartTid: Minutter"))
        self.venstreside.add_widget(Label(text="StopTid: Timer"))
        self.venstreside.add_widget(Label(text="StopTid: Minutter"))
        
        self.starttimer = TextInput(multiline=False)
        self.venstreside.add_widget(self.starttimer)
        self.startminutter = TextInput(multiline=False)
        self.venstreside.add_widget(self.startminutter)
        self.stoptimer = TextInput(multiline=False)
        self.venstreside.add_widget(self.stoptimer)
        self.stopminutter = TextInput(multiline=False)
        self.venstreside.add_widget(self.stopminutter)

        self.add_widget(self.venstreside)
        self.grundplan = Image(source='grundplan.png')
        self.add_widget(self.grundplan)



        self.tempentre.text = str(akEntre)
        self.tempkontor1.text = str(akKontor1)
        self.tempkontor2.text = str(akKontor2)
        self.tempkokken.text = str(akKokken)
        self.tempgang.text = str(akGang)
        self.temptoiletter.text = str(akToiletter)
        self.starttimer.text = str(6)
        self.startminutter.text = str(00)
        self.stoptimer.text = str(15)
        self.stopminutter.text = str(30)

        spEntre = self.tempentreSP
        spKokken = self.tempkokkenSP
        spKontor1 = self.tempkontor1SP
        spKontor2 = self.tempkontor2SP
        spGang = self.tempgangSP
        spToiletter = self.temptoiletterSP
        


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__=="__main__":
    MyApp().run()


