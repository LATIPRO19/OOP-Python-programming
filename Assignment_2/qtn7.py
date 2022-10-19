
year = 2022
default= 'Latif'
def roman_details():
    [name, birth_year, weight]
name = input('What is your name?....')
birth_year = int(input('Enter your birth year?...'))

if birth_year == 2002:
    if not name:
        name = default
weight= int(input('What is your weight?....'))
print('Your name is....',name)
print('Born in ',birth_year)
print('With a weight of.... ',weight,'kgs')

age =(year - birth_year)
print('Your age is', age)
roman_details()
