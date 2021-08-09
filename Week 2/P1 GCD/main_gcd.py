import random
import sys
import os

number_test = int(sys.argv[1])
#fill = "*"*100
for i in range(number_test):
    #print("Test # ",str(i))
    if i%20==0:
        print("Test # ",str(i))
    os.system("python Generator.py " + str(i) + " > input.txt")

    #with open('input.txt') as f:
     #   numeros = f.readlines()
    #for i in range(2):
     #   print("number {}: {}".format(i+1,numeros[i]))

    os.system("python modelo.py <input.txt >model.txt")  # run model(alternative solution)
    os.system("python Euclidean.py <input.txt >main.txt")  # run main solution

    with open('model.txt') as f:
        model = f.read()
    #print("Model: ", model)
    # Leer salida de solucion principal
    with open('main.txt') as f:
        main = f.read()
    #print("Main: ", main)
    if model != main:
        break
