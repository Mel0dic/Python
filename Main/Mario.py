def make(height):
    for i in range(height, 0, -1):

        for x in range(height - i, height):
            print(" ", end='')

        for l in range(0, height - i):
            print("#", end='')

        print(" ", end='')

        for a in range(0, height - i):
            print("#", end='')

        print("\n")

make(int(input("Enter The Height Of The Pyramid: ")))
