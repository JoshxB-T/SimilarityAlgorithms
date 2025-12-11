def inner_product(list1, list2):
    result = 0

    for i in range(len(list1)):
        result += list1[i] * list2[i]

    return result

def cosine_similarity(list1, list2):
    result = 0;

    numerator = inner_product(list1, list2)

    denom1 = 0
    for x in list1:
        denom1 += x * x

    denom2 = 0
    for x in list2:
        denom2 += x * x

    result =  numerator / ((denom1 ** 0.5) * (denom2 ** 0.5))

    return result

def l1_norm(list1, list2):
    result = 0

    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])

    return result

def euclidean_distance(list1, list2):
    result = 0

    return result

def linf_norm(list1, list2):
    result = 0
    
    return result


def get_lists(choice):
    list1 = input("Enter the first list of numbers (comma-separated): ")
    list2 = input("Enter the second list of numbers (comma-separated): ")

    list1 = [float(x) for x in list1.split(',')]
    list2 = [float(x) for x in list2.split(',')]

    if choice == '1':
        print(f"Inner Product: {inner_product(list1, list2)}")
    elif choice == '2':
        print(f"Cosine Similarity: {cosine_similarity(list1, list2)}")
    elif choice == '3':
        print(f"L-1 Norm: {l1_norm(list1, list2)}")
    elif choice == '4':
        print(f"Euclidean Distance: {euclidean_distance(list1, list2)}")
    elif choice == '5':
        print(f"L-Infinity Norm: {linf_norm(list1, list2)}")
    else:
        print("Invalid choice. Try again.")

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

    while choice != 'X' and choice in ['1', '2', '3', '4', '5']:
        get_lists(choice)
        choice = input("Select an option (1-5) or 'X' to exit: ")

    print("Exiting the program.")

if __name__ == "__main__":
    main()