def get_average(list_marks):
    return sum(list_marks) / len(list_marks) if list_marks else 0


def get_weighted_average(weighted_marks):
    total_weighted_sum = sum(note * coef for note, coef in weighted_marks)
    total_coefficients = sum(coef for _, coef in weighted_marks)
    return total_weighted_sum / total_coefficients if total_coefficients else 0