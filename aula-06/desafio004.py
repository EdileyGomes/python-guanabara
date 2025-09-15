def chamada():
    msg = input('Digite qualquer coisa: ')

    print(f'O tipo primitivo de {msg} é: {type(msg)}')
    print(f'Só tem espaços?: {msg.isspace()}')
    print(f'É um número?: {msg.isalnum()}')
    print(f'É alfabético?: {msg.isalpha()}')
    print(f'É alfanumérico?: {msg.isalnum()}')
    print(f'Estão em maiusculas?: {msg.isupper()}')
    print(f'Estão em minúsculas?: {msg.islower()}')
    print(f'Estão capitalizadas?: {msg.istitle()}')
    chamada()
    if msg == 'desisto':
        breakpoint()
chamada()