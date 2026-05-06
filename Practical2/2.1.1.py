def main():
    numbers = []

    while True:
        # print("Menu:")
        print("1. Add")
        print("2. Remove")
        print("3. Display")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == '1':
            value = input("Integer: ")
            try:
                num = int(value)
                numbers.append(num)
                print(f"List after adding: {numbers}")
            except ValueError:
                print("Invalid input")

        elif choice == '2':
            if not numbers:
                print("List is empty")
            else:
                value = input("Integer: ")
                try:
                    num = int(value)
                    if num in numbers:
                        numbers.remove(num)
                        print(f"List after removing: {numbers}")
                    else:
                        print("Element not found")
                except ValueError:
                    print("Invalid input")

        elif choice == '3':
            if not numbers:
                print("List is empty")
            else:
                print(numbers)

        elif choice == '4':
            # print("Exiting program...")
            break

        else:
            print("Invalid choice")


# Run the program
main()
	
	
		
