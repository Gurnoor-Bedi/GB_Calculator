def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mult(a,b):
  return a*b
def div(a,b):
  return a/b
def aot(a,b):
  return 0.5*a*b
def aoc(r):
  return 3.14*r*r
def aoe(a,b):
  return 3.14*a*b
def lg(a):
  import numpy as np
  a= np.log(78)
  return a

menu =["+","-","/","*","aoc","aot","lg","aoe"]
print("Calculator.")
print()
print("Choose what operation to run.")
print()


print ("Press '+' for addition , Press '-' for subtraction, Press '/' for division and Press '*' for multiplication.")
print ("Enter 'aot' for area of triangle , Enter 'aoc' for area of circle, Enter 'aoe' for area of ellipse and Enter 'lg' for log to the  base 10.")
choice = input("Enter your operator.")

if choice== "+":
  a=int(input("Enter your 1st number: "))
  b=int(input("Enter your 2nd number: "))
  print ("The answer is: ",add(a,b))
elif choice=="-":
  a=int(input("Enter your 1st number: "))
  b=int(input("Enter your 2nd number: "))
  print ("The answer is: ", sub(a,b))
elif choice=="*":
  a=int(input("Enter your 1st number: "))
  b=int(input("Enter your 2nd number: "))
  print ("The answer is: ", mult(a,b))
elif choice=="/":
  a=int(input("Enter your 1st number: "))
  b=int(input("Enter your 2nd number: "))
  print ("The answer is: ", div(a,b))
elif choice=="aot":
  a=int(input("Enter your base length."))
  b=int(input("Enter your height."))
  print ("The answer is: ", aot(a,b))
elif choice =="aoc":
  r=int(input("Enter your radius."))
  print ("The answer is: ", aoc(r))
elif choice=="aoe":
  a=int(input("Enter the length of major axis."))
  b=int(input("Enter length of minor axis."))
  print ("The answer is: ", aoe(a,b))
elif choice =="lg":
  a=int(input("Enter your number."))
  print ("The answer is: ", sub(a))

else:
  print ("Stop.")