# Question 1 - Write a function to print "Hello USERNAME"

def hello_name(name):
    print("Hello " + name.title())

hello_name("thomas")

# Question 2 - Print the first odd numbers between 1 and 100

def first_odds():
    i = 0
    while i(i<100):
        if i % 2 != 0:
            print(i, end=' ')
        i = i + 1

# Question 3 - Write a function that returns the max number in a given list

def max_num_in_a_list(a_list):
    return max(a_list)

# Question 4 - Write a function that returns True if the given year is a leap year

def is_a_leap_year(a_year):
    if a_year % 400 == 0 or a_year % 100 and a_year % 4 == 0:
        return True
    else:
        return False

# Question 5 - Write a function to check to see if all numbers in list are consecutive numbers.

def is_consecutive(a_list):
    