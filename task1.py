import numpy as np
import itertools


def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix


def calculateProductsOfPermutations(l_permutations, m_matrix):
    """
    Calculates the products of elements from a matrix based on a list of permutations.

    This function computes the product of matrix elements selected by each permutation in
    `l_permutations`, while adjusting the product's sign according to the permutation's
    inversion count (multiplies by -1 for each inversion). For each permutation, it selects
    matrix elements from the row `u_row_index` and column `u_column_index` where
    `u_column_index` is determined by the permutation.

    Args:
        l_permutations (list of lists): A list of permutations, where each permutation is
            a list of integers representing a sequence of column indices.
        m_matrix (list of lists): A square matrix (2D list) of numbers.

    Returns:
        list: A list of products, one for each permutation, representing the product of
        matrix elements selected by the permutation and adjusted for the number of inversions.
    """
    l_products = list()

    for l_permutation in l_permutations:
        i_product = 1

        for i in range(0, len(l_permutation)):
            for j in range(i + 1, len(l_permutation)):
                if l_permutation[i] > l_permutation[j]:
                    i_product *= -1

        for u_row_index in range(0, len(l_permutation)):
            u_column_index = l_permutation[u_row_index]

            i_product *= m_matrix[u_row_index][u_column_index]

        l_products.append(i_product)

    return l_products


def sumOfList(l_values):
    """
    Calculates the sum of all elements in a list.

    This function iterates through a list of numeric values and returns the total sum of
    its elements.

    Args:
        l_values (list): A list of numeric values to be summed.

    Returns:
        int or float: The sum of all values in the list.
    """
    i_sum = 0
    for i_value in l_values:
        i_sum += i_value
    return i_sum


def readNatural(prompt):
    """
    Reads a natural number (positive integer) from user input, with error handling.

    This function repeatedly prompts the user for input until a valid natural number (a
    positive integer) is entered. It handles invalid input (non-integer values or negative
    numbers) by printing an appropriate message and retrying. If the user enters "exit" or
    interrupts the input (via `Ctrl+C`), the function returns "exit".

    Args:
        prompt (str): The prompt string displayed to the user.

    Returns:
        int or str: The natural number entered by the user, or "exit" if the user chooses to
        exit.
    """
    s_input = ''
    i_value = 0
    while True:
        try:
            s_input = input(prompt)
        except KeyboardInterrupt:
            return "exit"
        if s_input == "exit":
            return "exit"
        try:
            i_value = int(s_input)
        except ValueError:
            print("Enter the value consisting of digits [0-9]")
            continue
        if i_value <= 0:
            print("Value must be positive")
            continue

        return i_value


def createPermutationsList(u_dimensions):
    """
    Generates a list of all possible permutations for a given number of dimensions.

    This function creates a list of integers ranging from 0 to `u_dimensions - 1`, then
    returns a list of all possible permutations of those integers.

    Args:
        u_dimensions (int): The number of dimensions or elements to permute.

    Returns:
        list of tuples: A list containing all permutations of the integers from 0 to
        `u_dimensions - 1`. Each permutation is represented as a tuple.
    """
    l_columns = list()
    for u_row_index in range(0, u_dimensions):
        l_columns.append(u_row_index)
    return list(itertools.permutations(l_columns))


while True:
    print("Enter 'exit' to quit")
    matrix_dimensions = readNatural("Enter the dimesnions of square matrix: ")
    if matrix_dimensions == "exit":
        break

    matrix = random_matrix(matrix_dimensions)
    det = sumOfList(calculateProductsOfPermutations(createPermutationsList(matrix_dimensions), matrix))

    print("matrix:\n", matrix)
    print("determinant:", det)
    # print("determinant np:", np.linalg.det(matrix))
