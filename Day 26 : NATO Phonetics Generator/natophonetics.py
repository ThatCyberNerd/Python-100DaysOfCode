import pandas

word = input("Enter your name or any word : ").upper()
phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index,row) in phonetics.iterrows()}

nato = [dictionary[letter] for letter in word]
print(nato)
