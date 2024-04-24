def tuples_to_list(tuple_list):
    return [list(tup) for tup in tuple_list]

original_tuple1 = [(4,2),(2,3),(3,4)]
original_tuple2 = [(1,2),(2,3,5),(3,4),(2,3,4,2)]
print(tuples_to_list(original_tuple1))
print(tuples_to_list(original_tuple2))

def sum_of_tuples(tuple_list):
    return [sum(tup) for tup in tuple_list]

tuple_list = [(1, 2), (2, 3), (3, 4)]
print(sum_of_tuples(tuple_list))

tuple_list = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print(sum_of_tuples(tuple_list))


def is_present(typles,element):
    return any(element in tup for tup in tuples)

tuples = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
print(is_present(tuples, 'White')) 
print(is_present(tuples, 'Olive'))  

def third_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-3]

numbers = [4,3,1,2,9,7,8,6,10]
print(third_largest(numbers))


import itertools

from matplotlib.patches import Polygon

def find_combination(numbers,target):
    return [comb for comb in itertools.combinations(numbers,3)if sum(comb) == target]
numbers = [1,2,3,4,5,6]
target = 9
print(find_combination(numbers,target))


def find_missing(set1,set2):
    return(set1-set2,set2-set1)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 6}
print(find_missing(set1, set2))


def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count , odd_count
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count, odd_count = count_even_odd(numbers)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

def fibo(max_val):
    a,b = 0,1
    series = []
    while a <= max_val:
        series.append(a)
        a,b = b,a+b
    return series

print(fibo(50))


def fizz_buzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
            
fizz_buzz()
            

def triangle_type(a,b,c):
    if (a == b == c ):
        return"equilateral"
    elif a == b or b == c or a == c :
        return "isoceles"
    else:
        return "scalene"
    
# Example usage:
print(triangle_type(2, 2, 2))  # Equilateral
print(triangle_type(2, 3, 2))  # Isosceles
print(triangle_type(2, 3, 4))  # Scalene


def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(5)


def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a 

num1 = 48
num2 = 60 
print(gcd(num1,num2))

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(6))


def fact(n):
    if n == 0:
        return 1
    else :
        return n * fact(n-1)
    
print(fact(5))


def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

rows = 5
print_triangle(rows)


def minimum(num1,num2,num3):
    return min(num1,num2,num3)

def is_anagram(str1,str2):
    return sorted(str1) == sorted(str2)

def is_armstrong(n):
    order = len(str(n))
    sum = 0
    temp = n
    while(temp > 0):
        digit = temp % 10
        sum = sum+digit**order
        temp //= 10
    return sum == n

print(minimum(3, 1, 2))
print(is_anagram('listen', 'silent'))
print(is_armstrong(153))


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome(121))  
print(is_palindrome(123))



def divby7or5(start,end):
    return[n for n in range(start,end+1)if n % 7 == 0 and n%5 == 0]

print(divby7or5(1500, 2700))


def count_digits_letters(s):
    digit_count = sum(c.isdigit() for c in s)
    letter_count = sum(c.isalpha() for c in s)
    return {'Digits': digit_count, 'Letters': letter_count}

print(count_digits_letters("hello1234"))
    

def find_even_digits():
    result = []
    for num in range(100,401):
        if all(int(digit)%2 == 0 for digit in str(num)):
            result.append(str(num))
    return ','.join(result)

print(find_even_digits())


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))


def reverse_at_location(lst, start, end):
    lst[start:end+1] = reversed(lst[start:end+1])
    return lst
print(reverse_at_location([1, 2, 3, 4, 5], 1, 3))



from itertools import permutations
def list_permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        perms = []
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in list_permutations(rest):
                perms.append([lst[i]] + p)
        return perms

print(list_permutations([1, 2, 3]))




def kth_smallest(lst, k):
    return sorted(lst)[k-1]

print(kth_smallest([7, 10, 4, 3, 20, 15], 3))



l2 = [5, 6, 7, 8, 9, 2, 45, 23, 1, 0]
l2.sort()
x = int(input("enter the element position: "))
print(l2[x-1])


def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]
print(kth_largest([7, 10, 4, 3, 20, 15], 2))



def is_palindrome_list(lst):
    return lst == lst[::-1]
print(is_palindrome_list([1, 2, 3, 2, 1])) 



l1 = [1, 2, 4, 6, 8]
l2 = [4, 8, 9, 40, 20]
s1 = set(l1)
s2 = set(l2)
s3 = s1.union(s2)
s4 = s1.intersection(s2)
print(list(s3)), print(list(s4))



l1 = [1, 2, 3, 4, 1, 6, 7, 9, 3, 4]
l2 =[]
def remove_dup(list1):
    seen = []
    for x in list1:
        if x not in seen:
            seen.append(x)         
    return seen
print(remove_dup(l1))




x = int(input("enter a number: "))
dict1 = {}
for y in range(1 , x+1):
    dict1[y] = y*y   
print(dict1)


# Define a dictionary
my_dict = {'a': 1, 'b': 2}
# Add a new key-value pair
my_dict['c'] = 3
print(my_dict)


