def to_python_complex(s):
    return complex(s.replace('i', 'j'))

def format_i(z):
    return f"{z.real}+{z.imag}i" if z.imag >= 0 else f"{z.real}{z.imag}i"

def main():
    try:
        # Read complex numbers using ONLY i
        c1 = to_python_complex(input("Enter first complex number (e.g., 2+3i): "))
        c2 = to_python_complex(input("Enter second complex number (e.g., 4-2i): "))

        print("\nChoose operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "1":
            print("\nSum:", format_i(c1 + c2))
        elif choice == "2":
            print("\nDifference:", format_i(c1 - c2))
        elif choice == "3":
            print("\nProduct:", format_i(c1 * c2))
        elif choice == "4":
            print("\nQuotient:", format_i(c1 / c2))
        elif choice == "5":
            print(f"\nModulus of first: {abs(c1)}")
            print(f"Modulus of second: {abs(c2)}")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid complex number. Use format like 2+3i.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()
