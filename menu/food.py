import pandas as pd
from simple_term_menu import TerminalMenu
from menu.key import get_key
from menu.bool import comparator, def_crit
from menu.save import prompt_save

def food_menu(options, choice, lang):

    if (choice is None) | (get_key(options, choice) == '<'):
        return (None, 'main')

    match choice:

        case 0:

            name = input(f'{options[choice]}: ')

            foods = pd.read_csv(r'./Frida20220615/Data_Table.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')

            match lang:

                case 'da':
                    results = foods[foods['FødevareNavn'].str.lower().str.contains(name.lower())].sort_values(['FødevareNavn']).reset_index()
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, food in results.iterrows(): print(food['FødevareNavn'])

                case 'en':
                    results = foods[foods['FoodName'].str.lower().str.contains(name.lower())].sort_values(['FoodName']).reset_index()
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, food in results.iterrows(): print(food['FoodName'])

        case 1:

            name = input(f'{options[choice]}: ')

            foods = pd.read_csv(r'./Frida20220615/Data_Table.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')

            match lang:

                case 'da':
                    results = foods[foods['FødevareGruppe'].str.lower().str.contains(name.lower())].sort_values(['FødevareGruppe','FødevareNavn']).reset_index()
                    print(f'Resultater fundet: {len(results.index)}')
                    for index, group in results[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').reset_index().iterrows():
                        print()
                        print(group['FødevareGruppe'].upper())
                        print('-'*len(group['FødevareGruppe']))
                        for index, food in results.iterrows(): print(food['FødevareNavn'])

                case 'en':
                    results = foods[foods['FoodGroup'].str.lower().str.contains(name.lower())].sort_values(['FoodGroup','FoodName']).reset_index()
                    print(f'Results found: {len(results.index)}')
                    for index, group in results[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').reset_index().iterrows():
                        print()
                        print(group['FoodGroup'].upper())
                        print('-'*len(group['FoodGroup']))
                        for index, food in results.iterrows(): print(food['FoodName'])

        case 2:

            params = pd.read_csv(r'./Frida20220615/Parameter.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')

            groups = params[['ParameterGroupID','ParameterGroupName','ParameterGruppeNavn']].drop_duplicates(keep='first')#.sort_values(['ParameterGroupID']).reset_index()#.set_index('ParameterGroupID')

            match lang:

                case 'da': options = [value for index, value in groups['ParameterGruppeNavn'].sort_values().reset_index()['ParameterGruppeNavn'].items()]

                case 'en': options = [value for index, value in groups['ParameterGroupName'].sort_values().reset_index()['ParameterGroupName'].items()]

            choice = TerminalMenu(options, quit_keys=['escape']).show()

            if (choice is None) | (get_key(options, choice) == '<'):
                return (None, 'food')

            print(options[choice])

            match lang:

                case 'da': options = [value for index, value in params[params['ParameterGruppeNavn'] == options[choice]]['ParameterNavn'].sort_values().reset_index()['ParameterNavn'].items()]

                case 'en': options = [value for index, value in params[params['ParameterGroupName'] == options[choice]]['ParameterName'].sort_values().reset_index()['ParameterName'].items()]

            choice = TerminalMenu(options, quit_keys=['escape']).show()

            if (choice is None) | (get_key(options, choice) == '<'):
                return (None, 'food')

            print(options[choice])

            (req, min, max) = def_crit(lang)

            foods = pd.read_csv(r'./Frida20220615/Data_Normalised.csv', delimiter=';')#.sort_values(['FoodID']).reset_index()#.set_index('FoodID')

            match lang:

                case 'da':
                    try:
                        foods = foods.loc[foods['ParameterNavn'] == options[choice]]#.sort_values(['FødevareNavn']).reset_index()
                        results = foods.loc[:,:]
                        results['DotVal'] = foods['ResVal'].apply(lambda val: float(str(val).replace(',','.')))
                        results['Covers'] = results['DotVal']/req
                        results['Lacks'] =  1 - results['DotVal']/req
                        results['Recommended'] = 100 / (results['DotVal']/req)
                        results = results[comparator(results['DotVal'], min, max)].sort_values(['DotVal'], ascending=False).reset_index()
                        print(f'Resultater fundet: {len(results.index)}')
                        print()
                        #for index, food in results.iterrows(): print(f'{food.ResVal} — {food.FødevareNavn}')
                        print(results[['FødevareNavn','ResVal','Covers','Lacks','Recommended']].set_index('FødevareNavn'))
                        results = results.drop('DotVal', axis=1)
                    except ValueError:
                        results = None
                        print('Resultater fundet: 0')

                case 'en':
                    try:
                        foods = foods.loc[foods['ParameterName'] == options[choice]]#.sort_values(['FoodName']).reset_index()
                        results = foods.loc[:,:]
                        results['DotVal'] = foods['ResVal'].apply(lambda val: float(str(val).replace(',','.')))
                        results['Covers'] = results['DotVal']/req
                        results['Lacks'] =  1 - results['DotVal']/req
                        results['Recommended'] = 100 / (results['DotVal']/req)
                        results = results[comparator(results['DotVal'], min, max)].sort_values(['DotVal'], ascending=False).reset_index()
                        print(f'Results found: {len(results.index)}')
                        print()
                        #for index, (food) in results.iterrows(): print(f'{food.DotVal} — {food.FoodName}')
                        print(results[['FoodName','DotVal','Covers','Lacks','Recommended']].set_index('FoodName'))
                        results = results.drop('DotVal', axis=1)
                    except ValueError:
                        results = None
                        print('Results found: 0')

    print()

    prompt_save(results, lang)

    return (results, 'food')
