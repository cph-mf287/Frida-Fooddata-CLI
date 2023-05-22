import pandas as pd
from menu.key import get_key
from menu.save import prompt_save

def dataset_menu(options, choice, lang):

    if (choice is None) | (get_key(options, choice) == '<'):
        return (None, 'main')

    match get_key(options, choice):

        case '1':

            name = input(f'{options[choice]}: ')

            foods = pd.read_csv(r'./Frida20220615/Frida_Dataset_June2022.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')
            groups = foods[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first')#.sort_values(['FoodGroupID']).reset_index()#.set_index('FoodGroupID')

            match lang:

                case 'da':
                    results = groups[groups['FødevareGruppe'].str.lower().str.contains(name.lower())].sort_values(['FødevareGruppe']).reset_index()
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['FødevareGruppe'])

                case 'en':
                    results = groups[groups['FoodGroup'].str.lower().str.contains(name.lower())].sort_values(['FoodGroup']).reset_index()
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['FoodGroup'])

        case '2':

            name = input(f'{options[choice]}: ')

            params = pd.read_csv(r'./Frida20220615/Parameter.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')
            groups = params[['ParameterGroupID','ParameterGroupName','ParameterGruppeNavn']].drop_duplicates(keep='first')#.sort_values(['ParameterGroupID']).reset_index()#.set_index('ParameterGroupID')

            match lang:

                case 'da':
                    results = groups[groups['ParameterGruppeNavn'].str.lower().str.contains(name.lower())].sort_values(['ParameterGruppeNavn']).reset_index()
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['ParameterGruppeNavn'])

                case 'en':
                    results = groups[groups['ParameterGroupName'].str.lower().str.contains(name.lower())].sort_values(['ParameterGroupName']).reset_index()
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['ParameterGroupName'])

        case '3':

            name = input(f'{options[choice]}: ')

            params = pd.read_csv(r'./Frida20220615/Parameter.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')

            match lang:

                case 'da':
                    results = params[params['ParameterGruppeNavn'].str.lower().str.contains(name.lower())].sort_values(['ParameterGruppeNavn']).reset_index()
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['ParameterNavn'])

                case 'en':
                    results = params[params['ParameterGroupName'].str.lower().str.contains(name.lower())].sort_values(['ParameterGroupName']).reset_index()
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['ParameterName'])

        case '<':

            return (None, 'main')

    print()

    prompt_save(results, lang)

    return (results, 'dataset')




# FORMULA:
# (1 + (1 - (800/900)))*100