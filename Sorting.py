import math


def create_halved_2d_array():
    # Here, we keep asking for numbers until tama na yung input nila
    while True:
        try:
            # We ask for numbers separated by space
            arr = [int(x) for x in input("Input numbers in the range 0-100, separated by space: ").split()]
            # Check natin kung pasok lahat sa range
            if all(0 <= num <= 100 for num in arr):
                break
            else:
                print("Please input numbers only in the range 0-100!")
        except ValueError:
            print("Invalid input! Please enter integers only.")
    # Print natin yung original na array
    print("Original na array:", arr)
    return arr


def merge_sort(arr, sort_order):
    print(f"Sorting: {arr}")
    # Dito sa algorithm na 'to, we're gonna divide and conquer
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, sort_order)
        merge_sort(R, sort_order)

        print(f"Merging: {L} and {R}")

        i = j = k = 0

        while i < len(L) and j < len(R):
            # Ascending ba or descending?
            if sort_order == "ASC":
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            else:
                if L[i] >= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(f"Merged: {arr}")



def create_2d_array(arr):
    # Calculate natin yung dimensions ng 2D array
    n = len(arr)
    divisor = int(math.sqrt(n))
    divisor = max(1, divisor)
    sub_array_length = n // divisor
    # Dito na natin ginagawa yung 2D array by dividing yung 1D array
    result = [arr[i:i+sub_array_length] for i in range(0, n, sub_array_length)]
    return result


def print_sorted_2d_array(arr):
    # Print natin yung sorted 2D array
    print("[", end="")
    for i in range(len(arr)):
        if i > 0:
            print(", ", end="")
        print("[", end="")
        for j in range(len(arr[i])):
            print(arr[i][j], end="")
            if j < len(arr[i]) - 1:
                print(", ", end="")
        print("]", end="")
    print("]")


if __name__ == '__main__':
    # Dito na tayo sa main program execution
    print("Enter elements for the array:")
    # Gawa tayo ng 1D array
    arr_1d = create_halved_2d_array()

    while True:
        # Piliin nila kung pa-ascend o pa-descend
        order = input("Choose order: (ASC)-Ascending/(DESC)-Descending: ").upper()
        if order in ["ASC", "DESC"]:
            break
        else:
            print("Invalid Input!")

    # Ayusin natin yung 1D array
    merge_sort(arr_1d, order)

    # Convert natin yung sorted 1D array sa 2D array
    arr_2d = create_2d_array(arr_1d)

    print("\nSorted  2D array:")
    print_sorted_2d_array(arr_2d)
