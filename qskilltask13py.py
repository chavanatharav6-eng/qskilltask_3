import numpy as np


# Function to take matrix input
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"\nEnter values for {name} row by row:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))

        matrix.append(row)

    return np.array(matrix)


# Display matrix
def display_matrix(matrix):
    print("\nResult:")
    print(matrix)


# Addition
def addition(A, B):
    if A.shape != B.shape:
        print("\nError: Matrices must have the same dimensions.")
        return

    result = A + B
    display_matrix(result)


# Subtraction
def subtraction(A, B):
    if A.shape != B.shape:
        print("\nError: Matrices must have the same dimensions.")
        return

    result = A - B
    display_matrix(result)


# Multiplication
def multiplication(A, B):
    if A.shape[1] != B.shape[0]:
        print("\nError: Number of columns of A must equal number of rows of B.")
        return

    result = np.dot(A, B)
    display_matrix(result)


# Transpose
def transpose(A):
    result = A.T
    display_matrix(result)


# Determinant
def determinant(A):
    if A.shape[0] != A.shape[1]:
        print("\nError: Determinant is only possible for a square matrix.")
        return

    result = np.linalg.det(A)

    print("\nDeterminant:")
    print(round(result, 2))


# Main program
print("=" * 45)
print("       MATRIX OPERATIONS TOOL")
print("=" * 45)

print("\nEnter Matrix A")
A = input_matrix("Matrix A")

print("\nEnter Matrix B")
B = input_matrix("Matrix B")


while True:

    print("\n" + "=" * 45)
    print("              MENU")
    print("=" * 45)

    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Determinant of Matrix A")
    print("7. Determinant of Matrix B")
    print("8. Display Matrices")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        addition(A, B)

    elif choice == "2":
        subtraction(A, B)

    elif choice == "3":
        multiplication(A, B)

    elif choice == "4":
        transpose(A)

    elif choice == "5":
        transpose(B)

    elif choice == "6":
        determinant(A)

    elif choice == "7":
        determinant(B)

    elif choice == "8":
        print("\nMatrix A:")
        print(A)

        print("\nMatrix B:")
        print(B)

    elif choice == "9":
        print("\nThank you for using Matrix Operations Tool!")
        break

    else:
        print("\nInvalid choice. Please select 1-9.")