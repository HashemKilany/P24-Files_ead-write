#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./input/Names/invited_names.txt", "r") as y:
    names = y.read().split()
with open("./input/letters/starting_letter.txt", mode="r") as x:
    letter = x.read()
    for i in names:
        new_letter = letter.replace('[name]', i)
        with open(f"./Output/ReadyToSend/letter_for_{i}.txt", "w") as Z:
            Z.write(new_letter)
