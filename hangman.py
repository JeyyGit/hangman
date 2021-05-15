import random

def conv(string):
    list1 = []
    list1[:0] = string
    return list1

def hang():
    if wrong == 0:
        print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n")
    if wrong == 1:
        print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========= You have 5 lives left.\n")
    if wrong == 2:
        print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========= You have 4 lives left.\n")
    if wrong == 3:
        print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========= You have 3 lives left.\n")
    if wrong == 4:
        print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n========= You have 2 lives left.\n")
    if wrong == 5:
        print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n========= You have 1 live left.\n")
    if wrong == 6:
        print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n")

print("HANGMAN GAME BY JEYY\n")

#word = input("Input the word: ")
#words = conv(word.upper())
animal = ["cat",
          "dog",
          "donkey",
          "goat",
          "pig",
          "horse",
          "rabbit",
          "sheep",
          "chicken",
          "fish",
          "duck",
          "ant",
          "baboon",
          "monkey",
          "crab",
          "bat",
          "bear",
          "bird",
          "whale",
          "camel",
          "kangaroo",
          "cow",
          "crocodile",
          "deer",
          "lion",
          "elephant",
          "frog",
          "fox",
          "fly",
          "gorilla"]


wordd = random.choice(animal)
words = conv(wordd.upper())

wrong = 0
ans = ["_"] * len(words)
print(",".join(ans))


while ans != words and wrong != 6:
    guess = input("Guess a letter: ")
    guess = guess.upper()
    if words.count(guess) > 0 and ans.count(guess) < words.count(guess):
        boo = [i for i, x in enumerate(words) if x == guess]
        for idx in boo:
            ans[idx] = guess
        print(",".join(ans))
        print("Right choice! There (is/are) " + str(words.count(guess)) + " '" + guess + "' letter(s).\n")
        hang()
    else:
        wrong += 1
        print(",".join(ans))
        hang()
        print("Wrong choice! There is none '" + guess + "' letter.\n")


if ans == words:
    print("Congratulations! You've won the game!")
if wrong == 6:
    print("You're dead.\nThe right answer is " + ",".join(words))
