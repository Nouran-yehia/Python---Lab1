def countIti ():
    count = 0
    str1 = raw_input("please enter your string to count iti string : ")
    splited = str1.split(" ")
    for i in splited:
        if i == "iti":
            count += 1
    print(count)
countIti()