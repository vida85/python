from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.animation import Animation
import json
import os
from time import strftime
import smtplib



class ScreenGenerator(ScreenManager):
    pass



class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.ids.menu_date.text = strftime('[size=24][b]%A[/b][/size], %B %Y')



class Trackers(Screen):
    storage = {}
    path = ''
    email = {'kevin': 'Klhyer@gmail.com',
        'davi': 'vidasilveira85@gmail.com'}

    def on_pre_enter(self):
        self.path = App.get_running_app().user_data_dir + '/'
        self.loadData()
        for tracker, num in self.storage.items():
            self.ids.track.add_widget(Tracker(text=tracker, number=num, data=self.storage))


    def saveData(self, *args):
        with open(self.path + 'data.json', 'w') as data:
            json.dump(self.storage, data)


    def loadData(self, *args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.storage = json.load(data)
        except FileNotFoundError:
            pass


    def addWidget(self):
        text_input = self.ids.text_input.text
        num = '0'
        if text_input not in self.storage.keys():
            self.ids.track.add_widget(Tracker(text=text_input, number=num, data=self.storage))
            self.storage[text_input] = '0'
            self.ids.text_input.text = ''
            self.saveData()


    def delete_storage(self, tracker):
        tracking = tracker.ids.label.text
        self.ids.track.remove_widget(tracker)
        del self.storage[tracking]
        self.saveData()


#### Add numebers and Subtract numbers from labels, Function ####
    def add_num(self, tracker):
        tracker.ids.count_add.text = str(int(tracker.ids.count_add.text) + 1)
        self.storage[tracker.ids.label.text] = str(int(tracker.ids.count_add.text))
        self.saveData()

    def subtract_num(self, tracker):
        tracker.ids.count_add.text = str(int(tracker.ids.count_add.text) - 1)
        self.storage[tracker.ids.label.text] = str(int(tracker.ids.count_add.text))
        self.saveData()

    def send(self):
        os.chdir(r'C:\Users\vida\Desktop\PESS')
        with open('bat', 'r') as bat:
            login = bat.read()
            me = self.email['davi']
            recipient = self.email['kevin']
            message = "Daily Tracking Report\n"

            for tracker, numbers in self.storage.items():
                message += f"{numbers} ---> {tracker}\n"

            #  setup email login/send msg
            smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login(me, login)
            smtp_obj.sendmail(me, recipient, message) #  send email
            smtp_obj.quit()
            print("...Email Sending...")




class Tracker(BoxLayout):
    def __init__(self, text='', number='', data={}, **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
        self.ids.count_add.text = number



class Pess(App):
    
    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '800')
        from kivy.core.window import Window
        Window.clearcolor = get_color_from_hex('#262829')

        return ScreenGenerator()


if __name__ == '__main__':
    Pess().run()
