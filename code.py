print("hello world\n","with nayasha sharma")
name = "nayasha"             #variables
age = 21
PI = 3.14
print(name, age, PI)
print("my name is:", name)
print("my age is:",age-5)
print(type(age))              #data type
print(type(PI))
print(type(name))
num = 3               
isPrime = False    
print(type(isPrime))
tot_price = 100
full_name = "nayasha sharma"
a = 3
b = 12
sum = a + b
print(sum)
print("sum is:", sum)
#arithmetic op
a = 3
b = 8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulo
print(a**b)
#relational op
a = 6
b = 3
print(a > b)
print(a == b)
print(a != b)
print(a >= b)
#asignment op
a = 6
b = 2
a += 5 # a = a * 5
a *= 5
a /= 5 #a = a / 5
a %= 5
a **= 5
print(a)
#logical op     #not op
var = False
print(not var) #true
print(not (3 > 7))
print((5 > 3) and (3 > 2)) #true # and op
print((3 > 2) or (2 > 1)) # or op



x = 3
x += 5
print(x)

ans = int(5 + 10.0) #type conversion
print(ans)
print(type(ans))

ans1 = int(5 + 10.0) #casting
ans2 = 5 + 10.0  #conversion
print(ans1, type(ans))
print(ans2, type(ans))

val = bool(-10)
print(val, type(val))

username = input("enter your name:") #user input
print("welcome", username)

sum = 3 + 4
print(sum)

mul = 4 * 4
print(mul)

div = int(4 / 2)
print(div)

mod = 10 % 5
print(mod)



a = int(input("enter a:"))
b = int(input("enter b:"))
sum = a + b
print(sum)

a = int(input("enter a:"))
b = int(input("enter b:"))
sub = a - b
print(sub)

a = int(input("enter a:"))
b = int(input("enter b:"))
mul = a * b
print(mul)

a = int(input("enter a:"))
b = int(input("enter b:"))
div = a / b
print(div)


a = int(input("enter a:"))
b = int(input("enter b:"))
mod = a % b
print(mod)


a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
avg = (a+b+c)/3
print("avg of 3 nums =", avg)

a = float(input("enter a:"))
b = float(input("enter b:"))
avg = (a+b)/2
print("avg of 2 nums =", avg)
#conditional statements
age = 21   
if age >= 18:
     print("you can vote")
     print("u can drive")
else:
     print("u can't vote")

#traffic lights #elif

age = int(input("enter age: "))
if (age < 13) :
     print("child")
elif (age >= 13 and age <= 18) :
      print("teenager")
else:
     print("adult")
  
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("Login Successful!")
elif username == "admin" and password != "pass": 
    print("correct Username and wrong password")
elif  username != "admin" and password == "pass" :
    print("wrong username and correct password")
else:
     username != "admin"  and password != "pass"
     print("wrong username and password")

     
n = int(input("enter num:"))
if (n % 5 == 0):
     print("multiple of 5")
else: 
      print("not multiple of 5")


n = int(input("enter num:"))
if (n % 2 == 0):
     print("EVEN")
else:
     print("ODD")


#chck if no is palindrome or not
n = int(input("Enter number: "))
rev = int(str(n)[::-1])

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")










#check if n is prime no. or not
n = int(input("enter n: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("prime")
else:
    print("not prime")


#print all prime no.
n = int(input("Enter n: "))

for n in range(2, n + 1):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n)

#print prime no. upto 50
for n in range(2, 51):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n)



















#nesting


#match case
color = input("enter color:")

match color:
     case "Green":
        print("Go")
     case "Yellow":
         print("Look")
     case"Red" :
          print("Stop")
     case _:
          print("Wrong color!")


#loops
while True:
     print("hello world")

count = 1 #iterator
while count <= 5:
     print("HW", count)
     count += 1
print("after loop, count =", count)

i = 1 #iterator
while(i <= 5):
     print(i)
     i += 1

i = 5     #reverse
while(i >= 1):
   print(i)
   i -= 1

