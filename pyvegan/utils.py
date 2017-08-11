import sys
from webbrowser import open as url_open

from bs4 import BeautifulSoup
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
import requests as req


SEARCH_URL = 'http://presuntovegetariano.com.br/?s={}&lang=en'


def search_recipe(ingredients):
    """Search using the given ingredients and return the HTML"""

    params = '+'.join(ingredients.split())
    url_search = SEARCH_URL.format(params)
    response = req.get(url_search)

    return response.content


def parse_content(content):
    """Parse the HTML content to retrieve the desired info"""

    post = {}
    list_recipes = []
    parsed_html = BeautifulSoup(content, 'html.parser')

    for div in parsed_html.find_all('div', attrs={'class': 'post'}):
        div_content = div.find(
            'div',
            attrs={'class': 'fusion-post-content-container'}
        )
        post = {
            'post_link': div.a.attrs['href'],
            'post_title': div.h1.get_text(),
            'post_content': div_content.get_text(),
        }
        list_recipes.append(post)

    return list_recipes


def clean_title(title):
    """Clean and return the received title"""

    result = title.encode('utf-8')

    if sys.version_info.major == 3:
        result = result.decode()
    return result


def create_menu(list_recipes):
    """Create a CLI menu using CursesMenu"""

    title = 'PyVegan - List of Recipes'
    menu = CursesMenu(title, 'Select one and press enter')
    msg = 'This search isn\'t a valid one'

    for recipe in list_recipes:
        recipe_title = clean_title(recipe['post_title'])

        if 'post_link' in recipe:
            item = FunctionItem(
                recipe_title,
                url_open,
                args=[recipe['post_link']]
            )
        else:
            item = FunctionItem(recipe_title, lambda x: print(x), args=[msg])
        menu.append_item(item)

    return menu
