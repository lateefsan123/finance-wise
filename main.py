from kivy import resources
from kivy.app import App
from kivy.core.window import Window

import libs.uix.components  # first every initialize widgets
from libs.applibs import utils
from libs.applibs.config import config
from libs.applibs.core.theming import ThemeManager
from libs.applibs.state import StateProvider
from libs.uix.root import Root

resources.resource_add_path(utils.abs_path("assets", "images"))


if not utils.is_android():
    Window.size = (350, 650)


class MainApp(App):
    theme_cls = ThemeManager()
    state = StateProvider()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Finance Tracker"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()

        refresh_token = config.refresh_token

        if refresh_token:
            self.root.set_current("loading")
        else:
            self.root.set_current("onboarding")

    def on_start(self):
        if utils.is_android():
            from android.permissions import Permission, request_permissions

            request_permissions(
                [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE]
            )


if __name__ == "__main__":
    MainApp().run()
