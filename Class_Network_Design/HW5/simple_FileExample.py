
def fileExample():
    # Get input from user
    file_name = input("File name> ")

    try:
        # Open file -> read binary
        f = open(file_name, "rb")
        # print(f.read())

        # Create file -> write binary
        f2 = open("gfm_" + file_name, "wb")

        # Read and write File commands
        f2.write(f.read())

        # Close files
        f.close()
        f2.close()

    except FileNotFoundError as e:
        print(str(e))


if __name__ == "__main__":
    fileExample()
