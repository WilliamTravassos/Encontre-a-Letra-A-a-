def separate_A_and_a(s):
    # Lista para armazenar as ocorrências de 'A'
    uppercase_a_list = [char for char in s if char == 'A']
    # Lista para armazenar as ocorrências de 'a'
    lowercase_a_list = [char for char in s if char == 'a']
    return uppercase_a_list, lowercase_a_list

# Opção 1: String pré-definida
# input_string = "Aqui está uma string de exemplo com letras A e a."

# Opção 2: Solicitar a entrada do usuário
input_string = input("Digite uma string para separar as letras 'A' e 'a': ")

# Separar as letras e exibir o resultado
uppercase_a_list, lowercase_a_list = separate_A_and_a(input_string)
print(f"As ocorrências da letra 'A' são: {uppercase_a_list}")
print(f"As ocorrências da letra 'a' são: {lowercase_a_list}")
print(f"Total de 'A': {len(uppercase_a_list)}")
print(f"Total de 'a': {len(lowercase_a_list)}")
