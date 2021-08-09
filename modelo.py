def modelo(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return a

a = int(input())
b= int(input())

print(modelo(a,b))