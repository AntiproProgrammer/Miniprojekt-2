import random
import json

# Spellop
def spela_omgang():
    hemligt_tal = random.randint(1, 100)
    antal = 0

    while True:
        gissa = int(input("Gissa: "))
        antal += 1

        if gissa < hemligt_tal:
            print("For lagt!")
        elif gissa > hemligt_tal:
            print("For hogt!")
        else:
            print(f"Ratt! {antal} gissningar.")
            return antal

