string = raw_input("please enter your string to check the longest subString: ")
def longestOrderStr(str1):
    l = str1[0]
    c = str1[0]
    for i in str1[1:]:
        if i >= c[-1]:
            c += i
            if len(c) > len(l):
                l = c
        else:
            c = i
    print " The Longest concat of ordered substring is : {}".format(l)

longestOrderStr(string)