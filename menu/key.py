def get_key(options, choice):
    if choice == None:
        return 'escape'
    try:
        return options[choice][options[choice].find('[') + 1 : options[choice].find(']')]
    except ValueError:
        return -1