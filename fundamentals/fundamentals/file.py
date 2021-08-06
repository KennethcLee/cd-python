num1 = 42  #variable declaration
num2 = 2.3 #Numbers
boolean = True   #Boolean
string = 'Hello World'  #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']   # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictonary
fruit = ('blueberry', 'strawberry', 'banana')  ##Tuples
print(type(fruit))  #type check
print(pizza_toppings[1]) # List access value
pizza_toppings.append('Mushrooms')  #List add value
print(person['name'])  #Dictionary access value
person['name'] = 'George'  #Dictionary change value
person['eye_color'] = 'blue'   #Dictoary add value
print(fruit[2]) #access tuple

if num1 > 45:   # conditional if, else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:    #conditional if, else if length check
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):   #for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):  #for loop increment
    print(x)
x = 0
while(x < 5):    #while loop
    print(x)
    x += 1      #while loop increment

pizza_toppings.pop()  #list delete last value
pizza_toppings.pop(1)  #list delete second value

print(person)   
person.pop('eye_color')  #dictionary delete key/value
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue                        #For loop continue
    print('After 1st if statement')
    if topping == 'Olives':
        break                           #For loop break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):   #function
    for num in range(x):      #function argument
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)



"""
Bonus section
"""

# print(num3)      NameError: name <variable name> is not defined
# num3 = 72
#fruit[0] = 'cranberry'      # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    KeyError: 'favorite_team'
# print(pizza_toppings[7])      IndexError: list index out of range
#   print(boolean)       IndentationError: unexpected indent
# fruit.append('raspberry')  AttributeError: 'tuple' object has no attribute 'append'
#fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
y = list(fruit)
y.append('orange')
y.pop(2)
y[0]='watermelon'
fruit = tuple(y)