import string
def main():
    myInput = input("Por favor introduzca una frase:\n")

    myInput = myInput.translate(str.maketrans('', '', string.punctuation))
    myInput = myInput.translate(str.maketrans('', '', "¿¡"))

    myInput = "".join(myInput.split())
    
    print("La salida es: {0}".format(myInput))

    #le damos la vuelta al string

    myInputReversed = myInput[::-1]

    print("La salida dada la vuelta es: {0}".format(myInputReversed))

    if(myInput.lower() == myInputReversed.lower()):
        print("palyndromes!!!!")
    else:
        print("not palyndromes!!")

if __name__ == "__main__":
    main()