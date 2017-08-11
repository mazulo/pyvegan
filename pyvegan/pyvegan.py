"""Script to gather vegan recipes from some sites"""
import argparse
import sys

import requests


from utils import search_recipe, parse_content, create_menu


def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(
        prog='PyVegan',
        description='The better way to collect some delicious vegan recipes!',
        usage="""
        PyVegan - Get delicious vegan recipes from the web!
        Usage: pyvegan [-s/--search ingredient_to_search]


        Examples:
        - Get recipes with potato
            $ pyvegan -s batata
        - Get recipes that use more than one ingredient
            $ pyvegan -s "batata e tomate"

        How to get basic options and help? Use -h/--help
        """,
    )
    parser.add_argument(
        '-s',
        '--search',
        type=str,
        help='Get recipes using the given ingredients'
    )

    options = parser.parse_args()

    if options.search:
        param = options.search
    else:
        param = ''

    try:
        content = search_recipe(param)
    except requests.ConnectionError:
        print('A connection problem occurred.')
    except requests.Timeout:
        print('A timeout problem occurred.')
    except requests.TooManyRedirects:
        msg = (
            'The request exceeds the configured'
            ' number of maximum redirections.'
        )
        print(msg)

    if not content:
        return

    list_recipes = parse_content(content)

    menu = create_menu(list_recipes)
    menu.show()


if __name__ == '__main__':
    sys.exit(main())
