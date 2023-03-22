from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def devide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devide,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number?\n"))
  exit_calculator = False
  while exit_calculator == False:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above:\n")
    num2 = float(input("What's the second number?\n"))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {round(answer)}")
    next_question = input(f"Do you want to continue with {answer}? Print 'y' or 'n'\n")
    if next_question == "y":
      num1 = answer
    if next_question == "n":
      exit_calculator = True
      calculator()

calculator()