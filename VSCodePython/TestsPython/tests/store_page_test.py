from pages.store_page import StorePage
import pytest

class TestStorePage():
    @pytest.fixture(autouse=True)
    def before_and_after_test(self, altdriver):
        self.store_page = StorePage(altdriver)
        self.store_page.load()

    def test_store_page_loaded_correctly(self):
        self.store_page.press_item_tab_switcher()
        assert (self.store_page.is_dispalyed_shop())

    def test_item_tab_switcher(self):
        self.store_page.press_item_tab_switcher()
        assert (self.store_page.is_displayed_item_list_tab())

    def test_character_tab_switcher(self):
        self.store_page.press_character_tab_switcher()
        assert (self.store_page.is_displayed_character_list_tab())

    def test_accesories_tab_switcher(self):
        self.store_page.press_accesories_tab_switcher()
        assert (self.store_page.is_displayed_character_accessories_list_tab())

    def test_themes_tab_switcher(self):
        self.store_page.press_themes_tab_switcher()
        assert (self.store_page.is_displayed_theme_list_tab())