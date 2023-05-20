import pandas as pd
from menu.save import prompt_save

def food_menu(options, choice, lang): #######################
    if choice == None: # [ESCAPE]: Go back to the main menu #
        return (None, 'main') ###############################

    name = input(f'{options[choice]}: ')

    foods = pd.read_csv(r'./Frida20220615/Frida_Dataset_June2022.csv', delimiter=';').sort_values(by=['FoodID']).reset_index()#.set_index('FoodID')

    #groups = foods[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').sort_values(by=['FoodGroupID']).reset_index()#.set_index('FoodGroupID')

    match choice:

        case 0:

            match lang:

                case 'da':
                    results = foods[foods['FødevareNavn'].str.lower().str.contains(name.lower())]
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, food in results.iterrows(): print(food['FødevareNavn'])

                case 'en':
                    results = foods[foods['FoodName'].str.lower().str.contains(name.lower())]
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, food in results.iterrows(): print(food['FoodName'])

        case 1:

            match lang:

                case 'da':
                    results = foods[foods['FødevareGruppe'].str.lower().str.contains(name.lower())].sort_values(by=['FødevareGruppe'])
                    print(f'Resultater fundet: {len(results.index)}')
                    for index, group in results[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').reset_index().iterrows():
                        print()
                        print(group['FødevareGruppe'].upper())
                        print('-'*len(group['FødevareGruppe']))
                        for index, food in results.iterrows(): print(food['FødevareNavn'])

                case 'en':
                    results = foods[foods['FoodGroup'].str.lower().str.contains(name.lower())].sort_values(by=['FoodGroup'])
                    print(f'Results found: {len(results.index)}')
                    for index, group in results[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').reset_index().iterrows():
                        print()
                        print(group['FoodGroup'].upper())
                        print('-'*len(group['FoodGroup']))
                        for index, food in results.iterrows(): print(food['FoodName'])

    print()

    prompt_save(results, lang)

    return (results, 'main')
