def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be a positive number.")
            return value
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")


length = get_input("Enter the length of the rectangle: ")
width = get_input("Enter the width of the rectangle: ")

area = length * width
print(f"Rectangle area: {area}")
