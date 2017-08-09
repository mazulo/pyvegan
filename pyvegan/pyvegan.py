"""Script to gather vegan recipes from some sites"""
import argparse
import sys


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

    if __name__ == '__main__':
        sys.exit(main())
