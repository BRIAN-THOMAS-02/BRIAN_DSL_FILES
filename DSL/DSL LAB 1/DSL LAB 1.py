"""class_SEA = ["DEVANG", "KUNAL", "ATHARVA", "ANSHU", "SAYYED", "TANISHQ", "JOSHI", "PARTH", "BRIAN", "SAHIL"]
print("Total Student sin SE C class are...", class_SEA)

cricket = ["KUNAL", "ANSHU", "TANISHQ", "PARTH" ]
print("Students who play Cricket = ", cricket)

badminton = ["ATHARVA", "SAYYED", "TANISHQ", "PARTH"]
print("Students who play Badminton", badminton)

football = ["DEVANG", "JOSHI"]
print("Students who play Football", football)

# creating empty lists
common = []
only_Cricket = []
only_Badminton = []
Cricket_Badminton = []
play_neither_Cricket_nor_Badminton = []
Cricket_Football = []
Cricket_Football_not_Badminton = []


def mainMenu():
    print(" ")
    print("1. List of common Students who play both Cricket and Badminton")
    print("2. List of Students who play either Cricket or Badminton not both")
    print("3. List of Students who play neither Cricket or Badminton")
    print("4. List of Students who play Cricket and Football but not Badminton")
    print("5. Exit")

    print(" ")
    choice = int(input("Enter Your Choice: "))

    if (choice == 1):
        print(" ")
        play_both_Cricket_and_Badminton()
    elif (choice == 2):
        print(" ")
        either_Cricket_or_Badminton()
    elif (choice == 3):
        print(" ")
        neither_Cricket_nor_Badminton()
    elif (choice == 4):
        print(" ")
        play_Cricket_Football_not_Badminton()
    elif (choice == 5):
        exit()
    else:
        print("Enter Valid Number")


def play_both_Cricket_and_Badminton():
    for num in cricket:
        for n1 in badminton:
            if num == n1:
                common.append(num)
    print("List of common Students who play both Cricket and Badminton are : ", common)


def either_Cricket_or_Badminton():
    for num in cricket:
        flag = 0
        for n1 in badminton:
            if (num == n1):
                flag = 1
        if flag == 0:
            only_Cricket.append(num)
    print("List of Students who play only Cricket are : ", only_Cricket)

    for num in badminton:
        flag = 0
        for n1 in cricket:
            if (num == n1):
                flag = 1
        if (flag == 0):
            only_Badminton.append(num)
    print(" ")
    print("List of Students who play only Badminton are : ", only_Badminton)


def neither_Cricket_nor_Badminton():
    for num in cricket:
        Cricket_Badminton.append(num)
    for no in badminton:
        flag = 0
        for n1 in Cricket_Badminton:
            if no == n1:
                flag = 1
        if flag == 0:
            Cricket_Badminton.append(no)
    print("List of Students who play both Cricket and Badminton are :", Cricket_Badminton)

    for num in class_SEA:
        flag = 0
        for n1 in Cricket_Badminton:
            if num == n1:
                flag = 1
        if flag == 0:
            play_neither_Cricket_nor_Badminton.append(num)
    print(" ")
    print("List of Students who play neither Badminton nor Cricket are : ", play_neither_Cricket_nor_Badminton)


def play_Cricket_Football_not_Badminton():
    for num in cricket:
        Cricket_Football.append(num)
    for no in football:
        flag = 0
        for n1 in Cricket_Football:
            if no == n1:
                flag = 1
        if flag == 0:
            Cricket_Football.append(no)
    print("List of Students who play Cricket and Football ", Cricket_Football)

    for num in Cricket_Football:
        flag = 0
        for no in badminton:
            if no == num:
                flag = 1
        if flag == 0:
            Cricket_Football_not_Badminton.append(num)
    print("")
    print("List of Student who play Cricket and Football but not Badminton", Cricket_Football_not_Badminton)

mainMenu()"""

marks = ['Brian', 25]
