n = 17
# final n binary length
max_len = len(bin(n)[2:])
for i in range(1, n + 1):
    binary = ""
    while i > 0:
        rem = i%2
        binary = str(rem) + binary  
        i = i//2
    spaces = max_len - len(binary)

    print(" " * spaces + binary)