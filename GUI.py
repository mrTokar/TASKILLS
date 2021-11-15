from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu

from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from kivy.properties import StringProperty

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex


MDScreen:

    MDBottomNavigation:
        panel_color: get_color_from_hex("#eeeaea")
        selected_color_background: get_color_from_hex("#97ecf8")
        text_color_active: 0, 0, 0, 1
        
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Генерация'
            icon: 'wrench-outline'
            badge_icon: "numeric-10"
            
            MDGridLayout:
                id: box_screen1_up
                spacing: "56dp"
                size_hint: 0.5,0.5
                pos_hint: {"center_x": 0.5, "center_y": 0.7}
                cols: 1
                
                MDDropDownItem:
                    id: drop_item_setting
                    text: 'Сеттинг'
                    on_release: app.menu_setting.open()
                    
                MDDropDownItem:
                    id: drop_item_location
                    text: "Локация"
                    on_release: app.menu_location.open()
                    
                MDTextField:
                    hint_text: "Неигровые персонажи"
                    helper_text: "Введите неигровых персонажей через запятую"
                    helper_text_mode: "on_focus"
                
                MDTextField:
                    hint_text: "Ключевые предметы"
                    helper_text: "Введите ключевые передметы через запятую"
                    helper_text_mode: "on_focus"
            
            
            MDBoxLayout:
                id: box_screen1_button
                spacing: "56dp"
                adaptive_size: True
                pos_hint: {"center_x": 0.5, "center_y": 0.15}
                
                

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Описание'
            icon: 'message-outline'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Описание'
                halign: 'center'
        
'''


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": name,
                "height": dp(56),
                "on_release": lambda x=name: self.set_item_setting(x),
            } for name in ["Забытые королевства", "EBERRON"]
        ]
        self.menu_setting = MDDropdownMenu(
            caller=self.screen.ids.drop_item_setting,
            items=menu_items,
            width_mult=4,
        )
        self.menu_setting.bind()

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": name,
                "height": dp(56),
                "on_release": lambda x=name: self.set_item_location(x),
            } for name in ["Рашута", "Замаок"]
        ]
        self.menu_location = MDDropdownMenu(
            caller=self.screen.ids.drop_item_location,
            items=menu_items,
            width_mult=4,
        )
        self.menu_location.bind()


    def set_item_setting(self, text_item):
        self.screen.ids.drop_item_setting.set_item(text_item)
        self.menu_setting.dismiss()

    def set_item_location(self, text_item):
        self.screen.ids.drop_item_location.set_item(text_item)
        self.menu_location.dismiss()


    def build(self):
        return self.screen

    def on_start(self):
        self.root.ids.box_screen1_button.add_widget(
            MDFillRoundFlatButton(
                text= 'Генерация',
                font_size= 30,
                md_bg_color= get_color_from_hex("#C0C0C0"),
            )
        )


if __name__ == "__main__":
    MainApp().run()