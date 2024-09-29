
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program for user interaction
def main():
    try:
        # Ask user to enter the temperature and type
        temp = input("Enter the temperature to convert: ")
        temp = float(temp) 
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equivalent to {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equivalent to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle non-numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Entry point of the script
if __name__ == "__main__":
    main()

