from pet import Pet

def main():
    print("Creating pet: Fluffy")
    pet = Pet("Fluffy")
    
    pet.eat()
    pet.play()
    pet.sleep()
    
    pet.train("roll over")
    pet.train("play dead")
    
    pet.get_status()
    pet.show_tricks()

if __name__ == "__main__":
    main()