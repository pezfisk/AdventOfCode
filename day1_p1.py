def openFile(filePath):
    file = open(filePath, "r")

    array1 = []
    array2 = []

    while True:
        content = file.readline()

        if not content:
            break

        number = [int(num) for num in content.split()]
        # print(number)

        array1.append(number[0])
        array2.append(number[1])

    file.close()

    return array1, array2


def main():
    print("Hello world!")
    arr1 = openFile("day1_input.txt")[0]
    arr2 = openFile("day1_input.txt")[1]

    arr1.sort()
    arr2.sort()

    # print("arr1 " + str(len(arr1)) + "\narr2 " + str(len(arr2)))

    i = 0
    total_distance = 0
    while i < len(arr1):
        distance = arr1[i] - arr2[i]

        total_distance += abs(distance)

        i += 1

    return total_distance


print("Total distance is " + str(main()))

