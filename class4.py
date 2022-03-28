# convert miles to kilometre
# miles =input("Enter the number\n")
# miles = int(miles)
# km = miles*(0.6)
# print(f"The convertion of {miles}m is {km}km")

# # convert naira to dollar
# dollars =input("Enter the amount\n")
# dollars = int(dollars)
# naira = dollars*(416.20)
# print(f"The convertion of {dollars}$ is {naira}₦")

# def print_twice(bruce,alex):
#     print(bruce)
#     print(alex)

# print_twice(alex='a')


# def minus(a,b):
#     print(a-b)

# minus(8,5)
# minus(5,8)
# minus(a=5,b=8)
# minus(b=8,a=5)

# a = ['A', 'quick', 'brown', 'fox', 'just', 'died.' ]
# b = " ".join(a)

# print(b.replace("brown","white"))

# arr = [1,2,3,4,5,6]
# mapped =map(lambda y : y**2, arr)
# print(list(mapped))

# def bring_up(a):
#     a.upper()

# a = ['x' , 'y' , 'z']
# mapped = map(bring_up,a)
# print(list(mapped))

# write a simple program that have a list of numbers then the 
# program should be able to find the average and the range

# qq = [1,2,3,4,5]
# avg = sum(qq)/len(qq)
# print (avg)

# rng = max(qq) - min(qq)
# print (rng)

# receive input from user that receive input from user and turn it to list

# receive = input("Enter number seperated by comma\n>")
# p = receive.split(',')
# print(p)
# # additional programme that convert my result to int
# c = list(map(int,p))
# print(c)

def add_num(a,b):
    return(a+b)
    print(a+b)

x = add_num(4,6)
print(x) 



# write a program that takes the scores of 
# the student as an input from the teacher sepearted by comma 

from math import sqrt

a = input("Enter the scores")
b = a.split(',')
print(b)
c = list(map(int,b))
print(c)
average = sum(c)/len(c)
print(average)

rng = max(c) - min(c)
print (rng)

d = map(lambda x: (x-average)**2, c)
sd = sqrt(sum(d)/len(c))
print(sd)

v = sd**2
print(v)

# x = input("Enter your age")
# x = int(x)
# y = 2022 - x
# print(f"You were born in {y}") 

