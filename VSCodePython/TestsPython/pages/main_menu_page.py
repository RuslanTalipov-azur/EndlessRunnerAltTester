from pages.base_page import BasePage
from alttester import By


class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StoreButton', timeout=2)
    
    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'OpenLeaderboard', timeout=2)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingButton', timeout=2)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'MissionButton', timeout=2)

    @property
    def run_button(self):   
        return self.altdriver.wait_for_object(By.NAME, 'StartButton', timeout=2)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharName', timeout=2)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'ThemeZone', timeout=2)

    def is_displayed(self):
        return self.store_button \
            and self.leader_board_button \
            and self.settings_button \
            and self.mission_button \
            and self.run_button \
            and self.character_name \
            and self.theme_name

    def press_run(self):
        self.run_button.tap()

    def press_mission_button(self):
        self.mission_button.tap()

    def press_settings_button(self):
        self.settings_button.tap()

    def press_store_button(self):
        self.store_button.tap()