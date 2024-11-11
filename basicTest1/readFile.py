def main():

    with open("workfile_1.txt", "r") as myFile:
        lines = myFile.readlines()


    for line in lines:
        line = line.replace("\n","")
        print(line)

    print (lines)

if __name__ == "__main__":
    main()