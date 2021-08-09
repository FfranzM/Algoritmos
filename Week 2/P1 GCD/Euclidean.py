
def EuclideanAlg(a,b):
    if b==0:
        return a
    else:
        r = a%b
        return EuclideanAlg(b,r)

a = int(input())
b= int(input())

print(EuclideanAlg(a,b))


