#se trata de dividir dos números que introduce el usuario
#se trata de controlar la división / 0 y el hecho de que se introduzca algo que no se puede pasar a número
import logging
def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.ERROR)
    try:
        numerator = int (input("Introduce numerador: "))
        denominator = int (input("Introduce denominator:"))

        print("El resultado es {:.4f}: ".format(numerator/denominator))
    except ValueError as ve:

        logger.error(ve)

    except ZeroDivisionError as div_by0:
    
        logger.error(div_by0)
        

    
    finally:
        print("The end!!!")
        SystemExit()
        


if __name__ == "__main__":
    main()
