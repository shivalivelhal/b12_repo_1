#Its a High level language
# Platform Independent
# Portable
# Dynamically Typed


#Data Types (14 datatypes in python)

# A data type in programming refers to the classification of data that specifies the type of value a variable can hold and determines the operations that can be performed on that value. In Python, data types are dynamically inferred,meaning you don’t need to explicitly declare them.

#NUMERIC
    # 10 20 ---int
    # 10.23 12.12 44.55 ---float
    # 10+9j ---complex

# True Flase ---boolean
# none ---None
#SEQUNCE COLLECTION
    # [l,2,3,4,5,5,7,7]  ---list changable/muteable

    # {11,22,33,44,55,66}  ---set  changable/muteable

    # ( 10,20,30,40) ---tuple  unchangable/immuteable

    # ---byte
    # ---bytearray

    # range(1,51)

    # string -- "hello"

    # dictinary --- {"id":1,"name":"rosh","addres": "kop"}  ---- key value pair 

    # frozenset
# --------------------------------------------------
# type() its used to check the type of the variable

# --------- DataType Practices --------

# a=10
# print(a)            10
# print(type(a))      <class 'int'>

# a=1
# print(a)
# a= 44
# print(a)   # it takes the latest value of a

# A=10
# print(A)  # it is case sensitive lang

# # Type
# a=10
# print(a)
# print(type(a)) # <class 'int'>

# a=12.3
# print(a)
# print(type(a)) #<class 'float'>

# c=10+7j
# print(c)
# print(type(c))  #<class 'complex'>

# r=True
# print(type(r)) #<class 'bool'>

# r=None
# print(type(r))  #<class 'NoneType'>        

# l=[1,2,3,4,5,5,7,7]
# print(type(l))  #<class 'list'>

# s={11,22,33,44,55,66}
# print(type(s))  #<class 'set'>

# dist={"id":1,"name":"rosh","addres": "kop"}
# print(type(dist))  #<class 'dict'>

# t=(1,2,3,4,5)
# print(type(t)) #<class 'tuple'>

# a ="dfghjuyd"
# print(type(a)) #<class 'str'>

# #-------------------------------------------------
#IDENTIFIRES

# In Python, identifiers are the names used to identify variables,functions, classes, or other objects in your code. 

# Rules to Define Indentifires
# Can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# Must start with a letter or underscore, not a digit.
# Case-sensitive (Variable and variable are different).
# Cannot use reserved keywords (e.g., if, class, def).
# Cannot contain spaces or special characters (e.g., @, #, -).
# No length limit, but keep them meaningful.
# Underscore usage conventions:
#    _var: Private by convention.
#    __var: Name mangling.
#    __init__: Reserved for special methods.

# a="rosh"
# print(a)

# b="abc"
# print(b)

# sum12_ = 12
# print(sum12_)

# _sum = 12
# print(_sum)
##----------------------------------------------------------------------

# Keywords in Python
# Python keywords are reserved words that have predefined meanings and cannot be used as identifiers (variable names, function names, etc.). They are case-sensitive.

# import keyword
# print(keyword.kwlist)


# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

##--------------------------------------------------------------

# Memory Location in Python
# id() Function: Use id(obj) to get the memory address of an object.
# x = 10
# print(id(x))  # Memory address of x
# ""b = input("enter the value of b = ")
# print(b)
# a= float(input("Enter the value of a = "))
# print(a)""
# a= float(input("Enter the value of a = "))
# b = int(a)
# print(a)
# print(b)

# a= int(float(input("Enter the value of a = ")))
# print(a)
# int()
# float()
# str()

a

