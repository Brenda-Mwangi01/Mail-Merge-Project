#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# draft_letter = "Day 24 Mail-Merge-Project-Starting\Input\Letters\starting_letter.txt"
# names_file = "Day 24 Mail-Merge-Project-Starting\Input\Letters\Names\invited_names.txt"
with open("./Input/Letters/starting_letter.txt") as let:
    letter = let.read()

with open("./Input/Names/invited_names.txt") as names:
    invitee = names.readlines()

for name in invitee:
    new_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_to_{new_name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", new_name))
