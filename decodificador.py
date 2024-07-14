def decode(file):
    with open(file, 'r') as f:
        data = f.read()
        for index in range(0, len(data), 8):
            letra = ""
            for char in data[index:index + 8]:
                if char == " ":
                    letra += '0'
                else:
                    letra += '1'
            letra = chr(int(letra, 2))
            print(letra, end='')

file = input('\n[!] Decodificar: ')
decode(file)
