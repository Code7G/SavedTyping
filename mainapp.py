from pathlib import Path  # for creating save folders and files


# the main function for user input
def writing():
    write = input('>')
    if write == 'quit':
        return 'end'
    if write == 'save':
        return 'saved'
    if write == 'help':
        print('''Commands:
              quit = qiut the app
              save = veiw the last save
              help = display help''')
    return write


save_file = []  # short term save file
all_saves = Path('Saves\All_saves.txt')  # location of the save file

if all_saves.exists():
    while True:
        writing_e = writing()
        save_file.append(writing_e)

        if 'help' in save_file:
            save_file.remove('help')

        # saving the changes to the save file
        if writing_e == 'end':
            save_file.remove('end')
            all_saves.write_text(f'''
            {all_saves.read_text()}
                                 
            {str(save_file)}''')
            break

        if writing_e == 'saved':
            save_file.remove('saved')
            print(f'Last save >>>>{save_file}<<<<')

if all_saves.exists() == False:
    while True:
        writing_e = writing()
        save_file.append(writing_e)

        if 'help' in save_file:
            save_file.remove('help')

        if writing_e == 'end':
            save_file.remove('end')

            # creating the 'Saves' folder and the save file
            folder = Path("Saves/")
            folder.mkdir(parents=True, exist_ok=True)
            fn = "All_saves.txt"
            filepath = folder / fn
            with filepath.open("w", encoding="utf-8") as file:
                file.write(str(save_file))
                break

        if writing_e == 'saved':
            save_file.remove('saved')
            print(f'Last save >>>>{save_file}<<<<')
