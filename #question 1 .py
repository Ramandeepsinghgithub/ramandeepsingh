#Q1
string1="Python is a case sensitive language" #string1
print("<A>the length of string is",len(string1))#function to find length of string
print("<B>the reversed string is",string1[-1::-1])
string2=string1[10:26]#stored a case sensitive in a new string
string2.replace("a case sensitive","object oriented") #replaced "a casesensitive" with "object oriented"
print("<E>the index of substring a is",string1.find('a'))
print("<F>the original string after reoving whitespaces is",string1.replace(" ",""))
print("\n")
