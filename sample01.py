def main():

    f = open("users.text", mode="r")

    text = f.read()

    print(text)

    f.close()


if __name__ == "__main__":
    main()

