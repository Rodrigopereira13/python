# Uma implementação de solução para o exercício acima. 

def isPalindrome(str):
  str = str.lower()
  if str == str[::-1]:
    return True
  else:
    return False


# Solicitar ao usuário que introduza a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if isPalindrome(userInput):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")
    
if __name__ == "__main__":
    main()


# Declarar uma nova tupla, nome "person"
person  = ('Jane','Doe', 21)

# "Pacote"/associar cada elemento da tupla com uma etiqueta. Observe a ordem das etiquetas.
first, last, age = person

print(first)


