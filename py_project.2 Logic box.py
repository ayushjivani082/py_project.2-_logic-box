# =========================================================================

# LOGIC BOX - PATTERN GENERATOR & NUMBER ANALYZER

# =========================================================================

# Concepts covered:
# input() , print() , variables , int() , if/elif/else , for , while ,
# range() , nested loops , break , continue , pass , function ,
# menu-driven program ,, validation and basic error handling.

#===========================================================================

def title(text):
    print("\n" + "=" * 65)
    print(text.center(65))
    print("=" * 65)

#===========================================================================

# PATTERN GENERATOR

#==========================================================================
def pattern_generator():
    title("PATTERN GENERATOR")

    while True:
        print("\nChoose a pattern:")
        print("1. Right-Angled Star Triangle")
        print("2. Number Triangle")
        print("3. Inverted Star Triangle")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "4":
            break

        if choice not in ("1", "2", "3"):
            print("Invalid choice! Please try again.")
            continue

        while True:
            try:
                rows = int(input("Enter number of rows: "))

                if rows <= 0:
                    print("Rows must be greater than 0.")
                    # break is intentionally used to stop invalid pattern generation
                    break

                title("GENERATED PATTERN")

                # Nested loops: outer loop controls rows,
                # inner loop controls columns/items in each row.
                if choice == "1":
                    for i in range(1, rows + 1):
                        for j in range(i):
                            print("*", end=" ")
                        print()

                elif choice == "2":
                    for i in range(1, rows + 1):
                        for j in range(1, i + 1):
                            print(j, end=" ")
                        print()

                elif choice == "3":
                    for i in range(rows, 0, -1):
                        for j in range(i):
                            print("*", end=" ")
                        print()

                break

            except ValueError:
                print("Please enter a valid whole number.")
                continue


# ==============================================================
# NUMBER ANALYZER
# ==============================================================

def number_analyzer():
    title("NUMBER ANALYZER")

    while True:
        try:
            start = int(input("Enter start number: "))
            end = int(input("Enter end number: "))

            if end < start:
                print("Error: End number must be greater than or equal to start.")
                continue

            if end == start:
                print("Only one number was entered. Analysis will still be performed.")

            total = 0
            odd_count = 0
            even_count = 0

            print("\nNumber Analysis:")
            print("-" * 65)

            # range() is used to generate numbers in the requested range.
            for number in range(start, end + 1):

                # continue demonstrates skipping a selected number.
                if number == 0:
                    print("Number 0 is neither Odd nor Even for this project.")
                    total += number
                    continue

                if number % 2 == 0:
                    print(f"Number {number} is Even")
                    even_count += 1
                else:
                    print(f"Number {number} is Odd")
                    odd_count += 1

                total += number

            print("-" * 65)
            print("Total Even Numbers:", even_count)
            print("Total Odd Numbers :", odd_count)
            print("Sum of all numbers:", total)

            # pass is used as a placeholder for future analysis features.
            if total >= 0:
                pass

            break

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue


# ==============================================================
# MAIN MENU
# ==============================================================

def main():
    title("WELCOME TO LOGIC BOX")
    print("Pattern Generator & Number Analyzer")
    print("This project demonstrates Python control structures.")

    while True:
        title("MAIN MENU")

        print("1. Pattern Generator")
        print("2. Number Analyzer")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            pattern_generator()

        elif choice == "2":
            number_analyzer()

        elif choice == "3":
            title("EXIT")
            print("Thank you for using Logic Box!")
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")
            continue


# Program starts here
main()

         
