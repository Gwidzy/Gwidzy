import random
import time
import string

alpha_stringL = string.ascii_lowercase
alpha_stringU = string.ascii_uppercase
space = ' '

alpha = list(alpha_stringL) + list(alpha_stringU) + list(space)

solution = 'passWordTEST'
start = ''
holder = ''
i = 0

print("Welcome!")

while start != solution:
    holder = random.choice(alpha)
    if holder != solution[i]:
        alpha.remove(holder)
        print(start + holder)
        time.sleep(.05)
    else:
        alpha = list(alpha_stringL) + list(alpha_stringU) + list(space)
        start += holder
        print(start)
        i += 1
        time.sleep(.05)

if start == solution:
    print("SUCCESS!")
else:
    print("FAILURE!")

# import random
# import time
# import unicodedata

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',':',' ']

# solution = 'The quick'
# start = ''
# holder = ''
# i = 0

# print("Welcome!")

# while start != solution:
    # holder = random.choice(alphabet)
    # if holder != solution[i]:
        # alphabet.remove(holder)
        # print(start + holder)
        # time.sleep(.05)
    # else:
        # alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',':',' ']
        # start += holder
        # print(start)
        # i += 1
        # time.sleep(.05)

# if start == solution:
    # print("SUCCESS!")
# else:
    # print("FAILURE!")
