import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        
    
    
    numerator = float(input('Numerator: '))
    denominator = float(input('Denominator: '))
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
