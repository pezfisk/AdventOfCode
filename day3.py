def main():
    file = open("data/day3_test.txt", 'r')
    data = file.read()
    print(data)

    i = 0
    while i < len(data) - 3:
        test_string = data[i] + data[i + 1] + data[i + 2] + data[i + 3]

        if test_string == "mul(":
            parCheck = 0
            while parCheck < 9:
                if test_string[i + parCheck] == ")":
                    print("mul found")

                parCheck += 1

        i += 1


main()
