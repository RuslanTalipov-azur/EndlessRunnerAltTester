from pages.base_page import BasePage
from alttester import By


class StorePage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Shop')

    @property
    def store_title(self):
        return self.altdriver.wait_for_object(By.NAME, 'StoreTitle', timeout=2)

    @property
    def item_tab_switcher(self):
        return  self.altdriver.wait_for_object(By.NAME, 'TabsSwitch/Item', timeout=2)

    @property
    def character_tab_switcher(self):
        return self.altdriver.wait_for_object(By.NAME, 'TabsSwitch/Character', timeout=2)

    @property
    def accesories_tab_switcher(self):
        return self.altdriver.wait_for_object(By.NAME, 'TabsSwitch/Accesories', timeout=2)

    @property
    def themes_tab_switcher(self):
        return self.altdriver.wait_for_object(By.NAME, 'TabsSwitch/Themes', timeout=2)

    @property
    def item_list_tab(self):
        return self.altdriver.wait_for_object(By.NAME, 'ItemsList', timeout=2)

    @property
    def character_list_tab(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharacterList', timeout=2)

    @property
    def character_accessories_list_tab(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharacterAccessoriesList', timeout=2)

    @property
    def theme_list_tab(self):
        return self.altdriver.wait_for_object(By.NAME, 'ThemeList', timeout=2)

    def is_displayed_item_list_tab(self):
        return self.item_list_tab

    def is_displayed_character_list_tab(self):
        return self.character_list_tab

    def is_displayed_character_accessories_list_tab(self):
        return self.character_accessories_list_tab

    def is_displayed_theme_list_tab(self):
        return self.theme_list_tab


    def is_dispalyed_shop(self):
        return self.store_title \
            and self.item_tab_switcher \
            and self.character_tab_switcher \
            and self.accesories_tab_switcher \
            and self.themes_tab_switcher

    def press_item_tab_switcher(self):
        self.item_tab_switcher.tap()

    def press_character_tab_switcher(self):
        self.character_tab_switcher.tap()

    def press_accesories_tab_switcher(self):
        self.accesories_tab_switcher.tap()

    def press_themes_tab_switcher(self):
        self.themes_tab_switcher.tap()



