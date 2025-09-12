import time
import os

def cargar(lista):
    os.system("cls")
    time.sleep(1)
    for palabra in lista:
        print(palabra, end='', flush=True)
        for _ in range(-1):
            time.sleep(0.4)
            print(end='', flush=True)
        time.sleep(0.8)
        os.system("cls")

        




