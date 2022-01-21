from random import randint

l=list(input("Enter space seperated list of words : ").split())
allowed_errors=int(input("Enter number of guesses : "))
word = l[randint(0,len(l)-1)]
guesses = []

done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end= " ")
        else:
            print(" _ ", end = " ")
    print()

    guess = input(f"Remaining Attempts : {allowed_errors}, Next Guess : ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"\nYou Found The Word : {word}\n")
else:
    print(f"\nGame Over, The Word Was : {word}\n")