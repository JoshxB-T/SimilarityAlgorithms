def main():
    print("480 Practice Similairty Algorithms")
    print("----------------------------------")
    print("1. Inner Product")
    print("2. Cosine Similairity")
    print("3. L-1 Norm")
    print("4. Euclidean Distance")
    print("5. L-Infinity Norm")
    print("X. Exit")

    choice = input("Select an option (1-5): ")

    while choice != 'X':
        if choice == '1':
            print("You selected Inner Product.")
        elif choice == '2':
            print("You selected Cosine Similairity.")
        elif choice == '3':
            print("You selected L-1 Norm.")
        elif choice == '4':
            print("You selected Euclidean Distance.")
        elif choice == '5':
            print("You selected L-Infinity Norm.")
        else:
            print("Invalid choice. Try again.")
        choice = input("Select an option (1-5) or 'X' to exit: ")

    print("Exiting the program.")

if __name__ == "__main__":
    main()