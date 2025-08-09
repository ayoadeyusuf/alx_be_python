import sys

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return

    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    return result



def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    if result is not None:
        print(f"The result of the division is {result}")
    else:
        print("Division could not be performed due to errors.")
if __name__ == "__main__":
    main()
