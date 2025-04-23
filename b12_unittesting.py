import unittest

# def add(a,b):
#     return a+b


# normally we test this code by givving some input
# res = add(10,20)
# print(res)

# but here we are not handling error,so client cant understand
# and if i check this code after a year so i cant remember ,so we make a skaleton


# unit testing ke liye yek class banana hota hai

# class AddTest(unittest.TestCase):  #test class
#     def test_with_two_integer(self):   #starts with test    #test case
#         res = add(10,88)
#         self.assertEqual(res,98)  #ine is actual value and another is expected value

# if __name__ == "__main__":
#     unittest.main()   #called as tes runner

# op:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# function starts with test so,pythnon undrstand testing ho rahi hai
# in asertequal we are checking both values equal or not
# in result we got . means successfull,
# we define one function means one testing define
# this class is called as test class
# all one function called one test case
# got in result means one test ran
# ok means successful

# now lets see example for fail
# def add(a,b):
#     return a*b

# class AddTest(unittest.TestCase):
#     def test_with_two_integer(self):
#         res = add(10,88)
#         self.assertEqual(res,98)

# if __name__ == "__main__":
#     unittest.main()
#     op:
#     F
# ======================================================================
# FAIL: test_with_two_integer (__main__.AddTest.test_with_two_integer)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "e:\python  class new\python pratice b12\non technical\b12_unittesting.py", line 49, in test_with_two_integer
#     self.assertEqual(res,98)
#     ~~~~~~~~~~~~~~~~^^^^^^^^
# AssertionError: 880 != 98

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)


# in output we got f--means failure


# code refactor:
# first we write some code,then test and after failure we correct it called as code refactor .

# this approach is called as TDD--test driven development

# TDD:
# life is a cycle but in testing life is a triangle,means once we got requirement ,we do testing and developement paralelly.

# eg for errors


# class AddTest(unittest.TestCase):
#     def test_with_two_integer(self):
#         res = add(10,88)
#         self.assertEquall(res,98)

# if __name__ == "__main__":
#     unittest.main()
# op:
# E
# ======================================================================
# ERROR: test_with_two_integer (__main__.AddTest.test_with_two_integer)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "e:\python  class new\python pratice b12\non technical\b12_unittesting.py", line 91, in test_with_two_integer
#     self.assertEquall(res,98)
#     ^^^^^^^^^^^^^^^^^
# AttributeError: 'AddTest' object has no attribute 'assertEquall'. Did you mean: 'assertEqual'?

# ----------------------------------------------------------------------
# Ran 1 test in 0.004s

# FAILED (errors=1)


# ok-- .
# FAILED--F   -expected and actual different
# ERRORS--E--code mai koi runtime error ya test code me runtime error aya to


# test karte karte we are developing,so we got robust code,means very less chances to got error

# TDD approach:
# add a test
# execute test
# make changes to code
# execute test

# --------------
# we can add multiple test cases in a single class


# class AddTest(unittest.TestCase):
#     def test_with_two_integer(self):
#         res = add(10,88)
#         self.assertEqual(res,98)

#     def test_with_two_str(self):
#         res = add("abc", "xyz")
#         self.assertEqual(res,"abcxyz")

# if __name__ == "__main__":
#     unittest.main()
# op:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# OK

# sare test cases mila ke ham usko bolenge testsuite

# test fixture
# ----

# test with multiple


# class AddTest(unittest.TestCase):
#     def test_with_two_integer(self):
#         res = add(10,88)
#         self.assertEqual(res,98)

#     def test_with_two_str(self):
#         res = add("abc", "xyz")
#         self.assertEqual(res,"abcxyz")

#     def test_with_str_int(self):
#         res = add("abc", 10)
#         self.assertEqual(res,"addition of int and string is not allowed")

# if __name__ == "__main__":
#     unittest.main()
#     op:
#     E..
# ======================================================================
# ERROR: test_with_str_int (__main__.AddTest.test_with_str_int)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "e:\python  class new\python pratice b12\non technical\b12_unittesting.py", line 168, in test_with_str_int
#     res = add("abc", 10)
#   File "e:\python  class new\python pratice b12\non technical\b12_unittesting.py", line 4, in add
#     return a+b
#            ~^~
# TypeError: can only concatenate str (not "int") to str

# ----------------------------------------------------------------------
# Ran 3 tests in 0.002s

# FAILED (errors=1)


# first two functions are corrected,then also why at start we got E,
# becoz testcases alphabetical order mai run hote hai,means in function name it search by alphabetically

# and now we put add function in try and catch


# def add(a, b):
#     try:
#         return a + b
#     except TypeError:
#         return "addition of int and string is not allowed"


# class AddTest(unittest.TestCase):
#     def test_with_two_integer(self):
#         res = add(10, 88)
#         self.assertEqual(res, 98)

#     def test_with_two_str(self):
#         res = add("abc", "xyz")
#         self.assertEqual(res, "abcxyz")

#     def test_with_str_int(self):
#         res = add("abc", 10)
#         self.assertEqual(res, "addition of int and string is not allowed")


# if __name__ == "__main__":
#     unittest.main()
# op:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK


# ---------------------------------------------------------------
# another example
def bool_fun(name):
    if name == "aparna":
        return True
    else:
        return False


# class BoolFunctionTest(unittest.TestCase):
#     def test_with_correct_value(self):
#         self.assertEqual(bool_fun("aparna"), True)


# if __name__ == "__main__":
#     unittest.main()
#     op:
#     .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# if i want to run only one 
# infront of terminal line give file path and class name "non technical\b12_unittesting.py" BoolFunctionTest 
# this concept is similar to command line argument

# for two give two names
    
#     for single function
# copy file path give classname.function_name

# # eg.
# class BoolFunctionTest(unittest.TestCase):
#     def test_with_correct_value(self):
#         self.assertTrue(bool_fun("aparna"))

# if __name__ == "__main__":
#     unittest.main()



# we can do asertNotEqueal as well

# search assert in unittesting in pythonn