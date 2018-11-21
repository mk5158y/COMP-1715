run = True
cont = ""

def Add(num1, num2):
  print("Answer:", num1 + num2)

def Subtract(num1,num2):
  print("Answer:", num1 - num2)

def Multiply(num1, num2):
  print("Answer:", num1 * num2)

def Divide(num1, num2):
  print("Answer:", num1 / num2)

def Run():
  num1 = int(input("Enter your first number: ")) 
  num2 = int(input("Enter your second number: "))
  print("Please enter a number for your selected operation:")
  print("1 - Add")
  print("2 - Subtract")
  print("3 - Multiply")
  print("4 - Divide")
  opt = input("Enter a number: ")
  if opt == "1":
    Add(num1, num2)
  if opt == "2":
    Subtract(num1, num2)
  if opt == "3":
    Multiply(num1, num2)
  if opt == "4":
    Divide(num1, num2)
  else:
    print("Incorrect option selected!")

while run == True:
  Run()
  cont = input("Use program again [Y/N]: ")
  if cont == "Y" or cont == "y":
    run == True
  else:
    run = False
    print("End!")
    exit
  
