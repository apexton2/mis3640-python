def calculate_bmi(weight, height):
    bmi = 703 * weight / (height * weight)
    if bmi <= 18.5:
        print("your bmi is {:1f}. You are Underweighted.".format(bmi))

    elif 18.5 < bmi <= 25:
        print("you bmi is {:.1f}. you are normal weighted.".format(bmi))