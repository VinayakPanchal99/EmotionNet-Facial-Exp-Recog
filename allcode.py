import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
# to use buttons:
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import report
import autoreport
import detect_expression 
import time
import os
from kivy.config import Config
Config.set('graphics','resizable',0)

class ConnectPage(MDFloatLayout):
    username = None
    useremail = None
    # runs on initialization
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source ='background.jpg', allow_stretch = True,  keep_ratio = False))

        self.k = MDCard(orientation = 'vertical',size_hint = (None,None),
        size = (500,550),
        pos_hint = {"center_x":.5,"center_y":.5},
        elevation = 15,
        padding = 50,
        spacing = 30) # widget #1, top left
        self.add_widget(self.k)
        self.k.add_widget(MDLabel( text = "Sentiment Analyzer!", font_style = "H3",
            halign = "center",
            size_hint_y = None,
            padding=[0,20]))
        self.name = MDTextField(hint_text= "name", mode = 'round',
            size_hint_x = None,
            icon_right = "account",
            width = 400,
            font_size = 20,
            pos_hint = {"center_x":.5,"center_y":.5},
            fill_color_normal =[35/255,49/255,48/255,1],
            active_line = [1,1,1,1])
        self.k.add_widget(self.name)
        self.email = MDTextField(hint_text= "e-mail", mode = 'round',
            size_hint_x = None,
            icon_right = "account",
            width = 400,
            font_size = 20,
            pos_hint = {"center_x":.5,"center_y":.5},
            fill_color_normal =[35/255,49/255,48/255,1],
            active_line = [1,1,1,1])
        self.k.add_widget(self.email)
        self.submit = MDRoundFlatIconButton(text = "SIGN-UP",
                icon = "arrow-right-circle",
                font_size = 20,
                pos_hint= {"center_x":0.5, "center_y":0.5},
                 )
        self.submit.bind(on_press = self.login)
        self.k.add_widget(self.submit)
        self.clear = MDRoundFlatIconButton(text = "CLEAR",
                icon = "close-circle",
                font_size = 20,
                pos_hint= {"center_x":0.5, "center_y":0.5},
                 )
        self.clear.bind(on_press = self.clean)
        self.k.add_widget(self.clear)

    def login(self, *args):
        ConnectPage.username = self.name.text
        ConnectPage.useremail = self.email.text
        chat_app.screen_manager.current = 'Info'
        print(ConnectPage.useremail,ConnectPage.username)
    def clean(self, instance):
        self.name.text = ''
        self.email.text = ''

class InfoPage(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        #self.add_widget(Image(source ='background2.jpg', allow_stretch = True,  keep_ratio = False)) 
        
        self.add_widget(MDLabel( text = "HELLO BUDDY! We'll be there for you in good times and bad, so stay cool and don't let your emotions overpower your intellect. Select one of two capture modes:",
            halign = "center",
            size_hint_y = None,
            padding =[0,10]))
    
        
        self.newgrid = MDBoxLayout(spacing= 100, padding = 20, size_hint = (.2, .2))
        self.Mcap = MDRoundFlatIconButton(text = "Manual Capture",
                icon = "alpha-m-circle",
                font_size = 20,
                padding =[50,0]
                 )
        self.Mcap.bind(on_press = self.take_picture)
        self.newgrid.add_widget(self.Mcap)
        self.Acap = MDRoundFlatIconButton(text = "Auto Capture",
                icon = "alpha-a-circle",
                font_size = 20,
                padding =[50,0]
                 )
        self.Acap.bind(on_press = self.autcap)
        self.newgrid.add_widget(self.Acap)

        self.back = MDRoundFlatIconButton(text = "Back",
                icon = "arrow-left-circle",
                font_size = 20,
                padding =[50,0]
                 )
        self.back.bind(on_press = self.prepg)
        self.newgrid.add_widget(self.back)
        self.add_widget(self.newgrid)
        
        self.image = Image()
        self.add_widget(self.image)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video,1.0/30.0)
    def load_video(self,*args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame,0).tobytes()
        texture= Texture.create(size=(frame.shape[1], frame.shape[0]),colorfmt = 'rgba')
        texture.blit_buffer(buffer, colorfmt = 'bgr', bufferfmt = 'ubyte')
        self.image.texture = texture
    
    def take_picture(self,*args):
        image_name = 'pic.png'
        cv2.imwrite(image_name,self.image_frame)
        detexp = detect_expression.detect_expression()
        labl = detexp.manual_capture(image_name)
        rep = report.Report()
        rep.mainpage(labl, ConnectPage.username)

    def take_picture2(self,*args):
        image_name = 'pic.png'
        cv2.imwrite(image_name,self.image_frame)
        


    def autcap(self,instance):
        path = "C:/Users/vinay/Desktop/waterloo_courses/kivygui/images" # folder to save images
        time_interval = 2
        count = 0
        emofiles = []
        emos = []
        start_time = time.time()
        while count < 10:
            ret, frame = self.capture.read()

            # If the user presses 'q', exit the loop
            if cv2.waitKey(1) == ord('q'):
                break
    
            elapsed_time = time.time() - start_time
            if elapsed_time > time_interval:
                filename = f'image_{count}.jpg'
                emofiles.append(filename)
                cv2.imwrite(os.path.join(path,filename), frame)
                count += 1
                start_time = time.time()
        for i in emofiles:
            detexp1 = detect_expression.detect_expression()
            labl1 = detexp1.manual_capture(os.path.join(path,i))
            emos.append(labl1)
        autoreport.content(emos,ConnectPage.username)

    def prepg(self,instance):
        chat_app.screen_manager.current = 'Connect'


class EpicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)


        return self.screen_manager


if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()