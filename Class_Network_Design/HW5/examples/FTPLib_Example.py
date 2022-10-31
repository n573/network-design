import ftplib


def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except Exception as e:
        print(str(e))


def main():

    try:
        ftp = ftplib.FTP("ftp.nluug.nl")
        ftp.login("anonymous", "ftplib-example-1")
        ftp.dir()

        input()
        ftp.cwd("/pub/")
        ftp.dir()

        input()
        getFile(ftp, 'README.nluug')
        ftp.quit()

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
