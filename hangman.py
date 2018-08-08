import random


def generate_word():
    word_list = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
            ]
    random_word = random.SystemRandom()
    return random_word.choice(word_list)


def get_user_choice():
    return str.lower(input('Your Choice: '))
    

def start_game():
    turns = 3
    print('Would you like to play hangman? y/n')
    user_choice = get_user_choice()
    if user_choice == 'y':
        word = generate_word()
        word_display = list('*' * len(word))
        play_game(turns, word, word_display)
    elif user_choice == 'n':
        print('OK! We can play next time.')
    else:
        print('Selection invalid! Please select y or n' )

        
def play_game(turns, word, word_display):
    letters_used = set()
    play = True
    if turns > 3:
        play = True
 
    while play:
        if turns <= 0:
            play = False

        print('select a letter...')
        user_choice = get_user_choice()
  
        if user_choice in letters_used:   
            print(letters_used)
            print('You have already selected that letter, please try another.')
        else:
            letters_used.add(user_choice)
            if user_choice not in word:
               
                if turns > 0:
                    print('Gosh Darn It! That letter is not in the word.  Try Again')
                    turns = turns - 1
                else:
                    play = False
            for index, ltr in enumerate(word):
                if user_choice == ltr:
                    print('Nice Job! You got a letter')
                    word_display[index] = user_choice  

        if '*' not in word_display:
            print('YOU WIN!')
            play = False    
        print(word_display)
        if turns >= 1:
            print('You have ' + str(turns) + ' turns left')
            print('-' * 30)
        else:
            print('You are out of turns, GAME OVER')
            print('The word was: ' + str.upper(word))
            play = False

             
start_game()  

