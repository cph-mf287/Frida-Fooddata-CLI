from menu.key import get_key

def lang_menu(options, choice, lang):

    match get_key(options, choice):

        case '1': # Danish
            lang = 'da'

        case '2': # English
            lang = 'en'

    return (lang, 'main')
