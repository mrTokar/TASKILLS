from kivymd.app import MDApp
from kivy.lang import Builder

bottom_navigation = '''
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

            MDLabel:
                text: 'Генреация'
                halign: 'center'

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

    def build(self):
        return Builder.load_string(bottom_navigation)


if __name__ == "__main__":
    MainApp().run()