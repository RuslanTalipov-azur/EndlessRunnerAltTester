from pages.base_page import BasePage
from alttester import By


class MainMenuPopup(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def mission_popup(self):
        return  self.altdriver.wait_for_object(By.NAME, 'MissionPopup', timeout=2)

    @property
    def mission_close_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'MissionPopup/MissionBackground/CloseButton', timeout=2)

    @property
    def setting_popup(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingPopup', timeout=2)

    @property
    def settings_close_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingPopup/Background/CloseButton', timeout=2)

    def is_displayed_misson(self):
        return self.mission_popup

    def is_displayed_setting(self):
        return self.setting_popup

    def press_mission_close_button(self):
        self.mission_close_button.tap()

    def press_settings_close_button(self):
        self.settings_close_button.tap()



