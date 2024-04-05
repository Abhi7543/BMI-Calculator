def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index)
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Taking input from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculating BMI
    bmi = calculate_bmi(weight, height)

    # Interpreting BMI
    interpretation = interpret_bmi(bmi)

    # Displaying the result
    print("Your BMI is:", round(bmi, 2))
    print("You are", interpretation)

if __name__ == "__main__":
    main()