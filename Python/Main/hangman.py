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

def main():
    word = input("Please input a word for: ")
    sorte = sort(word, len(word))
    wrong = 0
    let = input("Input the char: ")
    if search(let, sorte, len(word)) == True:
        print("Found")
        for letter in word:
            if letter.lower() == let.lower():
                print(letter, end='')
            else:
                print("_", end='')
    else:
        wrong+=1
        if wrong == 3:
            print("Out of guesses")
            print("The word was %s" %(word))
            return 0

main()
