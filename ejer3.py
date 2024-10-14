numero=int (input("Dame un numero:"))
print(type(numero))


for x in range(2,numero+1):
    if x % 2 == 0:
        print(x)