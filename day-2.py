print("#"*20)
print("PYTHON CONDITIONAL STATEMENTS")
print("#"*20)

#CONCEPT 1: COMPARISON OPERATORS----
# ==, !=, >, <, >=, <=
a=67
b=89

print(f"\n a={a},b={b}")
print(f"\na==b (equal):{a==b}")
print(f"\na!=b(not equal to):{a!=b}")
print(f"\na>b(greater than):{a>b}")
print(f"\na<b(less than):{a<b}")
print(f"\na>=b(greater than equal to):{a>=b}")
print(f"\na<=b(less than equal to):{a<=b}")


#concept 2 : if statement

age=20

if age>=18:
    print(f"Age{age} is adult age")
age =15
if age >=18:
    print(f"Age {age} is adult age")
else:
    print(f"age {age}is minor ")


###if elif else Chain 
marks =85

if marks>=90:
    print(f"{marks}:-->Grade A")
elif marks >=75:
    print(f"{marks}-->Grade B")
elif marks>=65:
    print(f"{marks}:Grade-->C")
elif marks>=56:
    print(f"{marks }:Grade--> D")
else:
    print(f"{marks}:FAIL")


print("\n ----CONCEPT 4 : AND OPERATOR ___")
age=80
salary=89000

print(f"Age:{age},Salary:{salary}")
if age >=18 and salary>=25000:
    print("Eligible for Loan")
else: 
    print("NOT eligible for loan")



#### Concept 5: OR operator
student_discount=True
senior_discount=False

print(f"Student:{student_discount},Senior:{senior_discount}")

if student_discount or senior_discount:
    print("you will get discount")
else:
    print("no discount")

#Concept 6: NOT OPERATOR
print("\n----CONCEPT 6:NOT OPERATOR")
is_raining=True
if not is_raining:
    print("go out and play")
else:
    print("stay inside")


##concept 7: NESTED if:

age=20
marks=85

if age >=19:
    print(f"{age}:you are adult")
    if marks>=75:
        print(f"Marks{marks}-Excellent performance")
    else:
        print(f"marks:{marks}--work harder")
else:
    print(f"Age{age}--you are minor")

#### These are the concepts which is required to practice todays coding problems::::::::++++++==========





#PROGRAM 1: --EVEN OR ODDDD

num =int(input("ENTER THE NUMBER:"))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# PROGRAM 2: VOTING ELIGIBILITY------

age=int(input("Enter the Num :"))

if age>=18:
    print(f"{age}: you are eligible for voting")
else:
    years_to_wait=18-num
    print(f"{age}: you are not eligible for voting")
    print(f"you have to wait {years_to_wait} for voting")

## program 3: GRADE CALCULATOR-------

marks= float(input("Enter the Marks:"))
if marks>=90:
    grade="A"
    status="EXCELLENT"
elif marks>=75:
    grade="B"
    status="GOOD"
elif marks>=50:
    grade="C"
    status="OK"
else:
    grade="F"
    status="FAIL"

print(f"Marks:{marks}")
print(f"Grade: {grade}")
print(f"status:{status}")



## PROGRAM 4: LOGIN SYSTEM--------
correct_username="tribhuvan"
correct_password="password78790"

username =input("ENTER the username:")
password=input("Enter password:")

if username==correct_username  and password==correct_password:
    print(f"your credentials are right")
else:
    if username != correct_username:
        print("your username is not correct")
    else:
        print("your password is wrong") 

print("#="*30)
# Program 5: Age Category---------
age=int(input("Enter your age:"))

if age < 13:
    category="Child"
elif age < 18:
    category="teenage "
elif age <60:
    category="adult"
else:
    category="senior citizens"

print(f"Age:{age}----->category{category}")


print("#="*30)
# Program:6 ---->Number Comparison-------
num1=int(input("Enter first number:"))
num2=int (input ("Enter the second number :"))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"num1 is less than num2 ")
else:
    print(f"Both num are equal {num1}={num2}")



#PROGRAM 7--->Discount calculator

