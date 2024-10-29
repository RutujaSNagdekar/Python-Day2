

single_quote = 'single quote'
double_quote ="double quote"
triple_quote ='''triple quote'''
print (type(single_quote))
print (type(double_quote))
print(double_quote)
print(triple_quote)

e_seq = 'hi weather is \'good\' have a good \nday!!'
print(e_seq)

#String Operations
str1= 'quick brown fox'
str2= 'jumps over lazy dog'

#Concatenation
result= str1+str2
print('Concatenated String ', result)

#Repetation

repeat = result*3
print("Repeated Sring\n", repeat)

#Length of String
print("Length of String",len(result))

#Strip
str3 = "   abcde " + "  "
print(str3)

print(len(str3))

stripped_str= str3.strip()
print("Stripped String", stripped_str)
print("Length of Stripped", len(stripped_str))


text = "    sdjsdjs   *****"
lstrip = text.lstrip()
print("LEft Stripped", lstrip)


text = "    sdjsdjs   *****"
rstrip = text.rstrip('*')
print("Right Stripped", rstrip)

stripeeedd = text.strip(' *')
print("Striiped Both", stripeeedd)

#Find and Replace

ress = result + 'abc' + 'abc' + 'abc'
print(ress)

position = ress.find('abc')
print(position)

new_str = ress.replace('abc', "ABC", 2)
print(new_str)

#string comparision
res4="hello world"
res5="hello world"
resultcomp=res4==res5
print(resultcomp)


#case conversion
result="ABCabc"
print(result.lower())
print(result.upper())
print(result.title())

#
resulta="ABCDEFGH"
##indexing

firstchar= resulta[0]
lastchar =resulta[-1]
secondchar =resulta [1]

print(firstchar)
print(lastchar)
print(secondchar)

#Slicing

print(resulta)
substring =resulta[0:4]
print(substring)
substring =resulta[:4]
print(substring)
substring=resulta[4:]
print(substring)
substring=resulta[:]
print(substring)
substring=resulta[::-1]
print(substring)


#spliting
resconcat="abcd"+','+"efgh"
print(resconcat)
print(type(resconcat))
ressplit=resconcat.split(",")
print(type(ressplit))
print(ressplit)

#######################
str='start'
str=sorted(str)
str2='restart'
str2=sorted(str2)
print(str,"\n",str2)

#joining

fruit=['apple','banana','strawberry']
result=", ".join(fruit)
print(result)


# Palindrome of String
string1 = input("Enter first String ")


for i in range(len(string1)//2):
    if string1[i] != string1[len(string1)-1-i]:
        print('No')
        break
else:
    print("Yes")

#Anagrams

string3 = input("Enter first String ")
string4 = input("Enter first String ")

string5= string3.strip().lower()
string6 = string4.strip().lower()

if sorted(string5)==sorted(string6):
    print("Anagram it is ")
else:
    print("Not Anagram")


#List







