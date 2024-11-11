import os


def main():
    print("Warming up")
    directories = os.scandir()
    
    print ("Lista de directorios: {0}\n".format(directories))
    for directory in directories:
        if directory.is_dir():
            print("Directory name: {0}\n".format(directory))
        else:
            continue
            #print("File name: {0}\n".format(directory))
        if directory.name == "testfolder":
            print("Estoy en el directorio!!!!! - {0}\n".format(directory.name))
            files = os.scandir(directory.name)
            sizeOfFiles = 0
            for file in files:
                sizeOfFiles += file.stat().st_size
            


            directories.close()

            print("El tamaño acumulado de los ficheros es de : {0} Bytes\n".format(sizeOfFiles))
            break

if __name__ == "__main__":
    main()