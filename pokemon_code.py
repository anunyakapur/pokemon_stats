import csv
def entry_creation():
    with open("Pokemon.csv", "r") as file_in:

        reader = csv.DictReader(file_in)
        pokemon_dic = {}
        
        for line in reader:
            #print(line)
            pokemon_entry = [line["#"], \
                             line['Name'], \
                             line['Type 2'], \
                             line['Total'], \
                             line['HP'], \
                             line["Attack"], \
                             line["Defense"], \
                             line["Sp. Atk"], \
                             line["Sp. Def"], \
                             line["Speed"], \
                             line["Generation"], \
                             line["Legendary"]]

            if line['Type 1'] not in pokemon_dic:
                pokemon_dic[line["Type 1"]] = []
            pokemon_dic[line["Type 1"]].append(pokemon_entry)
        return pokemon_dic


def write_file(supporting):
    with open("pokemon_organized.txt", "w") as file_out:
        x = ""
        for key in supporting:
            x += key + "\n"
            x += str(len(supporting[key])) + "\n"
            for item in supporting[key]:
                entry = ""
                name = item[1]
                type2 = item[2]
                total = int(item[3])
                HP = int(item[4])
                attack = int(item[5])
                defense = int(item[6])
                spatk = int(item[7])
                spdef = int(item[8])
                speed = int(item[9])
                generation = int(item[10])
                legendary = item[11]
                entry += f'{name}, ' + f'{type2}, ' + f'{total}, ' + f'{HP}, ' + f'{attack}, ' + f'{defense}, ' + f'{spatk}, ' + f'{spdef}, ' + f'{speed}, ' +  f'{generation}, ' + f'{legendary}'  + "\n"
                x += entry
        file_out.write(x)

pokemon_dict = entry_creation()
#print(pokemon_dict)
write_file(pokemon_dict)
