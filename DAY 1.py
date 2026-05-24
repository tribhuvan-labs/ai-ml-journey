#python basics
#section 1:

print("Hello World")
print("My name is Tribhuvan Mishra")
print("College: RKGIT Gaziabad")
print("Goal: AI/ML Engineer")
print("Target:20 LPA")
print("Journey starts here!")

##section 2:
#string
name = "Tribhuvan Mishra"
college = "RKGIT Gaziabad"
city = "Ghaziabad"

#integer
age = 21
year=2
marks = 83

#float
cgpa = 8.5
height = 5.8
percentage = 83.0

#boolean
is_student = True
has_laptop = True  
print(f"Name:{name}")
print(f"College:{college}")
print(f"City:{city}")
print(f"Age:{age}")
print(f"cgpa:{cgpa}")
print(f"Height:{height}")
print(f"Percentage:{percentage}")
print(f"Is student:{is_student}")
print(f"Has laptop:{has_laptop}")

##section 3: Type checking
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

#section 4: f-string
print(f"My name is {name} and I am from {city}. I am {age} years old and my cgpa is {cgpa}.")
print(f"i study at {college}")
print(f"next year i will be in year{year+1}")

#section 5: math operations
a=10
b=78
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Remainder: {a%b}")
print(f"Exponentiation: {a**2}")
print(f"Floor Division: {b//a}")


#program 1: my introduction

name = "Tribhuvan Mishra"
age = 21
college = "RKGIT Gaziabad"
cgpa = 8.5
goal = "AI/ML Engineer"
target = "20 LPA"

print("="*30)
print("My Introduction")
print("="*30)
print(f"Name: {name}")       
print(f"Age: {age}")
print(f"College: {college}")
print(f"CGPA: {cgpa}")
print(f"Goal: {goal}")
print(f"Target: {target}")
print("="*30)

#   calculator
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print(f"\nAddition: {num1+num2}")
print(f"Subtraction: {num1-num2}")
print(f"Multiplication: {num1*num2}")
print(f"Division: {num1/num2}")
print(f"Remainder: {num1%num2}")
print(f"Exponentiation: {num1**num2}")
print(f"Floor Division: {num1//num2}")

### area calculator

print("\nArea Calculator")
num1=float(input("Enter length: "))
num2=float(input("Enter breadth: "))
area=num1*num2
print(f"Area of rectangle: {area}")
perimeter=2*(num1+num2)
print(f"Perimeter of rectangle: {perimeter}")

##program 4: swape two numbers
print("\nSwapping Two Numbers")
num1=float(input("Enter first number: "))
num2 =float(input("Enter second number: "))
print(f"Before swapping: num1={num1}, num2={num2}")
temp=num1
num1=num2
num2=temp
print(f"After swapping: num1={num1}, num2={num2}")

##program 5: TEMPERATURE CONVERSION
print("\nTemperature Conversion")
celsius=float(input("Enter temperature in Celsius: "+"C"))
fahrenheit=(celsius*9/5)+32
print(f"Temperature in Fahrenheit: {fahrenheit}F")   
kelvin=celsius+273.15
print(f"Temperature in Kelvin: {kelvin}")

#program 6: user input introduction
print("\nUser Input Introduction")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

if age>=18:
    print("You are an adult.")
else:
    print("You are a minor.")   


    ##simple interest calculator
print("\nSimple Interest Calculator")
principal=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time in years: "))
simple_interest=(principal*rate*time)/100
print(f"Simple Interest: {simple_interest}")
print(f"Total Amount: {principal+simple_interest}")


##BMI CALCULATOR
print("\nBMI Calculator")
weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in meters: "))
bmi=weight/(height**2)

print(f"\nYour BMI is: {bmi:.2f}")
if bmi<18.5:
    print("You are underweight.")
elif 18.5<=bmi<24.9:
    print("You have a normal weight.")
elif 25<=bmi<29.9:
    print("You are overweight.")    
else:
    print("You are obese.") 

    ##print string patterns
print("\nString Patterns")
word=input("Enter a word: ")
print(f"Original: {word}")
print(f"Reversed: {word[::-1]}")
print(f"Uppercase: {word.upper()}")
print(f"Lowercase: {word.lower()}")
print(f"replaced: {word.replace(word[0],'*')}")
print(f"Length: {len(word)}")
print(f"split: {word.split()}")
print(f"split: {word.split(',')[3]}")

##program 10 -variable patterns
print("\nVariable Patterns")
#pattern 1:
x=y=z=10
print(f"Pattern 1: x={x}, y={y}, z={z}")

#pattern 2:
a,b,c=10,20,30
print(f"Pattern 2: a={a}, b={b}, c={c}")

#pattern 3:
counter=0
counter+=1
print(f"Pattern 3: counter={counter}")

#pattern 4:string repitition
line="*"*30
star="*"*10
print(f"Pattern 4:\n{line}\n{star}\n{line}")
print(f"Pattern 5: {line}\n{star}\n{line}")

#pattern 5: concatenation
first_name="Tribhuvan"
last_name="Mishra"
full_name=first_name+" "+last_name
print(f"Pattern 5: {full_name}")

#pattern 6:number formatting
number=1234567890
number_4: 22032903.8998329
print(f"Pattern 6: {number:,}")  # With comma as thousands separator
print(f"Pattern 6: {number_4:.2f}")  # With two decimal places



#end of day 1
print("\nEnd of Day 1")
print("\n"+"="*30)


