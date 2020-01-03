import random
words = ["basketball", "soccer", "cheese", "code"]
secret_words =random.choice(words)
#The user only has 10 guesses
guesses = 10
#Ask a user to enter a letter as a guess

#This is what dashes is equal to the length of the secret word
dashes = "_" * len(secret_words)
print dashes
#Defined as get_guess and if the user enters more than one letter, it tells the user to enter only one letter.
#If the letter is uppercase, the condition, elif not user.islower tells the user that the letter must be lowercase
def get_guess():
    user = input("Enter Guess: ")
    if len(user) > 1:
        print"One letter only!"
    elif not user.islower():
        print"Letter must be lowercase!"

#I tried using update_dashes to show that the words and dashes and the
#guess could be defined in it. And I made a list to store the dashes
#I tried having the dashes join my list once the user entered a guess
#IT DID NOT WORK OUT :(
