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
            print("For lågt!")
        elif gissa > hemligt_tal:
            print("For högt!")
        else:
            print(f"Rätt! {antal} gissningar.")
            return antal

# Ladda highscore från JSON
def ladda_highscore():
    try:
        with open("highscore.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Spara highscore till JSON
def spara_highscore(highscore):
    with open("highscore.json", "w", encoding="utf-8") as f:
        json.dump(highscore, f, indent=4, ensure_ascii=False)

# Visa highscore 
def visa_highscore(highscore):
    if not highscore:
        print("\nInga resultat ännu")
        return
    
    sorterad = sorted(highscore, key=lambda x: x["gissningar"])
    
    print("\n--- HIGHSCORE ---")
    for i, spelare in enumerate(sorterad, 1):
        print(f"{i}. {spelare['namn']} - {spelare['gissningar']} gissningar")

