import os

directory = "C:\\Users\\bengr\\Google Drive\\Curated Dogs"
os.chdir(directory)
iterater = 0
for filename in os.listdir(directory):
    print(filename)
    os.renames(filename, str(iterater) + ".jpeg")
    iterater = iterater + 1
