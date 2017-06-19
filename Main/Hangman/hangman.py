from random import randint
import turtle

def generate():
    something = []
    with open('words.txt') as f:
        something = f.read().splitlines()
    print(len(something))
    return something[randint(0, len(something))]


def sort(word, n):
    this = list(word.lower())
    for x in range(0,n):
        for y in range(1, n):
            if ord(this[y]) < ord(this[y-1]):
                holder = this[y]
                this[y] = this[y-1]
                this[y-1] = holder
    return this

def search(s, c, n):
    if n < 0:
        return False
    min = 0;
    max = n - 1;
    while n > 0:
        half = (min+max)//2;
        if ord(c[half]) == ord(s):
            return True
        elif ord(c[half]) < ord(s):
            min = half+1
        else:
            max = half-1
        n = max - min + 1;
    return

array = []
arrayls = []
finished = False

def words(word, let):
    global arrayls
    global finished
    finished = True
    count = 0
    print("Found")
    count += 1
    arrayls.append(let)
    for letter in word:
        printed = False
        for i in arrayls:
            if letter.lower() == i.lower():
                print(letter, end='')
                printed = True
                break
        if printed == False:
            print("_", end = '')
            finished = False


def main():
    global finished
    wrong = 0
    word = generate()
    print(word)
    for i in range(0, len(word)):
        print('_', end='')
    sorte = sort(word, len(word))
    for s in range(0, len(word)):
        array.append(word[s].lower())
    while finished == False:
        let = input("\nInput the char: ")
        if search(let.lower(), sorte, len(word)) == True:
            words(word, let)
        else:
            wrong+=1
            if wrong == 3:
                print("Out of guesses")
                print("The word was %s" %(word))
                return 0
    if finished == True:
        print("\nCongratulations the word was %s" %(word))

if __name__ == "__main__":
    main()
