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
    arr1,arr2 = openFile("data/day1_input.txt")

    arr1.sort()
    arr2.sort()

    # print("arr1 " + str(len(arr1)) + "\narr2 " + str(len(arr2)))

    i = 0
    total_multiplayer = 0
    while i < len(arr1):
        times_found = 0
        e = 0
        while e < len(arr2):
            if arr1[i] == arr2[e]:
                times_found += 1
            #print(
            #   "Checking if arr1 ("
            #   + str(arr1[i])
            #   + ") is same as arr2 ("
            #   + str(arr2[e])
            #   + ") times_found: "
            #   + str(times_found)
            #)
            e += 1
        #if times_found != 0:
            #print(times_found)
        total_multiplayer += times_found * arr1[i]

        i += 1

        # print(
        #    "Arr1: "
        #    + str(arr1[i - 1])
        #    + " Arr2: "
        #    + str(arr2[e - 1])
        #    + " times_found: "
        #    + str(times_found)
        # )

    return total_multiplayer


print("Total distance is " + str(main()))
