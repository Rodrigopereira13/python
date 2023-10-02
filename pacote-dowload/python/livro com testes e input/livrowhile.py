
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


responses = {}
# Define uma flag para indicar que a enquete está ativa
polling_active = True
while polling_active:
# Pede o nome da pessoa e a resposta
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
# Armazena a resposta no dicionário
#coloca name(key) com response sendo seu valor
    responses[name] = response
# Descobre se outra pessoa vai responder à enquete
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# A enquete foi concluída. Mostra os resultados
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
print(responses)

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    while True:
        print("\nPlease tell me your name:")
        f_name = input("First name: ")
        l_name = input("Last name: ")
        formatted_name = get_formatted_name(f_name, l_name)
        print("\nHello, " + formatted_name + "!")
        print("(enter 'q' at any time to quit)")
        if f_name == 'q':
            break
        if l_name == 'q':
            break