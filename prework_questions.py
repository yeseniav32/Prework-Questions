#Question 1 

def hello_name(user_name):
    print("Hello " + user_name.upper())

hello_name("Yesenia")

#Question 2 

def first_odds():
    for num in range(1,100):
        if num % 2 != 0:
            print(num)

first_odds()

#Question 3 

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list([175,20,35,4]))

#Question 4 

def is_leap_year(a_year):
    if a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 ==0:
        return True
    else:
        return False

print(is_leap_year(2027))
print(is_leap_year(2020))

