

def division(x,y):
    try:
        result = x//y  # it roundups to decimal val
        print("your answer is :", result)
    except ZeroDivisionError:
        print(ArithmeticError)    
    except Exception as e:
       print(f"An error occurred: {e}")  # creates a string where the value of the expression inside the curly braces {e} is evaluated and inserted into the string.
    finally:
      print("Execution of division operation is complete.")
division(30,11)           
division(30,17)           
