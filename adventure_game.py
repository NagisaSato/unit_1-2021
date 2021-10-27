import time
#start time is recorded
start_time = time.time()

play_time = round(time.time() - start_time)
if play_time > 900:
    print("your time is up. You did not complete the challenge")
    exit()

#list of possible user inputs
answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

#items are added here and displayed when user types in "inventory"
inventory = []

#introduction
def displayintro():
    print("""
    WELCOME TO THE CHALLENGE!
    
    To begin with, please enter your name and grade level.
    
    Then input the name of your advisor.
    """)

displayintro()


#system to confirm the users' input (giving the chance of rentering information)
def confirm_input(property):
    answer = input('>> ')
    while answer not in answer_yes and answer not in answer_no:
        answer = input('Wrong input, enter Yes or No: ')
    while answer in answer_no:
        name = input(f'Please enter your {property}: ')
        answer = input(f'Is your {property} {name}? (Yes/No): ')

#check for three different properties
name = input('Name >> ')
print(f'is your name {name}? (Yes/No): ')
confirm_input(property='name')

grade = input('Grade level >> ')
print(f'is your grade {grade}? (Yes/No): ')
confirm_input(property='grade')

advisor = input('Advisor >> ')
print(f'is your advisor {advisor}? (Yes/No): ')
confirm_input(property='advisor')




#start of story
print(f"""
Is is 13:10, the worst time of the day, STOP AND CLEAN.
{advisor} has assigned you to the KAC 1, and you are currently in KAC 1. 
However you suddenly remember that you have forgotten to close your room curtains before leaving for stop and clean.
You really need to go back and close the curtains, otherwise people might find out that you have an alpaca living in your room.
""")

alpaca = input("Enter your alpaca's name >> ")

print(f"""
You are concerned about {alpaca}, and you need to go back to your house, but we all know negotiating with Mr. McGibbon, 
king of the KAC never works out.
Especially anything with stop and clean is non-negotiable, even mentioning it will enrage him. 
Therefore, you will need to escape from the KAC without getting caught.
Your goal is to go home before end of stop and clean, 13:25.

Would you like to stay in KAC 1 and look around, or pretend to look for someone and move to the library area? (Kac1/library area)
""")

#chose between kac or library
ans2 = input(">> ")

print()

kac1 = ["Kac 1", "kac 1", "kac1", "Kac1"]
library = ["Library", "library", "Library area", "library area"]

if ans2 in kac1:
    #this is success for player and game continues
    print("There is a roll of toilet paper and a bottle of disinfection spray.")
else:
    if ans2 in library :
        print(f"""
        'HeLlOooooOoooOOoooo {name}!!!!' 
        Mr. Onder finds you and happily gives you an important task to rearrange 50 books during stop and clean.
        You can no longer go home before end of stop and clean.
        
        You needed to think of any possibilities before you made your move...
        
        GAME OVER.
        
        {name}, I thought you were better than this...
        """)
    else:
        #if answer is neither kac or library, the game is over
        print(f"Your input was not understood, and {alpaca} is spotted by Mr. Lacoste. ")

    exit()

print()

print("Would you like to pick the items up? (yes/no)")
ans3 = input(">> ")



if ans3 in answer_yes:
    print("Items picked up.")
    inventory.append("toilet paper")
    inventory.append("disinfection spray")

else:
    print("Then let us proceed.")

print("Type 'Inventory' to see the items you have picked up")
ans4 = input(">> ")
if ans4 == "inventory" or "Inventory":
    print(inventory)
else:
    print("type in 'inventory'")
    ans4 = input(">> ")
    print(inventory)




print()
print("End of game")
print()
print(f"Name: {name}")
play_time = round(time.time() - start_time)
print(f"Time taken: {play_time} seconds")
time_exact = 10 + round(play_time/60)
print(f"The time now is 13:{time_exact}")

if time_exact < 25:
    print(f"Well done. {name}, you have completed the challenge before the end of stop and clean.")
else:
    print(f"You did not complete the challenge on time... {alpaca} has been found by {advisor}, and got realeased deep in the ISAK forest ")



with open ("database.txt", "w") as file:
    file.write(f"{name},{play_time}\n")

























