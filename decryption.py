import pyAesCrypt
import os

# decryption functon
def decryption(file, password):

    # buffer size
    buffer_size = 512 * 1024

    # method for decryption
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # print the name of the decrypted file
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' decrypted]")

    # delete starting file
    os.remove(file)

# scanning function
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории checking all sub-directory in the given directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if the file is found than decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # if we find a directory, than repeat cycle in search of files
        else:
            walking_by_dirs(path, password)


password = input("enter decryption password: ")
walking_by_dirs("Path", password)
