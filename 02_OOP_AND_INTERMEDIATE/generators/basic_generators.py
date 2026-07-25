"""
Generators

Unlike a list, a generator doesn't hold the entire results/values in memory.
It yields each result when needed.
The keyword 'next()` yields the next result and so will have to be written for as many times as the number of values;

E.g for [1,2,3,4,5]

        next()          # yields 1
        next()          # yields 2
        next()          # yields 3
        next()          # yields 4
        next()          # yields 5

If the next statement exceeds the number of values, an exception "StopIteration" is thrown.
    
"""
# This is normally a function that appends a list of numbers into an empty list
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)

# For a generator the syntax is different

def square_numbers(nums):
    # We do not need an empty list
    for i in nums:
        yield (i*i)    # this keyword signifies that it is a generator

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)              # returns a generator object
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# # Now, instead of printing multiple next statements we can use  for loop
# for num in my_nums:
#     print(num)


# We can use comprehension instead of the for loop function
my_nums = (x*x for x in [1,2,3,4,5,6])         # paranthesis is used for generator comprehension
# print(my_nums)
# for num in my_nums:
#     print(num)

# We can print the all the values at once by wrapping the generator in a list
print(list(my_nums))