# Define dictionaries to be concatenated
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Concatenate dictionaries
new_dict = {**dict1, **dict2}
print(new_dict)


# Define a dictionary
my_dict = {'a': 1, 'b': 2}
# Check if key exists
key = 'a'
if key in my_dict:
    print(f"{key} exists in the dictionary.")
else:
    print(f"{key} does not exist in the dictionary.")



# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Iterate over keys and values using for loop
for key, value in my_dict.items():
    print(key, value)
for key in my_dict:
    print(key,my_dict[key])



# Define a function to generate dictionary of squares
def generate_squares(n):
    return {x: x*x for x in range(1, n+1)}
# Example usage:
print(generate_squares(5))


# Define a dictionary with keys as numbers and values as squares
square_dict = {x: x*x for x in range(1, 16)}
print(square_dict)



# Define dictionaries to be merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Merge dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)



# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Iterate over keys and values using for loop
for key in my_dict:
    print(key, my_dict[key])



# Task 42: Sum All Items in a Dictionary
def sum_dict_values(d):
    return sum(d.values())
# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 30}
print("Sum of all items in the dictionary:", sum_dict_values(my_dict))

# Task 43: Multiply All Items in a Dictionary
def multiply_dict_values(d):
    result = 1
    for value in d.values():
        result *= value
    return result
my_dict = {'a': 2, 'b': 3, 'c': 4}
print("Multiplication of all items in the dictionary:", multiply_dict_values(my_dict))

# Task 44: Remove a Key from a Dictionary
def remove_key(d, key):
    if key in d:
        del d[key]
# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
remove_key(my_dict, 'b')
print(my_dict)

# Task 45: Map Two Lists into a Dictionary
def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))
# Example usage:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print("Mapped dictionary:", map_lists_to_dict(keys, values))

# Task 46: Sort a Dictionary by Key
def sort_dict_by_key(d):
    return dict(sorted(d.items()))
# Example usage:
my_dict = {'b': 2, 'c': 3, 'a': 1}
print("Sorted dictionary by key:", sort_dict_by_key(my_dict))

# Task 47: Get Maximum and Minimum Values of a Dictionary
def max_min_values(d):
    return max(d.values()), min(d.values())
# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 5}
print("Maximum and minimum values:", max_min_values(my_dict))

# Task 48: Get a Dictionary from an Object's Fields
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def to_dict(self):
        return self.__dict__
# Example usage:
emp = Employee(101, 'John', 50000, 'IT')
print("Dictionary from Employee object:", emp.to_dict())

# Task 49: Remove Duplicates from a Dictionary
def remove_duplicates_from_dict(d):
    return {k: v for k, v in dict.fromkeys(d).items()}
# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
print("Dictionary after removing duplicates:", remove_duplicates_from_dict(my_dict))

# Task 50: Check if a Dictionary is Empty or Not
def is_dict_empty(d):
    return len(d) == 0
# Example usage:
my_dict = {'a': 1, 'b': 2}
print("Is the dictionary empty?", is_dict_empty(my_dict))

# Task 51: Define Python Class Employee
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self):
        pass

    def emp_assign_department(self, department):
        self.emp_department = department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)
# Example usage:
emp = Employee(101, 'John', 50000, 'IT')
emp.print_employee_details()

# Task 52: Define Python Class Restaurant
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = set()
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_table(self, table_number):
        self.booked_tables.add(table_number)

    def customer_order(self, order):
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_booked_tables(self):
        print("Booked Tables:", self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:", self.customer_orders)
# Example usage:
restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza", 10)
restaurant.add_item_to_menu("Burger", 8)
restaurant.print_menu()

# Task 53: Define Python Class BankAccount
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance
# Example usage:
acc = BankAccount("123456", 1000, "2024-04-30", "John")
print("Initial Balance:", acc.check_balance())
acc.deposit(500)
print("Balance after deposit:", acc.check_balance())
acc.withdraw(200)
print("Balance after withdrawal:", acc.check_balance())

# Task 54: Define Python Class Inventory
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price}
        return self.items

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            if item_name is not None:
                self.items[item_id]['item_name'] = item_name
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
        else:
            print("Item ID not found.")

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found.")

# Example usage:
inventory = Inventory()
# Add an item to the inventory
inventory.add_item(1, "Laptop", 10, 1000)
# Update the item's name
inventory.update_item(1, item_name="Updated Laptop Name")
# Update the item's stock count
inventory.update_item(1, stock_count=5)
# Update the item's price
inventory.update_item(1, price=1200)
# Check the details of the updated item
# Add an item to the inventory and get the updated dictionary of items
items = inventory.add_item(1, "Laptop", 10, 1000)
print("Items after adding item:")
print(items)
print("Item details after updates:")
print(inventory.check_item_details(1))


# Task 55: Create a Lambda Function to Add 15 to a Number
add_15 = lambda x: x + 15
# Example usage:
print("Result after adding 15 to 5:", add_15(5))

# Create a Lambda Function to Multiply Two Numbers and Print the Result
multiply = lambda x, y: x * y
# Example usage:
print("Result of multiplying 5 and 3:", multiply(5, 3))

