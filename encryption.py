import pyAesCrypt
import os


# encryption function
def encryption(file, password):

    # buffer size
    buffer_size = 512 * 1024

    # encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # print the name of the encrypted file, to see the result
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' encrypted]")

    # delete original file
    os.remove(file)

# scanning func 
def walking_by_dirs(dir, password):

    # check sub directories in the directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # encrypt file if it is found
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # repeat, if the directory is found to find files
        else:
            walking_by_dirs(path, password)


password = input("enter encryption password: ")
walking_by_dirs("Path", password)
