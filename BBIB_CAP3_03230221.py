################################
# Github Repo link
# Pema Pelzang Thinley
# BI"B"
# Your Student ID Number: 03230221
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# https://www.youtube.com/watch?v=-gjxg6Pln50
################################
# SOLUTION
# Your Solution Score: 480829
################################

def calculate_sum(input_file):
    """
    Calculates the sum of two-digit numbers formed by the first and last digits of each line in the input file.

    Args:
        input_file (str): The path to the input text file.

    Returns:
        int or None: The total sum of the two-digit numbers, or None if an error occurs.
    """
    total_sum = 0

    try:
        with open(input_file, 'r') as file:
            for line in file:
                # Removing leading and trailing whitespaces
                line = line.strip()

                # Finding the first and last digits using two pointers
                start_ptr, end_ptr = 0, len(line) - 1

                # Moving the start pointer forward until it points to a digit
                while start_ptr < len(line) and not line[start_ptr].isdigit():
                    start_ptr += 1

                # Moving the end pointer backward until it points to a digit
                while end_ptr >= 0 and not line[end_ptr].isdigit():
                    end_ptr -= 1

                # Checking if both pointers are valid and point to digits
                if start_ptr < end_ptr:
                    # Extract the first and last digits
                    first_digit = int(line[start_ptr])
                    last_digit = int(line[end_ptr])

                    # Forming the two-digit number
                    two_digit_number = first_digit * 10 + last_digit

                    # Adding the two-digit number to the total sum
                    total_sum += two_digit_number

    except FileNotFoundError:
        print("Error: File not found")
        return None
    except Exception as e:
        print("Error:", str(e))
        return None

    return total_sum

input_file = r"Assignment 3/221.txt"

result = calculate_sum(input_file)
if result is not None:
    print("The total sum of from the given input file",input_file,"is",result)