name = input("Please enter your name: ")
print("Hello, " + name + "!")

#input multilinhas
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)


#int(height) converte o valor de entrada em uma representação numérica
#antes de fazer a comparação
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


#para ver se é par ou impar se usa o modulo % se for 0 é divisivel
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
