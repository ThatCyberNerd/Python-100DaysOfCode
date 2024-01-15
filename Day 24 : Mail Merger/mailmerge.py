with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as invite_letter:
            invite_letter.write(new_letter)
