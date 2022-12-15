class MyException(Exception):
  pass

def ask_for_number():
  while True:
    try:
      number = int(input("Enter a whole number: "))

      if number > 10:
        raise MyException("Number must be less than or equal to 10")

      return number
    except ValueError:
      print("Please enter a valid whole number")
    except MyException as e:
      print(e)