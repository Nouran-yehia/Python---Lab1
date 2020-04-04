str1 = "Hello, this is Nouran from iti open source track"

count = 0
strsplited = list(str1)
for i in strsplited:
    if (i == "a" or i == "e" or i == "i" or i =="o" or i =="u"):
        count += 1
print "The vowels count = {}".format(count)

