def grote_speler(speler: str, cijfer: int) -> bool:
    if cijfer >= 8:
        return True
    else:
        return False
        
        
if __name__ == "__main__":
    
    speler = input("Naam speler: ")
    cijfer = float(input("Cijfer wedstrijd: "))
    
    if grote_speler(speler, cijfer):
        print(f"Gefeliciteers {speler}, je bent een grote speler")
    else:
        print(f"{speler}, je bent een kleine bitch")