def main():
    data = open("data/day2_test.txt", "r")
    
    safeReports = 0

    for line in data:
        currentLine = line.strip()

        cutLine = currentLine.split(" ")
        #print(cutLine)
        
        i = 0
        steps = []

        while i < len(cutLine):
            e = i
            i += 1

            if i < len(cutLine):
                step = int(cutLine[e]) - int(cutLine[i])

                if abs(step) < 4 and step != 0:
                    steps.append(step)
                else:
                    i = 99
                    steps.clear()
        
        
        if len(steps) == 0:
            steps = extraSafety(cutLine)

        print(steps)

        if len(steps) > 0:
            if steps[0] > 0:
                positive = True
            else:
                positive = False
    
            okChecks = 0
            for num in steps:
                if (num > 0) == positive:
                    okChecks += 1
            
            if okChecks == len(steps):
                safeReports += 1
                print("Safe!")

    print("There are " + str(safeReports) + " safe reports")
    data.close()

def extraSafety(cutLine):
    print(cutLine)
    i = 0
    steps = []
    while i < len(cutLine) - 1:
        cutLineCopy = cutLine
        cutLineCopy.pop(i)
        print(cutLineCopy)
        e = 0
        i += 1
        while e < len(cutLineCopy):
            step = int(cutLineCopy[e]) - int(cutLineCopy[i])

            if abs(step) < 4 and step != 0:
                steps.append(step)
                print("Valid step")
                e += 1
            else:
                steps.clear()
                print("Not valid step")
                e = 99
                
    return steps

main()
