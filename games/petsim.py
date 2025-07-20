class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.cleanliness = 5
        self.age = 0

    def feed(self):
        self.hunger = max(self.hunger - 3, 0)

    def play(self):
        self.hunger = min(self.hunger + 1, 10)
        self.happiness = min(self.happiness + 2, 10)

    def clean(self):
        self.cleanliness = min(self.cleanliness + 1, 10)

    def pass_day(self):
        self.age += 1
        self.hunger = min(self.hunger + 1, 10)
        self.happiness = min(self.happiness - 1, 10)
        self.cleanliness = max(self.cleanliness - 0.5, 0)

    def is_alive(self):
        return self.hunger < 10 and self.cleanliness > 0

    def status(self):
        return f"{self.name} is hungry: {self.hunger}, happy: {self.happiness}, clean: {self.cleanliness}, and {self.age} years old."

def main():
    name = input("Enter your cat's name: ")
    pet = Pet(name)
    day = 1

    while True:
        print(f"\nDay {day}:")
        print(pet.status())
        choice = input("What do you want to do? (feed, play, clean): ").strip().lower()

        if choice == "feed":
            pet.feed()
        elif choice == "play":
            pet.play()
        elif choice == "clean":
            pet.clean()
        else:
            print("Invalid choice!")
            continue

        pet.pass_day()

        if not pet.is_alive():
            print(f"Your pet {pet.name} died on day {day}!")
            break

        day += 1

if __name__ == "__main__":
    main()