# Task 56: Create a Function that Multiplies an Argument with an Unknown Given Number
def multiply_with_unknown(x):
    unknown_number = 10
    return x * unknown_number
# Example usage:
print("Result of multiplying 5 with an unknown number:", multiply_with_unknown(5))



# Task 57: Find the Second Lowest Total Marks of Any Student(s) Using Lists and Lambda
def second_lowest_total_marks(names, marks):
    student_data = list(zip(names, marks))
    sorted_data = sorted(student_data, key=lambda x: sum(x[1]))
    lowest_total = sum(sorted_data[0][1])
    second_lowest_total = float('inf')
    for _, marks in sorted_data:
        total_marks = sum(marks)
        if total_marks > lowest_total and total_marks < second_lowest_total:
            second_lowest_total = total_marks
    students = [name for name, marks in sorted_data if sum(marks) == second_lowest_total]
    return second_lowest_total, students
# Example usage:
names = ["John", "Alice", "Bob"]
marks = [[80, 90, 85], [75, 85, 80], [70, 85, 75]]
second_lowest_total, students = second_lowest_total_marks(names, marks)
print("Second Lowest Total Marks:", second_lowest_total)
print("Students with Second Lowest Total Marks:", students)

# Task 58: Find Numbers in a String and Display Sorted Numbers Longer Than List Length Using Lambda
import re
def display_sorted_numbers(string):
    numbers = re.findall(r'\d+', string)
    sorted_numbers = sorted(filter(lambda x: len(x) > len(numbers), numbers))
    return sorted_numbers
# Example usage:
string = "There are 5 apples, 10 oranges, and 15 bananas."
print("Numbers longer than the length of the list:", display_sorted_numbers(string))

# Task 59: Create a DataFrame from a Dictionary and Display it Using Pandas
import pandas as pd
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# Task 60: Create and Display a DataFrame from a Dictionary with Index Labels Using Pandas
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)

# Task 61: Display Summary of Basic Information About a DataFrame and its Data Using Pandas
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print("Summary of DataFrame:")
print(df.info())

# Task 62: Select 'Name' and 'Score' Columns from a DataFrame Using Pandas
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'Score': [80, 85, 90]}
df = pd.DataFrame(data)
selected_columns = df[['Name', 'Score']]
print(selected_columns)

# Task 63: Calculate the Mean of All Students' Scores Using Pandas
data = {'Name': ['John', 'Alice', 'Bob'],
        'Score': [80, 85, 90]}
df = pd.DataFrame(data)
mean_score = df['Score'].mean()
print("Mean of all students' scores:", mean_score)



try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print("a/b = %d" % c)
except Exception as e:
    print("Can't divide by zero")
    print(e)
else:
    print("Hi, I am else block")



try:
    # This will throw an exception if the file doesn't exist.
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close()


try:
    print(variable_not_defined)
except NameError as e:
    print("Error:", e)  # Print the error message associated with the exception


try:
    if True:
    print("Indented statement")
except IndentationError as e:
    print("Error:", e)  # Print the error message associated with the exception

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except IOError as e:
    print("Error:", e)  # Print the error message associated with the exception
    
try:
    while True:
        data = input("Enter data (press Ctrl+D to end): ")
        print("Data entered:", data)
except EOFError as e:
    print("Error:", e)  # Print the error message associated with the exception



# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Single Inheritance
class Student(Person):
    pass

# Multilevel Inheritance
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

# Example usage
x = Person("Nikhilesh", "Joshi")
x.printname()  # Output: Nikhilesh Joshi

x = Student("Dr Arun", "Kulkarni")
x.printname()  # Output: Dr Arun Kulkarni


# Define the Person class with firstname and lastname properties
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Define the Student class inheriting from Person
class Student(Person):
    pass

# Create a Student object and print the name
x = Student("Dr Arun", "Kulkarni")
x.printname()

# Use the super() function to inherit properties from the parent class
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Dr Arun", "Kulkarni")
x.printname()

# Add properties to the Student class
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Dr Arun", "Kulkarni")
x.printname()
print(x.graduationyear)

# Add a year parameter to the Student class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Nikhilesh ", "Joshi", 1999)
x.printname()
print(x.graduationyear)

# Add a welcome method to the Student class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Nikhilesh ", "Joshi", 1999)
x.welcome()

# Define the Polygon class with methods for inputting and displaying sides
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

# Define the Triangle class inheriting from Polygon
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

# Define classes using multiple inheritance
class SuperClass1:
    def super_method1(self):
        print("Super Class 1 method called")

class SuperClass2:
    def super_method2(self):
        print("Super Class 2 method called")

class MultiDerived(SuperClass1, SuperClass2):
    def multi_derived_method(self):
        print("MultiDerived class method called")

# Create an object of the MultiDerived class
md = MultiDerived()
md.super_method1()
md.super_method2()
md.multi_derived_method()

# Define the shapes class with methods for inputting and displaying sides
class shapes:
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(no_sides)]

    def takeSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def disSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

# Define the rec class inheriting from shapes
class rec(shapes):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b = self.sides
        area = (a + b) * 2
        print('The area of the rectangle is' %area)

t = rec()
t.takeSides()

