from pages.main_menu_page import MainMenuPage
from pages.main_menu_popup import MainMenuPopup
import pytest

class TestMainMenuButtons():
    @pytest.fixture(autouse=True)
    def before_and_after_test(self, altdriver):
        self.main_menu_page = MainMenuPage(altdriver)
        self.main_menu_page.load()
        self.main_menu_popup = MainMenuPopup(altdriver)

    def test_main_menu_page_loaded_correctly(self):
        assert (self.main_menu_page.is_displayed())

    def test_main_menu_mission_button(self):
        self.main_menu_page.press_mission_button()
        assert (self.main_menu_popup.is_displayed_misson())
        #self.main_menu_popup.press_mission_close_button()
        #print("close mission_popup")

    def test_main_menu_settings_button(self):
        self.main_menu_page.press_settings_button()
        assert (self.main_menu_popup.is_displayed_setting())
        # self.main_menu_popup.press_settings_close_button()
        # print("close settings_popup")