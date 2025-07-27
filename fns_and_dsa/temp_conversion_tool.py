import sys

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        temp_input = input("Enter the temperature to convert: ")
        try:
            temp = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    while True:
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if scale in ['C', 'F']:
            break
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if scale == 'C':
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    else:
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")

if __name__ == "__main__":
    main()
