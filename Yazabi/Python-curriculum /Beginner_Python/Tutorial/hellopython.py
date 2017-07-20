import random
import sys
import os


colors = ['red', 'blue', 'green', 'black', 'sushi']
print(colors[1:4])

print("number of colors=",len(colors))

j=0
while j < len(colors):
    print(colors[j])
    j = j + 1

for i in range(3):
    print(colors[i])

squares = [1, 4, 9, 16]
print(squares[0])
sum = 0
for num in squares:
    sum+=num
    print("num=",num,"sum=",sum)
print("sum=",sum)
print("--------------------")

grocery_list=["Juice", "Tomates", "Bananas", "Chips", "Bread"]
print("First item=",grocery_list[0])
grocery_list[0]="Green Juice"
print("First item=",grocery_list[0])
print(grocery_list[1:4])

other_events=["Wash Cars", "Feed The Cats", "Do Grocery"]
to_do_list = [other_events, grocery_list]
print(("to_do_list[0][3]=",to_do_list[1][3])) #third item out of the first list
grocery_list.insert(0,"Onions") #add an item in a very specific place, first place there
print(grocery_list[0:6])
grocery_list.append("Apple") #add an item at the end of the list
grocery_list.sort()
grocery_list.remove("Bread")
del grocery_list[3]
print(grocery_list[0:7])
print(to_do_list[0:3])
to_do_list2= other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

print("--------------------")

pi_tuple = (3,1,4,1,5,9)
print(pi_tuple[0:6])
new_tuple = list(pi_tuple)



print(len(pi_tuple),"len")
print(max(pi_tuple),"max")
print(min(pi_tuple),"min")



list = ['a', 'b', 'c', 'd']
print (list[1:-1])  ## ['b', 'c']
list[0:2] = 'z'  ## replace ['a', 'b'] with ['z']
print(list)  ## ['z', 'c', 'd']

print("--------------------")


super_villans = {"Fiddler":"Bowin", "Cold":"Leo", "Pied":"Tom"} # est un dictionnaire "key":"value"

print(super_villans["Cold"]) #Id of Cold
del super_villans["Fiddler"] #to delede Fiddler
print(super_villans)
super_villans["Pied"]="Rat" #replace an ID by another one
print(super_villans)
print(len(super_villans))
print(super_villans.get("Pied"),"=key or value of Pied")
print(super_villans.keys())
print(super_villans.values())


print("--------------------Conditions")

age=21
if age > 16:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")
if age >=21:
    print("You are old enough to drink alcool")
else:
    print("You are not old enough to drink alcool")

#below: once a condition is met we no longer check the other conditions
if((age >= 1) and (age <=18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not (age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday yeah")

print("--------------------Loop")

for x in range(0,10):
    print(x,"",end="")

print("\n")

grocery_list=["Juice", "Tomates", "Bananas", "Chips", "Bread"]

for y in grocery_list:
    print(y)
for x in [2,4,6,8,10]:
    print(x)

num_list=[[1,2,3,4],[10,20,30,40],[100,200,330,400]]
for x in range(0,3):
    for y in range(0,4):
        print(num_list[x][y])

print("\n")
random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

print("\n")
print("while used like a for")
#while used like a for:
i = 0
while (i <=20):
    if (i%2 ==0):
        print(i,"=even i")
    elif( i ==9):
        break
    else:
        i = i+1
        continue

    i = i+1


print("\n")

#Le nombre 7 est premier car il admet exactement deux diviseurs positifs distincts: 1 et 7

#7/3 ! = 7 donc x est un nombre entier si x/z != x (Z!=x et Z != 1)

print("--------------------Functions")
N=[1,2,3,4,5,6]#,5,6,7,8,9,10,11,12,13,14,15]



print("N=",N)
for x in N:
        for y in N:
            if  (x/y == x):
                print("x=", x, "y=",y)
        y = y + 1

print("\n\n")
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res=res*i
    return res

print(factorial(3),"=3!")
print(factorial(5),"=5!")
print("\n\n")


print("\n\n")
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(3,5),"=max")

print("\n\n")

def addNumber(fNum,lNum):
    sumNum = fNum + lNum
    return sumNum

string = addNumber(1,4)#to call the function

print(addNumber(1,4))

# if you want to use the variable outside of the function:
#print("What is your name")
#name = sys.stdin.readline()
#print("Hello", name)

print("\n\n")

long_string = "i'll catch you if you fall - the Floor"
print(long_string[0:4],"=0 a 4")
print(long_string[-5:],"=-5:")
print(long_string[:-5],"=:-5")
print(long_string[:4]+" be there")
print("%c is my %s letter and my number %d number is %.5f"%("X","favorite",1,.14)) #.5f is 5 digits after .
print(long_string.capitalize(),"=capitalise")
print(long_string.find("Floor"),"=find")
print(long_string.isalpha(),"=alpha")
print(len(long_string))
print(long_string.replace("Floor","Ground"))
print(long_string.strip())

quote_list = long_string.split(" ")
print(quote_list)

print("\n\n")

print("--------------------Create file")

#test_file