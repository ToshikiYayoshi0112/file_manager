def main():
    f = open("users.text", mode="r")

    text = f.read()

    lines = text.split("\n")

    # print(lines)

    for line in lines:
        info = line.split(",")
        name = info[0]
        age = info[1]
        print(f"{name}さんは{age}歳です。")

    f.close()


"""
Ken Tanakaさんは15最です。

"""
if __name__ == "__main__":
    main()
