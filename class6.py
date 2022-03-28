# y = ['A','b','c','d']
# print(list(filter(lambda x:x.isupper() ,y)))

# a = input('Enter your set of numbers\n')
# b = a.split(',')
# c = map(int,b)
# print(list(filter(lambda a:(a%2) == 1, c)))

# a = "banana"
# b = "banana"

# print(a==b)
# print(a is b)

# a = [1,2,3,4,5,6]
# b = [1,2,3,4,5,6]

# print(a==b)
# print(a is b)

# a = [4,7,9]
# b = a
# c = a.copy()

# print(b is a)
# print(c is a)


# t = [1,2,3,4,5,6]

# def mid_dle():
#     return(t[1:5])
#     print(t[1:5])
  

# print(mid_dle())

# def mid_dle(arr):
#     return arr[1:-1]
  
# a = [1,2,3,4,5,6]

# print(mid_dle(a))


# def median(arr):
#     arr.sort()
#     mid_point = len(arr)//2
#     if len(arr)%2==0:
#         return (arr[mid_point] + arr
#         [mid_point-1])/2

#     return arr[mid_point]    

# z = [1,2,3,4,5,6,7,8,9]
  
# print(median(z))

# salary = 10000
# if salary >= 100000:
#   print('I feel good')  
# else:
#     print('Fuck you i will find a better job jerk..')

# # CHAINED CONDITIONS
# print = input('What did you score>>\n')
# score = int(input('>'))
# if score <= 39:
#    print("F")
# elif score <= 49:
#     print("E")
# elif score <= 59:
#     print("D")    
# elif score <= 69:
#     print("C")
# elif score <= 79:
#     print("B")   
# elif score <= 100:
#     if score <= 100:
#         print("A")


import random

## DICE DICE DICE.....
a = [3,2,5,6,1,4]

# print(f"select any number from {a}.\nWe hope it doesn't end in tears.")
# while True:
#     com_choice = random.choice(a)
#     random.shuffle(a)
#     print("Guess the number:")
#     user_choice = int(input(">"))

#     if user_choice in a:
#         if user_choice == com_choice:
#             print("All power belong to you comrade.")
#         else:
#             print("Arhhh, comrade e be like say u go try again o.")
#     else:
#         print("Comrade no be so!") 
#     print(f'Do you wanna give it another trial?')  
#     c = input('continue?\n>')
#     if c == 'y':
#         continue
#     else:
#         break

print(f"select any number from {a}.\nWe hope it doesn't end in tears.")
def roll_dice():
    com_choice = random.choice(a)
    random.shuffle(a)
    print("Guess the number:")
    user_choice = int(input(">"))

    if user_choice in a:
        if user_choice == com_choice:
            print("All power belong to you comrade.")
        else:
            print("Arhhh, comrade e be like say u go try again o.")
    else:
        print("Comrade no be so!") 

while True: 

    roll_dice()
    c = input('Do you wanna give another trial?\n>')
    if c == 'y':
     continue
    else:
     break


## SEARCH ENGINE
# text = '''I am a very good boy a unit of language, consisting of one or more spoken sounds or their written representation, that functions as a principal carrier of meaning. Words are composed of one or more morphemes and are either the smallest units susceptible of independent use or consist of two or three such units combined under certain linking conditions, as with the loss of primary accent that distinguishes the one-word blackbird '''
# sub_text = input("Enter text to search for:\n>").lower()

# lowercase_text = text.lower()
# found = lowercase_text.find(sub_text)
# count = lowercase_text.count(sub_text)

# if found != -1:
#     print(f"{count} results(s) found!")
#     new_text = text.replace(sub_text,sub_text.upper())
#     print(new_text)
# else:
#     print(f"{count} result(s) found!")   

## ASSIGNMENT