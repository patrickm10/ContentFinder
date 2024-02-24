"""
Python Script to guess a number and analyze the time complexity for each algorithm.
Author: Patrick Mejia
"""
import time


def brute_force_search(number: int):
    """
    Brute force search algorithm
    :param number: int
    :return: int
    """
    for i in range(number + 1):
        # Perform your search operation here
        # You can replace the print statement with your desired search logic
        # print(f"Searching number: {i}")
        if i == number:
            print(f"Number found: {i}")
            return i
        else:
            continue


def binary_search(number: int):
    """
    Binary search algorithm
    :param number: int
    :return: int
    """
    low = 0
    count = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        count += 1

        if mid == number:
            print(f"Number found in {count} attempts: {mid}")
            return mid
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Number not found in {count} attempts.")
    return None


def recursive_binary_search(number: int, low: int, high: int):
    """
    Recursive binary search algorithm
    :param number: int
    :param low: int
    :param high: int
    :return: int
    """
    count = 0
    if low <= high:
        mid = (low + high) // 2
        count += 1

        if mid == number:
            print(f"Number found: {mid}")
            print(f"Number found in {count} attempts: {mid}")
            return mid
        elif mid < number:
            return recursive_binary_search(number, mid + 1, high)
        else:
            return recursive_binary_search(number, low, mid - 1)
    else:
        print("Number not found")
        return None


# TODO: Write similar thing using binary search algorithm
def character_by_character_search(number: int):
    """
    Character by character search algorithm to guess an 8-digit number
    :param number: int - The 8-digit number to guess
    :return: int
    """
    # Convert the number to a string to get its length
    number_str = str(number)
    number_length = len(number_str)

    # Initialize an empty string to store the guessed digits
    guessed_digits_str = ""
    count = 0

    # Iterate over each position of the 8-digit number
    for position in range(1, number_length + 1):
        # Initialize a flag to indicate whether the digit is found
        digit_found = False

        # Iterate over each possible digit (0-9)
        for digit in range(10):
            # Perform your search operation here
            # You can replace the print statement with your desired search logic
            print(f"Character in position_{position}: {digit}")
            count += 1

            # Check if the guessed digit matches the digit at the current position in the number
            if str(digit) == number_str[position - 1]:
                # If the guess is correct, append it to the guessed digits string
                guessed_digits_str += str(digit)
                digit_found = True
                print(f"Position {position} Character: {digit}\n")
                if str(guessed_digits_str) == number_str:
                    print(f"Number Unlocked: {guessed_digits_str}")
                    guessed_number = int(guessed_digits_str)
                    print(f"Number Unlocked: {guessed_number} in {count} attempts.")
                    break
                else:
                    print(f"Guessed number so far: {guessed_digits_str}\n")
                    break
    # If no digits are guessed, return None
    if not guessed_digits_str:
        print("Number not guessed")
        return None

    # Otherwise, convert the guessed digits string to an integer and return it
    return guessed_number


# TODO: Create this algorithm and compare it to the efficiency of the other algorithms
def creative_binary_search(number: int):
    """
    Creative binary search algorithm
    Ideally uses the character by character search but uses binary search to guess the number
    :param number: int
    :return: int
    """
    pass


def compare_algorithms(algorithm1, algorithm2):
    """
    Compare the efficiency of the different algorithms
    """
    pass

def main():
    """
    Main function
    """
    # 8 digit number and 1 makes it a lot lower
    # Time complexity: O(n)

    number = 15413267

    # Brute Force Search
    # Time complexity: O(n)
    # start_time = time.time()
    # brute_force_search(number)
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"Brute Force Execution time: {execution_time} seconds\n")

    # Binary Search
    # Time complexity: O(log n)
    start_time = time.time()
    binary_search(number)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Binary Search Execution time: {execution_time} seconds\n")

    # Recursive Binary Search
    # Time complexity: O(log n)
    start_time = time.time()
    recursive_binary_search(number, 0, number)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Recursive Binary Search Execution time: {execution_time} seconds\n")

    # Character by Character Search
    # Time complexity: O(n)
    start_time = time.time()
    character_by_character_search(number)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Character by Character Execution time: {execution_time} seconds\n")


main()
