class GiftRegistry:
    def __init__(self):
        self.gifts = []

    def add_gift(self, gift):
        self.gifts.append(gift)

    def view_registry(self):
        print("Gift Registry:")
        if not self.gifts:
            print("No gifts in the registry.")
        else:
            for i, gift in enumerate(self.gifts, start=1):
                print(f"{i}. {gift}")

def main():
    gift_registry = GiftRegistry()

    while True:
        print("\nGift Registry Menu:")
        print("1. Add gift")
        print("2. View registry")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            gift = input("Enter the gift: ")
            gift_registry.add_gift(gift)
            print("Gift added to the registry!")

        elif choice == '2':
            gift_registry.view_registry()

        elif choice == '3':
            print("Exiting the gift registry. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
