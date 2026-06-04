#=========================
# DAY # -PYTHON LOOPS

#CONCEPT ! 1 FOR LOOPS :

#print 1 to 10:
print("Numbers 1 to 10")
for i in range(1,11):
    print(i,end=" ")
print()

#print with range step
print("\n Even numbers 2 to 20:")
for i in range(2,21,2):
    print(i,end=" ")
print()

#print coundown
for i in range (10,0,-1):
    print(i,end=" ")
print("\nBLASTING")

####CONCEPT 2----WHILE LOOP BASICS

print("using while loop")
i=1
while i<=10:
    print(i,end=" ")
    i+=1
print()

#COUNDOWN USING WHILE:
print("\nWhile coundown")
i=5
while i>=0:
    print(i,end=" ")
    i-=1
print("Done!")





#========================
#CONCEPT 3: Break AND CONTINUE:
print("Break at 5:")
for i in range(1,11):
    if i==5:
        break
    print(i,end=" ")
print()


###continue example:
print("\n skip even numbers:")
for i in range(1,11):
    if i%2==0:
        continue
    print(i,end=" ")
print()
#============
#CONCEPT 4-----LOOP with string:

name="TRIBHUVAN"
print(f"Letters in {name}")
for letter in name:
    print(letter,end=" , ")
print()



##count  vowels
vowels=0
for letter in name :
    if letter.lower() in "aeiou":
        vowels+=1
print(f"Vowels in {name}: {vowels}")


#PRogram 1: Sum of numbers:
n=int(input("Enter n:"))
total=0

for i in range(1,n+1):
    total+=i

print(f"Sum of 1 to {n} = {total}")

#verify with formula :
formula_result=(n*(n+1))/2
print(f"Formula result={formula_result}")



# PROGRAM 2: multiplication table :
num =int(input("Enter number for table:"))
print(f"\n Multiplication table of {num}:")
print("-"*20)
for i in range(1,11):
    print(f"\n {num}*{i}={num * i}")

print("-"*20)


###PROGRAM #-----FACTORIAL:
n=int(input("enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(f"Factorial of {n}:{factorial} ")

    ##PROGRAM:
num = int (input("Enter number:"))
is_prime=True

if num < 2:
    is_prime=False
else:
    for i in range(2,num):
        if num % i==0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is PRIME")
else:
    print(f"{num} is not prime")

#=================
#FIBonacci series :
#===================
n= int(input("Enter how many terms i should print:"))
a=0
b=1

print(f"Fiboonacci series till {n} terms: ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()




# print all prime number 6
n=int(input("Enter n:"))
print(f"\n Prime numbers up to {n}: ")

for num in range(2,n+1):
    is_prime=True
    for i in range (2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")
print()



#Program 7: REverse a number:
num=int(input("Enter a number"))
original=num
reverse=0

while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print(f"Original:{original}")
print(f"reversed:{reverse}")


##program 8 : Armstrong number:
num=int(input("Enter a 3---digit number:"))
original=num
total=0

while num>0:
    digit=num%10
    total+=digit**3
    num=num//10

if total == original:
    print("f{original}: is Armstrong number")
else:
    print(f"{original}:is not Armstrong number")





#===================================
#PATTERN 1:--------------RIGHT TRIANGLE:------------------- 
#===================================
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#--------2------------PATTERN INVERTED TRIANGLE:----------------------
n=int(input("Enter the num:"))
for i in range(1,n,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

## pyramid : 3   
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    # stars :
    for k in range(2*i-1):
        print(" *",end=" ")
    print()

    ###PATERN 4 : NUMBER TRIANGLE:
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

##SAME NUMBER TRIANGLE:5
n=5
for i in range (1,n+1):
    for j in range (1,i+1):
        print(i,end=" ")
    print()

###ALPHABET TRIANGLE:6
n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

###   SQUARE PATTERN:7
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


#============================
# PATTERN 8: HOLLOW SQUARE:8
#============================

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(" *",end=" ")
        else:
            print(" ",end=" ")
    print() 


#==============================
#DIAMOND PATTERN :9
#==============================

n=5
#Upper Half:
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(" *",end=" ")
    print()


#lower HALF:
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#============================
#MULTIPLICATION TABLE GRID: 10
#============================
print("     ",end=" ")
for i in range(1,21):
    print(f"{i:4}",end=" ")
print()
print("-" * 44)

for i in range(1,21):
    print(f"{i:3}",end=" ")
    for j in range(1,11):
        print(f"{i*j:4}",end=" ")
    print()































    