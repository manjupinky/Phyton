vowel=['a','e','i','o','u','A','E','I','O','U']
str=list(input("Enter the string"))
def vw(str):
    for i in vowel:
        if i in str:
            return "yes"
    return "no"
print(vw(str))
