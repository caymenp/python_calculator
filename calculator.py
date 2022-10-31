      print("Simple Math Calulator.")

      print("---------------------------------------------------------------------")
      
# First Number for User to Input.

  num_1 = input("Please Type Your First Number: ")

      print("---------------------------------------------------------------------")

      print("Type in the number for the type of calculation you want to do: ")

      print("---------------------------------------------------------------------")

      print("1 : Addition")
      print("2 : Subtraction")
      print("3 : Multiply")
      print("4 : Divide")

      print("---------------------------------------------------------------------")
      
# Where user selects from menu above for their calulation operator

  cal_variable = input()

      print("---------------------------------------------------------------------")
      
# Second Number for User to Input.

  num_2 = input("Please Type The Second Number: ")

      print("---------------------------------------------------------------------")

      print("Calulating................")
      
# Converts both user inputs to Floats.

  num_1 = float(num_1)
  num_2 = float(num_2)

# Creates the answer variable. Assigns value to 'none'.
  answer = None

      print("---------------------------------------------------------------------")
      
# Defining the functions for the math operator.

def addition(num_1, num_2):
    return num_1 + num_2
def subtraction(num_1,num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2
def divide(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        print("Cannot divide by 0, please choose another divisor.")


if cal_variable == '1':
    answer = addition(num_1, num_2)
elif cal_variable == '2':
    answer = subtraction(num_1, num_2)
elif cal_variable == '3':
    answer = multiply(num_1, num_2)
elif cal_variable == '4':
    answer = divide(num_1, num_2)
else:
    print("Please check your selections, and try again")

print("Your answer is:", answer)
