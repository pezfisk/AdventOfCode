def main():
    file = open("data/day3_input.txt", "r")
    data = file.read()
    # print(data)

    totalMultiplication = 0

    i = 0
    while i < len(data) - 3:
        test_string = data[i] + data[i + 1] + data[i + 2] + data[i + 3]

        if test_string == "mul(":
            parCheck = 0
            print("\n")
            while parCheck < 9:
                print(data[i + parCheck + 3])
                if data[i + parCheck + 3] == ")":
                    print("mul found")
                    print(parCheck)

                    mulString = ""
                    mulArray = []

                    e = 0
                    while e < parCheck - 1:
                        mulString += str(data[i + parCheck - e + 2])
                        e += 1

                    charIndex = mulString.find(",")
                    print(charIndex)
                    if charIndex != -1:
                        print("Valid mult found")
                        mulArray = mulString[::-1].split(",")
                        print(mulString)
                        print(mulArray)

                        totalMultiplication += int(mulArray[0]) * int(mulArray[1])

                    parCheck = 10

                parCheck += 1

        i += 1

    return totalMultiplication


print(main())