n = int(input("enter n: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("prime")
else:
    print("not prime")

n = int(input("enter n: "))
i = 1           #multiplication table of any num
while(i <= 10):
     print(n*i)
     i += 1

i = 1
while(i <= 10):
        if(i % 6 == 0):
         break
        print(i)
        i += 1

print("outside loop now.....")


#continue skip

#for loop
string = "hello"
for var in string:
     print(var)


string = "hello"
if 'o' in string:
     print("o exits in string")

for i in range(5):
     print("hello world")

word = "artificial intelligence"
#count number of i's => 5
count = 0
for ch in word:
     if(ch == 'i'):
          count += 1

print("count of i =", count)

word = "artificial"
count = 0
for ch in word:
     if(ch =='a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
          count += 1
          print("ans =", count)      

#range()
for i in range(5):
     print(i)
               #st,stp,step
for i in range(1, 10, 2):
     print(i)

#sum of 1st first n natural numbers
n = int(input("enter n:"))
sum =0
for i in range(1, n+1):
     sum += i
print("sum =", sum)
#1 to 5 natural numbers
sum = 0
for i in range(1,6):
     sum += i
print("sum =", sum)












#functions
def hello():     #fnxn definition
     print("hello")

hello()  #fnxn call


def sum(a, b): #parameter
     s = a + b
     return s
        
ans = sum(3, 4) #fnxn call
print(ans)/ print(sum(3, 4))

#sum of 3 nums
def sum(a,b,c):
     s = a + b + c
     return s

print(sum(3,4,5))

#print sum of 1st n natural numbers susing function
def sum(n):
     sum = 0
     for i in range(1, n +1):
         sum+=i
     return sum
n = int(input("enter n:"))
print("sum =", sum(n))





#sum of n natural numbers
n = int(input("enter n:"))
sum = 0
for i in range(1, n + 1):
     sum +=i
print("sum =", sum)







#AVG OF 3 nums using function
def avg(a, b, c):
     return (a + b + c) / 3

ans = avg(3, 4, 5)
print(ans)

def calc_avg(a, b, c):
     sum = a + b + c
     return sum/ 3

print (calc_avg(2, 2, 2))

def sum(a, b=1):
     return a + b

print(sum(3, 4))
print(sum(3)) #default value of b is 1

sum = lambda a, b: a + b
print(sum(3, 4))

avg = lambda a, b: (a+b)/2
print(avg(4, 5))

#factorial of n      
def calc_fact(n):     
   fact = 1
   for i in range(1, n + 1):
     fact = fact * i
     return fact
n = int(input("enter n:")) 
print(calc_fact(n))  

#check if num is palindrome or not using function
def palindrome(n):
   rev = int(str(n)[::-1])

   if n == rev:
     print("palindrome")
   else:
    print("not palindrome")

n = int(input("enter n:"))
palindrome(n)

#palindrome string using function
def string(s):
  if s == s[::-1]:
     print("palindrome")
  else:
          print("not palindrome")

s = (input("enter string:"))
string(s)
     
#reverse string using function
def reverse(s):
     print(s[::-1])
s = input("enter string:")
reverse(s)

#reverse a num using function
def rev_num(n):
     print(int(str(n)[::-1]))
s = input("enter string:")
rev_num(s)

#sort num using function # ascending
def sort_num(n):
     print("".join(sorted(n)))
n = input("enter n:")
sort_num(n)


#sort num using function # descending
def sort_num(n):
     print("".join(sorted(n, reverse = True)))
n = input("enter n:")
sort_num(n)

#check if num is odd or even
def num(n):
     if n % 2 == 0:
      print("even")
     else:
      print("odd")
n = int(input("enter n:"))
num(n)



















#check if num is prime or not using function
def prime(n):
     count = 0
     for i in range(1, n + 1):
          if n % i == 0:
           count = count + 1
     if count == 2:
          print("prime")
     else: 
          print("not prime")

n = int(input("enter n:"))
prime(n)
     









#hw prb
salary = int(input("enter final tax rate:"))
if salary < 30000:
       print("Tax rate = 5%")
elif salary <= 70000:
       print("Tax rate = 15%")
else:
      salary > 70000
      print("Tax rate = 25%")
     
#evn nums
def even(a, b):
     for i in range(a, b +1):
          if i % 2 == 0 :
               print(i)

even(1,10)

#odd nums
def odd(a, b):
     for i in range(a, b +1):
          if i % 2 != 0 :
               print(i)

odd(1,10)
#count no. of digits in a number
def digits(n):
     for i in str(n):
          print(i)
digits(312)

#count no. of digits in a number using yield
def digits(n):
    for i in str(n):
        yield i

for i in digits(312):
    print(i)





#count no. of digits in a number
def count_digits(n):
     return len(str(n))
n = int(input("enter n:"))
print(count_digits(n))



def count_digits(n):
     print(len(str(n)))
          
n = int(input("enter n:"))

count_digits(n)


#return the sum of digits of a number n
def sum_digits(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)

    print(sum)

n = int(input("enter n:"))
sum_digits(n)


#print all the no. that are divisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


#positive or negative until Quit
while True:
    n = input("enter n:")
    if n == "Quit":
        break

    if int(n)>0:
     print("positive")
    else:
     print("negative")

#simple calculator using function
def calculator(a,b, operation):
     if operation == "+":
         return a + b
     if operation == "-":
              return a - b
     if operation == "*":
              return a * b
     if operation == "/":
              return a / b
     else:
          print("invalid operation")

print(calculator(5,6,"+"))
     
#simple calculator
a = int(input("Enter a: "))
b = int(input("Enter b: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")



#check if num is prime or not using function
def prime(n):
     count = 0
     for i in range(1, n + 1):
          if n % i == 0:
           count = count + 1
     if count == 2:
          print("prime")
     else: 
          print("not prime")

n = int(input("enter n:"))
prime(n)

#number guessing game
secret = 50

guess = int(input("Guess the number: "))

if guess > secret:
    print("Too high")

elif guess < secret:
    print("Too low")

else:
    print("Correct!")


#strings     ' '  " "  '''  ''' 
word = "python"   # strings are immutable
print(len(word))
#loop in strings
for ch in word:
     print(ch)

word1 = "I like"
word2 = "python"
#concatenate
print(word1 + " " + word2)
sentence = word1 + " " + word2
print(sentence)
word3 = "pythn"
print(word3[0])


word4 = "aiml"   #slicing
print(word4[2:3])

word5 = "I study from ApnaCollege"
print(word5[13:25])
print(word5[:13])
print(word5[-6:-3])

#formatting
a = 5
b = 10
sum = a + b
print("sum is {}".format(sum))
#normal formatting
print("lamguage is {}".format("python"))

print("sum of {} & {} is {}".format(a, b, sum))
#index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))
#value based formatting
print("values of vars {a} & {b}".format(a=5, b=10))

#f-strings
print(f"sum of {a} & {b} is {a + b}")
print(f"avg of {a} & {b} is {(a + b)/2}")

#Lists = mutable sequence of values
marks1 = 99
marks2 = 89
marks3 = 100
marks4 = 65
marks5 = 92

marks = [99, 89, 100, 65, 92]   #list
print(marks)
print(marks[1])
marks[2] = 70
print(marks)
print(len(marks))

#slicing
print(marks[0:5])
print(marks[5:len(marks)])

#list methods
nums = [1, 2, 3]
nums.append(4)
print(nums)
nums.insert(1,4)
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

#loops in lists
nums = [1, 2, 3, 10, 4]
for val in nums:
    print(val)


nums = [1, 2, 3, 10, 4]
#to find x in kist
x = 10
idx = 0

for val in nums:
   if (val == x): 
       print(f"x/{x} found at idx={idx}")
       break
   idx += 1

#tuples => immutable sequences of values
tup = (1, 2, 3, 4, 5)
print(tup)
print(tup[2])
print(type(tup))
print(len(tup))
print(tup[0:3])
print(tup[:])

sum = 0
for val in tup:
    sum += val

print(f"sum of val is {sum}")
#tuple methods
tup = (1, 2, 2, 3, 2, 4)

print(tup.index(2))
print(tup.count(2))

#dictionaries => key :value pairs in which key is unique
info = {
     "name": "shradha",  # dict are mutable, unordered
     "cgpa": 9.2,
     "subjects": ["math", "science"]
}

info["cgpa"] = 9.6
print(info["cgpa"])
print(info)
print(type(info))
print(info["name"])
#dictionary methods
print(info.keys())


info = {
     "name": "shradha",  # dict are mutable, unordered
     "cgpa": 9.2,
     "subjects": ["math", "science"]
}

dict_keys = info.keys()
dict_keys = list(info.keys())
print(dict_keys)
print(type(dict_keys))

dict_vals = list(info.values())
print(dict_vals)

print(info.items())

print(info.get("cgpa"))
print(info.get("cgpa2"))
print("End of code")

info.update({
    "city": "Delhi",
})

print(info)

#sets => collection of unique elements -> immutable
s = {1, 2, 2, 2, 3}
print(s)
print(type(s))
print(len(s))
s.add(5)
print(s)

empty_set = set()
print(type(empty_set))

s,remove(1)
print(s)

s.clear()
print(s)

s.pop()
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}
print(s1.union((s2)))
print(s1.intersection(s2))



def even(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)
even(6)

def even(n):
    if n % 2 == 0:
        print(n)
even(6)

def even(n):
    if n % 2 == 0:
        print("even =",n)
even(6)

def odd(n):
    if n % 2 != 0:
        print("odd =",n)
odd(7)

def odd(n):
    for i in range(1, 8, 2):
      if n % 2 != 0:
        print(i)
odd(7)

#oops
class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

#object
stu1 = Student()
stu2 = Student()
print(stu1)
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)

#oops
#init method
class Student:
   def __init__(self, name, cgpa):
     self.name = name
     self.cgpa = cgpa

stu1 = Student("Rahul", 9.0)
stu2 = Student("Naya", 8.4)
stu3 = Student("Shradha", 9.2)

print(stu1.name)
print(stu2.cgpa)
print(stu3.name)
 



class Student:
   college_name = "ABC college"#class
   def __init__(self, name, gpa):
     self.name = name #instance
     self.gpa = gpa

stu1 = Student("Rahul", 9.2)

print(stu1.name)
print(stu1.college_name)


#encapsulation=>Wrapping data & methods into single unit.
# protect data from accidental & unauthorized modification.
class BankAccount:
     def __init__(self, name, balance):
         self.name = name
         self.balance = balance


acc1 = BankAccount("Rahul", 100_000)
print(acc1.name, acc1.balance)

#inhertance => reusing attributes & methods from a parent class.
class Employee:
    start_time = "10am"
    end_time = "5pm"

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Math")
print(t1.subject, t1.start_time, t1.end_time)

class AdminStaff(Employee):
     def __init__(self, role):
         self.role = role
staff1 = AdminStaff("manager")
print(staff1.role, staff1.start_time, staff1.end_time)



#abstraction => hiding unecessary details & shows essential features
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar!")

lion = Lion()
lion.make_sound()

class Cow(Animal):
    def make_sound(self):
        print("moo")

cow = Cow()
cow.make_sound()

#polymorphism=> redefining parent class in child class
class Employee:
     def get_designation(self):
         print("designation = Employee")

class Teacher(Employee):
       def get_designation(self):
           print("designation = teacher")

t1 = Teacher()
t1.get_designation()


#duck typing => walks like ducks & quacks like duck is duck
class Employee:
     def get_designation(self):
         print("designation = Employee")

class Accountant(Employee):
       def get_designation(self):
           print("designation = Accountant")

acc1 = Accountant()
acc1.get_designation()























































































































































































































































































































































