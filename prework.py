# Question 1

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")

# Question 2

def first_odds():
    for odd in range(1,100,2):
        print(odd)

first_odds()

# Question 3

def max_num_in_list(a_list):
    return max(a_list)

a_list = [1, 14, 21, 2, 11, 45, 90, 22, 71, 12]
print(max_num_in_list(a_list))

# Question 4

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(2025))

# Question 5

def is_consecutive(a_list):
    for index in range(1, len(a_list)):
        if a_list[index] != a_list[index-1] + 1:
            return False
    return True


consecutive = [1,2,3,4,5,6,7,8,9]
consecutive2 = [1,3,4,2]
non_consecutive = [3,1,6,7,2,7]

consecutive.sort()
consecutive2.sort()
non_consecutive.sort()

print(is_consecutive(consecutive))
print(is_consecutive(consecutive2))
print(is_consecutive(non_consecutive))