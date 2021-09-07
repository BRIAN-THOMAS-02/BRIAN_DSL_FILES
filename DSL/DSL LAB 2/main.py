print("Group A Assignment No B2")
print("Menu Driver Program for FDS Test of 38 Marks Analysis")
print(" ")
marks = [' ', 22, 20, 12, 23, 24, 25, ' ', 22, ' ', 25, 28, 25, 25, 25, 25, ' ', 18, 26, 25, 12, 30,' ', 14, 13, 10, 8, 5, 2, 1, 0]
print("The Marks secured by the Student in FDS out of 30 Marks is :")
print(marks)

global m1
m1 = Marks_are_out_of = 30


def mainMenu():
    #print(" ")
    print("1. The Average score of class SEA")
    print("2. Highest score and Lowest score of class")
    print("3. Absent Students for the Test")
    print("4. Display Marks with Highest Frequency")
    print("5. Exit")
    print(" ")
    choice = int(input("Enter Choice: "))

    if (choice == 1):
        print("Average score of Class SE A is: ")
        avg_score()
        print(" ")

    elif (choice == 2):
        print("Highest Score & Lowest Score of Class")
        high_score()
        low_score()
        print(" ")

    elif (choice == 3):
        print("Absent Students for Test")
        print_absent_students()
        print(" ")

    elif (choice == 4):
        print("Marks with Highest Frequency")
        high_frequency()
        print(" ")

    elif (choice == 5):
        exit()

    else:
        print(" ")
        print("Wrong Choice")


def absent_students():
    global absent_count1
    global present_count1
    absent_count = 0
    present_count = 0
    for x in marks:
        if type(x) == type(" "):
            absent_count = absent_count + 1
        else:
            present_count = present_count + 1

    absent_count1 = absent_count
    present_count1 = present_count


def print_absent_students():
    print("Absent Students : ", absent_count1)
    print("Present Students : ", present_count1)


def total_marks():
    global total_marks1
    cnt = 0
    total_marks = 0
    for x in marks:
        if type(x) == type(" "):
            cnt = cnt + 1
        else:
            total_marks = total_marks + x
    total_marks1 = total_marks


def avg_score():
    avg = 0
    n = len(marks)
    print(" ")
    print("Total strength of class : ", n)
    print("Absent Students : ", absent_count1)
    print("Present Students :", n - absent_count1)
    print("Combined Marks of all Students : ", total_marks1)
    avg = total_marks1 / (n - absent_count1)
    print("Average Score of Class is: ", avg)


def high_score():
    absent_count = 0
    max = 0
    min = 30
    for x in marks:
        if type(x) == type(""):
            absent_count = absent_count + 1
        elif x > max:
            max = x

    print("Highest Score is : ", max)


def low_score():
    absent_count = 0
    min = 30
    for x in marks:
        if type(x) == type(""):
            absent_count = absent_count + 1
        elif x < min:
            min = x

    print("Lowest Score is : ", min)


def present_marks():
    temp4 = []
    present_marks = []
    for x7 in marks:
        if type(x7) == type(" "):
            temp4.append(x7)
        else:
            present_marks.append(x7)

    final_present_marks = []
    temp_tp = []
    for v in range(30):
        for i4 in present_marks:
            if (i4 == v):
                final_present_marks.append(i4)
            else:
                temp_tp.append(v)

    global result
    result = []
    for nn in final_present_marks:
        if nn not in result:
            result.append(nn)

    #print(" ")
    #print("Present Sorted Non-Repeating Marks are : ")
    global i5
    for i5 in result:
        print(" ")
        #print(i5, end=" , ")


def high_frequency():
    count = []
    p = high = mm = 0
    for n in range(m1):
        cnt = 0
        for x in marks:
            if type(x) == type(" "):
                p = p + 1
            elif x == n:
                cnt = cnt + 1
        count.append(cnt)

        count1 = []
        temp = []
        for c in count:
            if (c == 0):
                temp.append(c)
            else:
                count1.append(c)

    for y in count1:
        if y > high:
            high = y
    #print("Highest Frequency is of : ", high)
    for z in range(30):
        if count[z] == high:
            mm = z

    print("Marks are : ", marks)
    print("Sorted Non-Repeating Marks of Present Students are : ", result)
    print("Count of Marks are : ", count1)
    print("Recurrence of Marks : ")
    print("Marks", "\t", "Occurrence")
    for i9, x8 in zip(result, count1):
        print(i9, "\t", "  =", "\t", x8)

    print(" ")
    print("Marks with Highest Frequency is : ", mm)
    print("Highest Frequency is ", "    \t  ", " : ", high)

absent_students()
total_marks()
present_marks()
mainMenu()
