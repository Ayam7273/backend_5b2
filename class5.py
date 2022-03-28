# def slugify(word):
#     return word.replace("","-").lower()

# print(slugify('How to dance'))    


# firststring = input("Enter the first word\n")
# secondstring = input("Enter the last word\n")

# x = firststring[:2]
# y = secondstring[-2:]

# def first_last(x,y):
#     return(x+y)

# print(f"The combination of the first and last two characters from the string is {first_last(x, y)}")

# a = lambda x : x+15
# print(a(20))

# hello = lambda a,b : a*b
# print(hello(20,30))
# # "".


# anything = lambda string : string.swapcase()
# print(anything("FUCK YOU"))

# a = input("Enter your file name please\n")
# print(a.split(".")[-1])



# def factorial():
#     return()

# a = [2,3,4,5,6]

# trippled = list(map(lambda x : 3*x, a))
# squared = list(map(lambda x : x**2, a))

# print(trippled)
# print(squared)

# a = []
# a = type(a)
# print(a)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(my_list[3])

# # list = [0:7:1]

# list[3] = 10
# print(list)

# u = [2,4,6,8,10]
# w = [1,3,5,7,9]

# print(u+w)

# x = [2,3,4,2,[2,3,4,5,[4,52,2],5],24]
# print(x[4][4][1] + x[-1])

# my_list = [13,24,6,8,3,9,10]
# my_list.sort()
# print(my_list[0])
# print(my_list[-1])
# print(f"The lowest three values are; {my_list[0:3]}")
# print(f"The highest three values are; {my_list[-3:]}")

# def largest(arr:list, k:int):
#     """ This function returns  
#     the highest K values in an array: arr."""


#     arr.sort(reverse=True)
#     return arr[:k]


# def smallest(arr:list, k:int):
#     """ This function returns  
#     the highest K values in an array: arr."""


#     arr.sort()
#     return arr[:k]


# print(largest([1,1,1,0,0,0,-2,-2],2))

# def unknown_fact():
#     return('READERS ARE LEADERS')

# print(unknown_fact().swapcase())


# a = input("Enter the scores")
# b = a.split(',')
# print(b)
# c = list(map(int,b))
# print(c)
# average = sum(c)/len(c)
# print(average)

# rng = max(c) - min(c)
# print (rng)

# d = map(lambda x: (x-average)**2, c)
# sd = sqrt(sum(d)/len(c))
# print(sd)

# v = sd**2
# print(v)

fruit = 'banana'
# print(len(fruit))

length = len(fruit)
# # last = fruit[length]
# # print(last)

# # correct thing
last = fruit[1:4]
print(last)