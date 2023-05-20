import pandas as pd
from menu.save import prompt_save

def dataset_menu(options, choice, lang): ####################
    if choice == None: # [ESCAPE]: Go back to the main menu #
        return (None, 'main') ###############################

    foods = pd.read_csv(r'./Frida20220615/Frida_Dataset_June2022.csv', delimiter=';').sort_values(by=['FoodID']).reset_index()#.set_index('FoodID')

    groups = foods[['FoodGroupID','FoodGroup','FødevareGruppe']].drop_duplicates(keep='first').sort_values(by=['FoodGroupID']).reset_index()#.set_index('FoodGroupID')

    match choice:

        case 0:

            results = groups

            match lang:

                case 'da':
                    print(f'Resultater fundet: {len(groups.index)}')
                    print()
                    for index, group in groups.iterrows(): print(group['FødevareGruppe'])

                case 'en':
                    print(f'Results found: {len(groups.index)}')
                    print()
                    for index, group in groups.iterrows(): print(group['FoodGroup'])

        case 1:

            name = input(f'{options[choice]}: ')

            match lang:

                case 'da':
                    results = groups[groups['FødevareGruppe'].str.lower().str.contains(name.lower())]
                    print(f'Resultater fundet: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['FødevareGruppe'])

                case 'en':
                    results = groups[groups['FoodGroup'].str.lower().str.contains(name.lower())]
                    print(f'Results found: {len(results.index)}')
                    print()
                    for index, group in results.iterrows(): print(group['FoodGroup'])

    print()

    prompt_save(results, lang)

    return (results, 'dataset')
