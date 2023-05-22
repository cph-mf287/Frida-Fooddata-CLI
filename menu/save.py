from simple_term_menu import TerminalMenu

def prompt_save(results, lang):

    if results is not None and len(results.index):

        match lang:

            case 'da': options = ['Gem', 'Kassér']

            case 'en': options = ['Save', 'Discard']

        choice = TerminalMenu(options, quit_keys=['escape']).show()

        match choice:

            case 0:

                match lang:

                    case 'da': name = input('Gem som: ')

                    case 'en': name = input('Save as: ')

                results.to_csv(f'./saved/{name}.csv', sep=';')

                print()

    else:

        print('Nothing to save')
        print()