price=float(input("enter price:"))
if price >=10000:
    discount=20
elif price >=5000:
    discount=15
elif price>=1000:
    discount=10
else:
    discount=0

discount_amount=(price*discount)/100
final_price= price-discount_amount

print(f"original price: {price}")
print(f"discount:{discount}%")
print(f"discount Amount:{discount_amount}")
print(f"Final price:{ final_price}")

####
#program 8: Temperature Category
# ##############

temp=float(input("enter the temperature in celcius:"))

if temp <0:
    category="Freeezing"
elif temp < 15:
    category = "cold"
elif temp < 27:
    category = "mild summer"
elif temp <35:
    category=" hot"
else:
    category="very hot"

print(f"Temperature:{temp}C----->{category}")


#program ---->marks checker

marks = int(input("Enter marks"))
      
if marks >= 90:
    print("Excellent!")
elif marks >= 75:
    print("good")
elif marks >= 50:
    print("pass")
else:
    print("need more effort")


    ##program 10: TRAFFIC LIGHT SYSTEM

color =input("Enter traffic light color (red/yellow/green):").lower()
if color=="red":
    action ="stop"
    message="wait for signal"
elif color == "yellow":
    action="CAUTION"
    message="get ready to move"
elif color =="green":
    action="GO"
    message="move forward"
else:
    action="invalid"
    message="unknown color"

print(f"Traffic Light:{color.upper()}")
print(f"Action:{action}")
print(f"Message:{message}")



#--------------------------
#PROGRAM 11: CALCULATOR:

num1= float(input("enter the number1:"))
num2= float(input("enter the number 2:"))
operation=input("enter operation(+,-,*,/):")

if operation =="+":
    result=num1+num2
    print(f"{num1}+{num2}={result}")
elif operation == "-":
    result=num1-num2
    print(f"{num1}-{num2}={result}")
elif operation=="*":
    result=num1*num2
    print(f"{num1}*{num2}={result}")
elif operation == "/":
    if num2!=0:
        result=num1/num2
        print(f"{num1}/{num2}={result}")
    else:
        print("cannot divide by zero")
else:
    print("invalid operation")


# LOAN ELIGIBILITY: 12:

age=int(input("enter age"))
salary= float(input("enter the salary:"))
credit_score=int(input("enter credit score"))


print("\nchecking eligibility")
eligible=True
reason=[]

if age<18:
    eligible=False
    reason.append("Age must be 18 or above")

if salary <50000:
    eligible=False
    reason.append("salary must be at least 50000")

if credit_score<700:
    eligible=False
    print("credit score must be at least 700")

if eligible:
    print("Eligible for loan")
    loan_amount=salary*12
    print(f"Maximum loan:{loan_amount}")
else:
    print("not eligible for loan")
    for reasons in reason:
        print(f"--{reason}")


### PROGRAM 13 MULTIPLE CONDITIONS

cgpa=float("Enter CGPA:")
projects=int(input("Enter number of Projects"))

if cgpa >=8.0 and projects>=2:
    print("Excellent profile for internships")
elif cgpa >=7.5 or projects>=3:
    print("good projects for internships")
elif cgpa >=7.0:
    print("average profile->improve cgpa or do more projects")

else:
    print("work harder on academics")






#program: 14 : shopping discount

is_member=input("Are you a member?(yes/no):").lower()=="yes"
amount=float(input("Enter the purchase amount"))
discount=0

if is_member:
    if amount>=5000:
        discount=20
    elif amount>=2000:
        discount=15
    else:
        discount=10
else:
    if amount>=5000:
        discount=10
    elif amount>=2000:
        discount=5
    else:
        discount=0


discount_amount=(amount*discount)/100
final_amount=amount-discount_amount

print(f"\nAmount: {amount}")
print(f"Member : {"Yes" if is_member else "no"}")
print(f"discount: {discount}%")
print(f"save: {discount_amount}")
print(f"Final amount: {final_amount}")

## END OF DAY 2
#========================================
print("CONDITIONS COMPLETED")



