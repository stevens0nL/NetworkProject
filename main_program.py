
from menu_functions import (
    binary_to_decimal_game,
    decimal_to_binary_game,
    classful_address_analysis,
    wildcard_mask_determination,
    save_results,
)

def display_menu():
    """
    Display the main menu.
    Pseudocode:
    1. Print menu options.
    2. Prompt the user for their choice.
    """
    print("\n=====================")
    print("       MAIN MENU")
    print("=====================")
    print("1. Binary to Decimal Conversion")
    print("2. Decimal to Binary Conversion")
    print("3. Classful Address Analysis")
    print("4. Wildcard Mask Determination")
    print("5. Exit")
    print("=====================")

def main():
    """
    Main program loop.
    Pseudocode:
    1. Display the menu.
    2. Execute the selected option.
    3. Exit the program when the user selects '5'.
    """
    running = True
    while running:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            binary_to_decimal_game()
        elif choice == "2":
            decimal_to_binary_game()
        elif choice == "3":
            classful_address_analysis()
        elif choice == "4":
            wildcard_mask_determination()
        elif choice == "5":
            save_results()
            print("\nThank you for using the program! Goodbye!")
            running = False
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

