"""
1. Write a Python program to create a lambda function that adds 15
 to a given number passed in as an argument, also create a lambda 
 function that multiplies argument x with argument y and print the result.
"""
plusFifteen = lambda x: x + 15
print(plusFifteen(15))


"""
2. Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number.
"""
multiplier = lambda x, y: x * y
print(multiplier(15, 5))


"""
3. Write a Python program to sort a list of tuples using Lambda.
"""
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subjects.sort(key = lambda x: x[1])
print(subjects)

"""
4. Write a Python program to sort a list of dictionaries using Lambda
"""

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, 
{'make':'Mi Max', 'model':'2', 'color':'Gold'}, 
{'make':'Samsung', 'model': 7, 'color':'Blue'}]
models.sort(key = lambda x: x['color'])
print(models)

"""
5. Write a Python program to filter a list of integers using Lambda.
"""

ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenInts = list(filter(lambda x: x % 2 == 0, ints))
oddInts = list(filter(lambda x: x % 2 == 1, ints))
print('odds', oddInts)
print('evens', evenInts)