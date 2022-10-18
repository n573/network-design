import os
import ftplib


# Read and Write files example
def fileExample():
    # get input from user
    file_name = input("File name>")

    try:
        # open file ... rb = read bytes
        f = open(file_name, "rb")
        # print(f.read())

        f2 = open("ncc_" + file_name, "wb")

        f2.write(f.read())  # passes bytes of f to f2

        f.close()
        f2.close()

    except FileNotFoundError as e:
        print(str(e))


def getCurrentDir():
    path = os.getcwd()
    print(path)


def runShellCmd():
    # Option 1
    # os.system("dir")

    # option 2
    list_files = os.popen("dir")
    print(list_files.read())

def listFiles():
    # get current dir
    path = os.getcwd()

    # list all files in current dir
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)

def ftplib_example():
    try:
        ftp = ftplib.FTP("ftp.nluug.nl")
        ftp.login("anonymous","ftplib-example-1")

        ftp.cwd("/pub/")
        ftp.dir()

        file_name = 'robots.txt'
        ftp.retrbinary("RETR " + file_name, open(file_name, 'wb').write)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    # Read/Write Examples

    # fileExample()
    # getCurrentDir()
    # runShellCmd()
    # listFiles()

    # FTP examples
    ftplib_example()