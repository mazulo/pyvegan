import sys
from webbrowser import open as url_open

from bs4 import BeautifulSoup
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
import requests as req


SEARCH_URL = 'http://presuntovegetariano.com.br/?s={}&lang=en'


class Browser:
    DEFAULT_SEARCH_URL = 'http://presuntovegetariano.com.br/?s={}&lang=en'
    
    def __init__(self, url=DEFAULT_SEARCH_URL):
        self.url = url
        self.response = None

    def search(self, words):
        """Search using the given ingredients"""

        params = '+'.join(words.split())
        url_search = self.url.format(params)
        self.response = req.get(url_search)
    
    def page_content(self):
        """Returns the page HTML"""

        if not self.response:
            raise Exception('Search for something first')

        return self.response.content


class Recipe:
    def __init__(self, link=None, title='', content=None):
        self.link = link
        self.title = self.__format_title(title)
        self.content = content

    def __format_title(self, title):
        """Clean and return the received title"""

        result = title.encode('utf-8')

        if sys.version_info.major == 3:
            result = result.decode()
        return result


class RecipeManager:
    def __init__(self, html_content):
        self.parsed_html = BeautifulSoup(html_content, 'html.parser')
        self.recipes = []

        self.__parse(self.parsed_html)
    
    def __parse(self, html):
        """Parse the HTML content to retrieve the desired info"""

        for div in html.find_all('div', attrs={'class': 'post'}):
            div_content = div.find(
                'div',
                attrs={'class': 'fusion-post-content-container'}
            )

            recipe = Recipe(
                link=div.a.attrs['href'],
                title=div.h1.get_text(),
                content=div_content.get_text()
            )

            self.recipes.append(recipe)


class Menu:
    def __init__(self, recipes):
        self.recipes = recipes
        
        self.title = 'PyVegan - List of Recipes'
        self.menu = CursesMenu(self.title, 'Select one and press enter')
        self.error_msg = 'This search isn\'t a valid one'

    def build(self):
        for recipe in self.recipes:
            if recipe.link:
                item = FunctionItem(
                    recipe.title,
                    url_open,
                    args=[recipe.link]
                )
            else:
                item = FunctionItem(recipe.title, lambda x: print(x), args=[self.error_msg])
            self.menu.append_item(item)

    def show(self):
        self.menu.show()
        

