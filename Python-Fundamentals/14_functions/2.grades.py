def grade_text(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.5:
        return "Good"
    elif grade < 5.5:
        return "Very Good"
    else:
        return "Excellent"


current_grade = float(input())
print(grade_text(current_grade))