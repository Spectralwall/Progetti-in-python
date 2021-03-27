from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

#kivy usa il file appostio .kv per la descrizione di dell'interfaccia grafica

#classe per un form di login
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):#metodo init di start
        super(LoginScreen, self).__init__(**kwargs)#viene chiamata una sovra classe
        self.cols = 4#il numero di elementi per riga
        self.add_widget(Label(text='User Name'))#aggiungo un label
        self.username = TextInput(multiline=False)#un text imput per iursername
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))#aggiungo una label
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Button(text='Loggati'))

#tendenzialmente si creano classi che poi vengono istanziate nella classe principale ovvero quella qua sotto
class TestApp(App):#difinizione nella classe base di kivy
    def build(self):#restituisce il root widget
        return LoginScreen()
        #return Button(text='Hello World')#inizializiamo il bottone e ritorniamo la sua istanza
        #in kivy i bottoni sono label a cui si associano azioni

TestApp().run()#inizialiazza la classe e la lancia