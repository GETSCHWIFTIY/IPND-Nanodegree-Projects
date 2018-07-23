# This is a quiz handed in for the Intro in Programming Nanodegree at Udacity by Eva in May 2018.
# It should show the newly acquired python skills of the programmer in-charge-of.
# To play the game on a Mac please save the file on your Desktop as QuizEva.py, open your Terminal, command to Desktop
# and python QuizEva.py.
# Start gaming and have fun!

# A list of replacement blanks to be filled in into the play game function.
blanks = ["--1--", "--2--", "--3--", "--4--", "--5--"]
# Easy level text and answers.
easy_quiz_string = "The European Union is a Union of several --1--. In 2018 --2-- countries will be part of it. The headquarter, the European Comission is located in --3-- and in --4--. The EU flag is blue with 28 --5-- stars, representing the countries."
answers_easy_quiz_string = ["countries", "28", "Brussels", "Strasbourge", "yellow"]

# Middle level text and answers.
middle_quiz_string = "The European Union is a Union of --1-- member states. It was founded in --2--. More than --3-- official languages are spoken in the different member states. The flag colors are --4-- and --5--."
answers_middle_quiz_string = ["28", "1958", "24", "blue", "yellow"]

# Hard level text and answers.
hard_quiz_string = "The European Union is a Union of --1-- member states. The aim of the European Union policies is to ensure free movement of --2--, with most of the citizen requiring now visa travelling from one country to another. Free movement of --3--, to boost the economy and free movement of  --4--, supported by the European Central Bank. The estimated population is over 510 --5--. "
answers_hard_quiz_string = ["28", "people", "goods", "capital", "million"]

# Welcome-part
print "Hello and welcome to Eva's quiz!"

# In the first section the user should choose one of the difficulty levels: easy, medium and hard.

def choose_level():
    """ raw input defines level and output is the particular string & solution
  based on the chosen level"""
    level = raw_input("Please choose a difficulty level. You can type in easy, middle or hard.\n\n")
    print "You choose: " + level
    if level == "easy":
        quiz_string = easy_quiz_string
        answers_quiz_string = answers_easy_quiz_string
    elif level == "middle":
        quiz_string = middle_quiz_string
        answers_quiz_string = answers_middle_quiz_string
    elif level == "hard":
        quiz_string = hard_quiz_string
        answers_quiz_string = answers_hard_quiz_string
    else:
        print "Please start all over again and choose a level easy, middle and hard."
    print  "\n You will get 5 tries to answer each question.\n"+ quiz_string
    return quiz_string, answers_quiz_string




# Checks if a word in blanks is a substring of the word filled in, it's checked if it's a blank.
def word_in_blanks(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

# This function checks if there is a blank element and replaces it.
def replace_blank(quiz_string, user_input):
    """ replaces blank elements with the user_input """
    replaced = []
    quiz_string = quiz_string.split()
    for word in quiz_string:
        replacement = word_in_blanks(word, blanks)
        if replacement != None:
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print replaced
    return replaced
# This function plays the game, displaying the quiz questions related to the blanks found to the user in the easy level.

def play_game(quiz_string, answers_quiz_string):
    count_answers = 0
    max_tries = 4
    count_blanks = 0
    max_blanks = len(answers_quiz_string)
    while count_answers < max_tries and count_blanks < max_blanks:
        user_input = raw_input("\n" "What should be filled in for " + blanks[count_blanks] + "?")
        for word in quiz_string:
            if user_input == answers_quiz_string[count_blanks]:
                print "Congratulations, that's correct!"
                correct_answer = replace_blank(quiz_string,user_input)
                count_blanks += 1
                count_answers += 1
                break
            else:
                print "Not quite. Try again. You have" + str[max_tries - count_answers] + "tries left. Good luck!"
                count_answers += 1
                break
        else: print "Sorry. Game over!"
quiz_string, answers_quiz_string = choose_level()
play_game(quiz_string, answers_quiz_string)
