from menu.key import get_key

def main_menu(options, choice, quit=False): #####
    if choice == None: # [ESCAPE]: Quit the CLI #
        return ('main', True) ###################

    match get_key(options, choice):

        case '1': return ('lang', False)

        case '2': return ('food', False)

        case '3': return ('dataset', False)

        case 'q': return ('main', True)
