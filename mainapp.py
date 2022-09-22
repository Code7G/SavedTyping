from pathlib import Path # for creating save folders and files


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


save_file = [] # short term save file
path = Path('Saves') # location of the save files
all_saves = Path('Saves\All_saves1~.txt')

# identifying the save files for creating new ones:
all_path = path.rglob('*.txt')
last_save_file = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
files = {}

for i in all_path:
    last_save_file.append(str(i))
for c in last_save_file:
    if '~' in c: # the '~' symbol is used to identify the files generated from the program
        for l in c:
            if l in numbers:
                files[c] = int(files.get(c, 0)) + int(l) # getting the number value of the files


if all_saves.exists():
    all_numbers = []

    for item in files:
        all_numbers.append(files.get(item))
    
    # finding the largest number in the files 
    max = 0
    for num in all_numbers:
        if max < num:
            max = num

    all_saves_second = Path(f'Saves/All_saves{max + 1}~.txt') # creating the name for the new file

    while True:
        writing_e = writing()
        save_file.append(writing_e)

        if 'help' in save_file:
            save_file.remove('help')

        if writing_e == 'end':
            save_file.remove('end')
            all_saves_second.write_text(str(save_file)) # using the new name for file creation
            print(f'Full save >>>>{all_saves_second.read_text()}<<<<')
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
            
            # creating the 'Saves' folder and the first save file
            folder = Path("Saves/")
            folder.mkdir(parents=True, exist_ok=True)
            fn = "All_saves1~.txt"
            filepath = folder / fn
            with filepath.open("w", encoding="utf-8") as file:
                file.write(str(save_file))
                break

        if writing_e == 'saved':
            save_file.remove('saved')
            print(f'Last save >>>>{save_file}<<<<')
