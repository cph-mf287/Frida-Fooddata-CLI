def def_crit(lang):

    match lang:

        case 'da': options = [ 'Behov', 'Mere end', 'Mindre end' ]

        case 'en': options = [ 'Requirement', 'More than', 'Less than' ]

    try: req = float(input(f'{options[0]}: '))
    except ValueError: req = None

    try: min = float(input(f'{options[1]}: '))
    except ValueError: min = None

    try: max = float(input(f'{options[2]}: '))
    except ValueError: max = None

    return (req, min, max)

def comparator(val, min, max):

    if min is not None and max is not None:
        return (min < val) & (val < max)

    if min is None and max is not None:
        return val < max

    if max is None and min is not None:
        return min < val

    return val == val

    return max > val > min if max is not None and min is not None else val > min if min is not None else max > val if max is not None else val > 0

    # (min,  max)
    #   S  v  S
    #   N  v  S
    #   S  v  N
    #   N  v  N   > 0
