# ===============================================================================
# Python Tutorial
# ===============================================================================

if 1 in [2,34]:
  print("In first IF")
elif 1 in [1,2]:
  if 1 in [1]:
    print("Inside nested elif")
  print("In elif")
else:
  print("In else")
  
x  = [3,4,5,6]
print(len(x))
x.append([10,11])
x.extend([12,34,67])

print(x)

x.insert(1, 100)
x.remove([10,11])

z = x.copy()
# z = x
z.clear()
# del z
print(x)
print(z)

x.sort()
x.reverse()
print(x)

print(x.count(5))

# Tuples are like lists but immutable
x = ( 1,2,3,5,7 )
print(x[1])
print(x.count(5))
print(len(x))
print(max(x))
print(min(x))

y  = ( 'max', 1, True)
print(y)

z = x + y
print(z)

a = ('repeat',) * 5
print(a)

# Set
a = {1,2,3,6,10,23, 3}
print(a)

a.add(100)
print(a)

a.update([15,92,23])
print(a)

# Throws error if element isnt present
a.remove(92)
print(a)

# No error if element isnt present
a.discard(100)
print(a)

a.pop()
print(a)

a.clear()
print(a)

a1 = set((10,20,50))
print(a1)

a2 = set([10,20,30,70])
print(a2)

print(a1 | a2)  # Union
print(a1.union(a2))

print(a1 & a2) # Inter
print(a1.intersection(a2))

print(a1-a2)
print(a1.difference(a2))
print(a2-a1)

print( a1 ^ a2 ) # Union - Intersection
print( a2.symmetric_difference(a1) )

print( dir (a1) )

# Dictionary

a = {"name": "max", "age": 15, "year": 2001}
print(a["age"])

for item, value in a.items():
    print(value)
    
a['new_key'] = "Added key"
print(a)

a.pop('name')
print(a)

a['new_key'] = "Updated key"
a.update({'age': 26})
print(a)

print(a.keys())
print(a.values())
print(a.items())

# Slice and negative index
a = [20, 40,120, 1, 230]

# start, end, step
print(a[2:])
print(a[:2])
print(a[::-1])

# negative value dictates direction, indexes remain the same
print (a)
print(a[-3::-1])

# Loops
# while loop
i = 1
while i < 4:
    print("value of i", i)
    i += 1
else:
    print("Always run after coming out of loop")

# for loop
a = [10,20,304]
b = (10,20,304)
c = { "a": 10, "b": 20, "c": 304}
d = {10,20,304}

for el in a:
    print(el)
for el in b:
    print(el)
for el in c:
    print(el)
for el in d:
    print(el)
else:
    print("Exiting for loop")

# break    
for el in a:
    if el == 20:
        break
    print(el)

# continue    
for el in a:
    if el == 20:
        continue
    print(el)
    
# function
print("\nFunction")
def functionWhichPrintsHi():
    print("HI")

functionWhichPrintsHi()

print("\n*args")
def functionwithargs(*args):
    print (args)
    for i in args:
        print(i)
        
print("\n**kwargs")
def functionwithkwargs(**kwargs):
    print (kwargs)
    for key, value in kwargs.items():
        print(key, value)
        
functionwithargs("max", 10, 2000)
functionwithkwargs(name="max", age=10, year=2000)

# Classes
print("\nClasses")
class FirstClass:
    pass # Pass is used to denote empty class, or can be used in methods

# can add attributes on the fly for pass classes
fobject = FirstClass()
fobject.attr1 = 10
fobject.attr2 = "name in object"
fobject.attr3 = 404

print(fobject.attr2)

# init and self
# cannot have multiple init methods, last defined is the one which will be used
print("\nInit and self")
class SecondClass:
    def __init__(self, firstarg, secondarg):
        print("SecondClass Object has been created")
        print(firstarg)
        print(secondarg)
        
        self.firstarg = firstarg
        self.secondarg = secondarg
        
sobject = SecondClass("name", 40)
print(sobject.firstarg)

