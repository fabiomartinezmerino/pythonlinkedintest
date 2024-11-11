def main():
    
    #simple, no try catch no error management
    myNumber = int(input("Type a score from 1 to 5:\n"))
    #print("The number is: {0:d}".format(myNumber))
    match myNumber:
        case 1 | 2:
            print("Score is poor: {0}\n".format(myNumber))
        case 3 | 4:
            print("Score is not bad: {0}\n".format(myNumber))
        case 5:
            print("Score is great: {0}\n".format(myNumber))
        case _:
            print("No matches")


if __name__ == "__main__":
    main()