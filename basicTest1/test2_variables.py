def main():
    #boolean
    myTest = True
    print(str(myTest) + " Es de tipo: " + str(type(myTest)))

    #list
    myListOfNumbers = [1,2,3,4,5,6,7,8,9,10]

    for index, number in enumerate(myListOfNumbers):
        print ("El indice es {0:d} \ny el valor es {1:d}".format(index, number))

    #dictionary
    myDictionary = {"Alicia": 49, "Fabio": 51}

    for key,value in (myDictionary.items()):
        print (("La clave es {0}\nEl valor es {1}".format(key, value)))


if __name__ == "__main__":
    main()