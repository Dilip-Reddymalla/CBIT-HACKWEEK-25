import argparse
def main():
    parser = argparse.ArgumentParser(description="Convert between Celsius and Fahrenheit.")
    parser.add_argument('--to', choices=['cel', 'fah'], required=True, help="unit to convert to.")
    parser.add_argument('--og', type=float, required=True, help="Temperature value to convert.")
    args = parser.parse_args()

    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    if args.to == 'cel':
        result = fahrenheit_to_celsius(args.og)
        print(f"{args.og} F is {result} C")
    elif args.to == 'fah':
        result = celsius_to_fahrenheit(args.og)
        print(f"{args.og} C is {result} F")

if __name__ == "__main__":
    main()
