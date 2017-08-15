file = open("words1.txt", "r")

print(len(file.readlines()[0].split()))

file.close()

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("words1.txt"))