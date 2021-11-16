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
                id: col
                spacing: "56dp"
                size_hint: 0.7,0.7
                pos_hint: {"center_x": 0.5, "center_y": 0.55}
                cols: 1
                
                MDGridLayout:
                    id: row_setting
                    spacing: "56dp"
                    rows: 1 
                        
                    MDLabel:
                        text: "Сеттинг"
                        halign: "center"

                    MDBoxLayout:
                        id: box_drop_item_setting
                        size_hint_x: 0.9
                        
                        MDDropDownItem:
                            id: drop_item_setting
                            text: '- - -'
                            halign: "center"
                            on_release: app.menu_setting.open()
                    
                MDGridLayout:
                    id: row_locations
                    spacing: "56dp"
                    rows: 1
                    
                    MDLabel:
                        text: "Локация"
                        halign: "center"
                    
                    MDBoxLayout:
                        id: box_drop_item_setting
                        size_hint_x: 0.9
                        size_hint_y: 1
                        
                        MDDropDownItem:
                            id: drop_item_location
                            text: "- - -"
                            on_release: app.menu_location.open()
                    
                MDGridLayout:
                    id: row_mobs
                    spacing: "56dp"
                    rows: 1

                    MDTextField:
                        hint_text: "Неигровые персонажи"
                        helper_text: "Введите неигровых персонажей через запятую"
                        helper_text_mode: "on_focus"
                    
                    
                MDGridLayout:
                    id: row_items
                    spacing: "56dp"
                    rows: 1

                    MDTextField:
                        hint_text: "Ключевые предметы"
                        helper_text: "Введите ключевые передметы через запятую"
                        helper_text_mode: "on_focus"
            
            
            MDBoxLayout:
                id: box_screen1_button
                spacing: "56dp"
                adaptive_size: True
                pos_hint: {"center_x": 0.5, "center_y": 0.1}
                
                

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Описание'
            icon: 'message-outline'
            badge_icon: "numeric-5"

            ScrollView:
                do_scroll_x: False
                
                GridLayout:
                    cols: 1
                    padding: dp(5)
                    size_hint_y: None
                    height: self.minimum_height
                    
                    MDLabel:
                        id: exposition
                        text: 'Здесь пока ничего нет'
                        size_hint_y: None
                        valign: 'top'
                        height: self.texture_size[1]
                        text_size: self.width - dp(10), None          
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

    def change_text(self, new_text):
        """Меняет текст в вкладке описание"""
        self.screen.ids.exposition.text = new_text

    def set_item_setting(self, text_item):
        """Устанавливает выбранное пользователем объект"""
        self.screen.ids.drop_item_setting.set_item(text_item)
        self.menu_setting.dismiss()

    def set_item_location(self, text_item):
        """Устанавливает выбранное пользователем объект"""
        self.screen.ids.drop_item_location.set_item(text_item)
        self.menu_location.dismiss()

    def button_press(self, event):
        self.screen.ids.exposition.text += "PRESSED!!\n"*10



    def build(self):
        return self.screen

    def on_start(self):
        self.root.ids.box_screen1_button.add_widget(
            MDFillRoundFlatButton(
                text= 'Генерация',
                font_size= 30,
                md_bg_color= get_color_from_hex("#C0C0C0"),
                on_release= self.button_press,
            )
        )


if __name__ == "__main__":
    MainApp().run()