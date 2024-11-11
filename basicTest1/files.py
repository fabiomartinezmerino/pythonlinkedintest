def main():

    with open("workfile_1.txt", "w+") as myFile:
        controlVariable = True
        while controlVariable:
            textToWrite = input("Introduce frase, sólo enter para concluir:\n")
            if textToWrite != "":
                
                myFile.write(textToWrite)
                myFile.write("\n")
            else:
                controlVariable = False

if __name__ == "__main__":
    main()