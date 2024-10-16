
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')

except Exception as e:
    print(e)

else:
    print(" I run when there is no exception")

finally:
    print( " I always run")

'''
Below syntax is to catch the exception specifically

except TypeError:
    print('Type Error Occurred')

except ValueError:
    print('Value Error Occurred')

except ZeroDivisionError:
    print('Zero Division Error Occurred')
    
'''
