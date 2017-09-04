def bmi(weight, height):
    bmi_index = weight / height ** 2
    if bmi_index <= 18.5:
        return "Underweight"
    elif bmi_index <= 25.0:
        return "Normal"
    elif bmi_index <= 30.0:
        return "Overweight"
    return "Obese"
