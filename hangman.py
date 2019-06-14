import random

categories = {
    "countries": ['albania', 'andorra', 'austria', 'belarus', 'belgium', 'bulgaria', 'croatia', 'czech',
                  'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary',
                  'iceland', 'ireland', 'italy', 'latvia', 'liechtenstein', 'lithuania', 'luxembourg',
                  'malta', 'moldova', 'monaco', 'netherlands', 'norway', 'poland', 'portugal', 'romania',
                  'russia', 'serbia', 'slovakia', 'slovenia', 'spain', 'sweden', 'switzerland', 'ukraine'],

    "animals": ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow',
                'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'fox', 'frog',
                'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion',
                'lobster', 'monkey', 'octopus', 'owl', 'panda', 'pig', 'puppy', 'rabbit', 'rat', 'scorpion', 'seal',
                'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel', 'tiger', 'turtle', 'wolf', 'zebra'],

    "sports": ['archery', 'badminton', 'baseball', 'basketball', 'bmx', 'bowling', 'boxing', 'cheerleading', 'cricket',
               'curling', 'cycling', 'dance', 'darts', 'dodgeball', 'fishing', 'football', 'golf',
               'gymnastics', 'handball', 'kayaking', 'lacrosse', 'mma', 'biking', 'polo', 'climbing', 'rugby',
               'sailing', 'shooting', 'skateboarding', 'skiing', 'skydiving', 'snowboarding', 'softball', 'squash',
               'surfing', 'swimming', 'tennis', 'volleyball', 'wrestling']}

used_letters = []
made_list = list(categories.keys())
drawn_category = random.choice(made_list)
drawn_word = random.choice(categories[drawn_category])
word_length = len(drawn_word)
hangman_pic = ['''



  +---+

  |   |

      |

      |

      |

      |

 =========''', '''



  +---+

  |   |

  O   |

      |

      |

      |

 =========''', '''



  +---+

  |   |

  O   |

  |   |

      |

      |

=========''', '''



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

 /|\  |

      |

      |

 =========''', '''



  +---+

  |   |

  O   |

 /|\  |

 /    |

      |

=========''', '''



  +---+

  |   |

  O   |

 /|\  |

 / \  |

      |

=========''']


def start_game():
    print("\n")
    print("Hello player, welcome to Hangman game!")
    print("**************************************")
    print("Let's start a game!")
    print(f"Try to guess the word")
    print("**************************************")
    print(f"The word is from category: {drawn_category}")
    print(f"Your word has: {word_length} letters")
    print("\n")

def game():
    guesses_left = 6
    floor = "-" * word_length
    print(floor)
    print(hangman_pic[0])
    point = 0

    while guesses_left > 0 and floor != drawn_word:
        print("\n ")
        print(str(f"attempts: {guesses_left}"))
        letter = input("Give a letter: ")
        used_letters.append(letter)
        print(f"used letter: {used_letters}")




        if len(letter) != 1:
            print("You can enter only one character")
        elif letter.isalpha() != True:
            print("You entered a number, you should enter a character")
        elif letter in drawn_word:
            result = ""
            print("The letter is in the word!")
            for i in range(len(drawn_word)):
                if drawn_word[i] == letter:
                    result = result + letter
                else:
                    result = result + floor[i]
            floor = result
            print(result)
        else:
            print("The letter is not in the word!")
            point += 1
            guesses_left -= 1
            print(hangman_pic[point])


    if guesses_left <= 0:
        print(f"You lose! The word was: {drawn_word}")
    else:
        print(f"You won! The word was: {drawn_word}")


start_game()
game()
used_letters = ", ".join(used_letters)
print(f"used letters: {used_letters}")