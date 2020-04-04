def countIti ():
    count = 0
    str1 = "iti is the place for learning, joining iti will enhance your skills, in iti you will learn new things, iti is the best"
    splited = str1.split(" ")
    for i in splited:
        if i == "iti":
            count += 1
    print(count)
countIti()