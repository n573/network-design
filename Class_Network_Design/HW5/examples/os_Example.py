import os


def getCurrentDirectory():
    # Get current directory
    path = os.getcwd()
    print(path)


def listFiles():
    # Get current directory
    path = os.getcwd()
    # List all files in current directory
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)


# Run shell commands
# ******************************
def runShellCommands():
    # Option 1
    os.system("dir")

    # Option 2
    list_files = os.popen("dir")
    print(list_files.read())


if __name__ == "__main__":
    getCurrentDirectory()
    runShellCommands()
    listFiles()
