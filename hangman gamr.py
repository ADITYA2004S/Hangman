import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
/$$
| $$
| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$
| $$__  $$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
| $$  \ $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                               /$$  \ $$
                              |  $$$$$$/
                               \______/                                    '''


print(logo)



Word_List = ["the godfather", "12 angry men", "forrest gump", "inception", "interstellar", "psycho", "gladiator", "parasite"]
display = []

Word_choice = random.choice(Word_List)
Word_length = len(Word_choice)
lives = 6
print("Select correct letters to fill the gaps below ")

for _ in range(Word_length):
    display+="_"
print(display)





end_of_game = False

while not end_of_game:
    User_input = input("Please enter the letter :- ").lower()
    #print(f"the chosen word is {Word_choice}")


    for position in range(Word_length):
        letter = Word_choice[position]
        if letter == User_input:
            display[position] = letter



    if User_input not in Word_choice:
        lives-=1
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")


    print(stages[lives])