import math

class ComplexNumberConverter:
    def parse_rectangular(self, s):
        s = s.replace(" ", "")
        for i in range(1, len(s)):
            if s[i] in "+-":
                real = float(s[:i])
                imag = float(s[i:-1])
                return real, imag
        raise ValueError("Invalid format")

    def rectangular_to_polar(self, s):
        a, b = self.parse_rectangular(s)
        magnitude = math.sqrt(a*a + b*b)
        angle = math.degrees(math.atan2(b, a))
        return magnitude, angle

    def polar_to_rectangular(self, magnitude, angle):
        rad = math.radians(angle)
        a = magnitude * math.cos(rad)
        b = magnitude * math.sin(rad)
        return a, b

def main():
    conv = ComplexNumberConverter()
    choice = input("Choose conversion:\n1. Rectangular to Polar\n2. Polar to Rectangular\nEnter choice (1/2): ")

    if choice == '1':
        s = input("Enter complex number (e.g., 3+4i): ")
        mag, ang = conv.rectangular_to_polar(s)
        print(f"Magnitude: {mag}")
        print(f"Angle (degrees): {ang}")

    elif choice == '2':
        mag = float(input("Enter magnitude: "))
        ang = float(input("Enter angle (degrees): "))
        a, b = conv.polar_to_rectangular(mag, ang)
        sign = "+" if b >= 0 else ""
        print(f"Rectangular form: {a}{sign}{b}i")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
