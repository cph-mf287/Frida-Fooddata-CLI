from simple_term_menu import TerminalMenu
from menu.main import main_menu
from menu.lang import lang_menu
from menu.food import food_menu
from menu.dataset import dataset_menu

lang = 'en'
menu = 'main'
quit = False

#results = None # The whole file is one scope

while quit == False:

    file = open(f'./menu/{lang}/{menu}.txt')
    options = [line.strip() for line in file.readlines()] #options = [[s.strip() for s in line.rstrip('\n').split('=', 1)] for line in file.readlines()]
    file.close()
    
    choice = TerminalMenu(options, quit_keys=['escape']).show()

    match menu:

        case 'main': (menu, quit) = main_menu(options, choice)

        case 'lang': (lang, menu) = lang_menu(options, choice, lang)

        case 'food': (results, menu) = food_menu(options, choice, lang)

        case 'dataset': (results, menu) = dataset_menu(options, choice, lang)