# encapsulation
print("\nEncapsulation")
class EncapClass:
    __speed = None
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
        print("Encap class init")
        
    def set_speed(self, speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed
    
encapobj = EncapClass("MS", 30)

encapobj.set_speed("200")
encapobj.__speed = 800
# print(encapobj.__speed)
print(encapobj.get_speed())


# Private method
print("Private method")
class PrivateMethodClass:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
        self.__cal_speed() # private method accesible within class
        
    def set_speed(self, speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed
    
    def __cal_speed(self):
        print(self.__speed * 9.5)
    
pmclass = PrivateMethodClass("Toyota", 100)
# pmclass.__cal_speed() # Gives an error as missing attribute

# Inheritance
print("Inheritance")
class MyBaseClass:
    __name = None
    __age = None
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("MyBaseClass init")
        super().__init__(self.__name, 230)
        
    def set_values(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
        
class MySubClass(MyBaseClass):
    def __init__(self):
        super().__init__("Clive", 27)
        print("Sub class init")    
    def print_info(self):
        print( f'Name = {self.get_name()}, Age = {self.get_age()}')
        
# subobj = MySubClass()
# subobj.print_info()

# Multiple inheritance
print("\nMultiple inheritance")
class MultiInheritanceClass(MyBaseClass, EncapClass):
    def __init__(self):
        super().__init__("Clive", 27)

multiobj = MultiInheritanceClass()
print("Multiple inheritance")
print(multiobj.get_age())
print(multiobj.get_speed())

# __mro__ method resolution order
# shows the chain of methods which will be executed first

# composition is creating and using an object of a different class within a class as an instance variable
# part-of relationship
# where inheritance -> is-a relationship
# aggregation -> has-a relationship

# Abstract class
print("\nAbstract class")
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(): pass
    
    @abstractmethod
    def perimeter(): pass
    
class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return 4 * self.__side
    
square_obj = Square(10)
print(square_obj)

# Exception Handling
# import builtins
# help(builtins)
print("\nException Handling")
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Zero division error", type(e))
except Exception as e:
    print("Error -> ", e)
else:
    # Runs only if no exceptions occurs
    print("Else")
finally:
    # Runs always
    print("Finally")

# Iterator
print("\nIterator")
class IteratorExample:
    def __init__(self, list):
        self.__list = list
        self.__index = -1
        
    def __next__(self):
        self.__index += 1
        if( self.__index == len(self.__list)):
            raise StopIteration
        return self.__list[self.__index]   
    
    def __iter__(self):
        return self
    
example = IteratorExample([10,20,53,2,123])
it = iter(example)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

for i in it:
    print(i)
    
# Generators
print("\nGenerators")
def list_generator_yield(list_c):
    yield 'a'
    yield 'b'
    yield 'c'

it = list_generator_yield([10,123,534,12])
print(next(it))
print(next(it))
print(next(it))
        
def list_generator(list_c):
    for i in list_c:
        yield i
        
it1 = list_generator([10,123,534,12])
print(next(it1))

# Closures
print("\nClosures")

def exponent_func(exponent):
    def inner_func(base):
        print(base, exponent)
        
    return inner_func

a = exponent_func(10)
a(20)

# Decorators 
# Take a function as argument and return a function
print("\nDecorators")
def my_decorator(func):
    def line_printer(a):
        print("-"  * 40)
        func(a)
        print("-"  * 40)
        
    return line_printer

def outer_decorator(func):
    def outer_equal_print(args):
        print("="  * 40)
        func(args)
        print("="  * 40)
        
    return outer_equal_print

@outer_decorator
@my_decorator
def printHelloWith(something):
    print("Hello, World ", something)
    
printHelloWith("Random")

# Operator Overloading
print("\nOperator Overloading")
class OperatorOV:
    def __init__(self, speed):
        self.__speed = speed
        
    def __lt__(self, second_obj):
        return self.__speed < second_obj.__speed
    
obj1 = OperatorOV(200)
obj2 = OperatorOV(300)

print("Obj2 is faster") if obj1 < obj2 else print("Obj1 is faster")

# CLI arguments
print("\nCommand line arguments")
import argparse

parser = argparse.ArgumentParser()

# py py_tutorial.py --num 25 --iden 1 --position 16
# py py_tutorial.py -n 25 -id 1 -p 16
parser.add_argument('-n', '--num', help='Number', type=float )
parser.add_argument('-id', '--iden', help='ID', type=float, )
parser.add_argument('-p', '--position', help='Position', type=float)

args = parser.parse_args()
print(args.num, args.iden, args.position)
