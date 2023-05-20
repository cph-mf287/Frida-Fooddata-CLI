from menu.key import get_key

def main_menu(options, choice, quit=False): #####
    if choice == None: # [ESCAPE]: Quit the CLI #
        return ('main', True) ###################

    match get_key(options, choice):
        case '1': # Language
            menu = 'lang'
        case '2': # Food entries
            menu = 'food'
        case '3': # Food groups
            menu = 'dataset'
        case 'q': # Quit
            quit = True

    return (menu, quit)
