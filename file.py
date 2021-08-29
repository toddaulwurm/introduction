num1 = 42 #variable declaration, init number
num2 = 2.3 #variable declaration, init number
boolean = True #variable dec, init boolean
string = 'Hello World'  #var dec, init string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list init
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary init
fruit = ('blueberry', 'strawberry', 'banana') #tupple init
print(type(fruit))       #log access tupple value
print(pizza_toppings[1]) #log access list value
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #log value in dictionary
person['name'] = 'George' #change value in dictionary
person['eye_color'] = 'blue' #change value in dictionary
print(fruit[2]) #log access tupple value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") # conditional  log number


if len(string) < 5: 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!") 
else:
    print("Just right!") #conditional log string

for x in range(5):
    print(x)        #for loop log 0-4
for x in range(2,5):
    print(x)  #for loop log 2-4
for x in range(2,10,3):
    print(x) #for loop 2-9 every 3rd value/ 2,5,8
x = 0
while(x < 5): #while loop log 0-4
    print(x)
    x += 1

pizza_toppings.pop() #delete value from list
pizza_toppings.pop(1) #delete value from list at index 1

print(person) #log dictionary
person.pop('eye_color') #delete key from dictionary
print(person) #log dictionary

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':   #conditional of list value
        continue                 #log string
    print('After 1st if statement')
    if topping == 'Olives': #conditional of list value
        break # end loop

def print_hello_ten_times(): """Function init Hello
                                            x10"""
    for num in range(10): #function parameter for loop
        print('Hello') #function return log string

print_hello_ten_times() #call function

def print_hello_x_times(x): #function parameter for loop and return
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #call function

def print_hello_x_or_ten_times(x = 10): #function parameter for loop  and return
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()  #call functions
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) no variable
# num3 = 72 
# fruit[0] = 'cranberry'  not a list
# print(person['favorite_team']) no key
# print(pizza_toppings[7]) out of range
#   print(boolean)         indent
# fruit.append('raspberry') not a list
# fruit.pop(1)   not a list


name = "Zen"
print("My name is", 5)

name = "Zen"
print("My name is " + 5)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.