def encode(text):
    with open('file.txt', 'w') as f:
        for a in text.encode('utf-8'):
            bits = format(a, '08b')
            for bit in bits:
                if(bit == '0'):
                    f.write(" ")
                if(bit == '1'):
                    f.write("\t")

text = input('\n[+] Codificar: ')
encode(text)
