def make(height):
    for i in range(height , 0, -1):

        for x in range(height - i, height):
            print(" ", end='')

        for l in range(0, height - i + 1):
            print("#", end='')

        print("  ", end='')

        for a in range(0, height - i + 1):
            print("#", end='')

        print("\n", end='')

def start():

    condition = False

    while condition == False:
        try:
            Height = int(input("Enter The Height Of The Pyramid: "))
            if Height > 0 & Height <= 100:
                condition = True
                break
        except:
            print("\nError")

    make(Height)

start()
