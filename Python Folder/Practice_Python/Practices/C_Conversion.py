class Conversion:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        return (9 / 5 * self.celsius) + 32

    def celsius_to_kelvin(self):
        return self.celsius + 273


a = float(input("Enter Celsius value: "))
b = input("Enter 'f' for Fahrenheit value or 'k' for Kelvin value: ")
conv = Conversion(a)
if b.lower() == "f":
    print(f"{conv.celsius_to_fahrenheit():.2f} Fahrenheit")
elif b.lower() == "k":
    print(f"{conv.celsius_to_kelvin():.2f} Kelvin")
else:
    print("Invalid input  'f' or 'k'.")
