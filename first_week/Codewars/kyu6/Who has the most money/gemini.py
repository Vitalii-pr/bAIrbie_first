def most_money(students):
    """
    Calculates the total money each student has and returns the name of the student
    with the most money, or "all" if there's a tie for the most.
    """
    max_money = 0
    richest_student = None
    for student in students:
        total_money = (student.fives * 5) + (student.tens * 10) + (student.twenties * 20)
        if total_money > max_money:
            max_money = total_money
            richest_student = student.name
        elif total_money == max_money:  # Handle the case of a tie
            richest_student = "all"
    return richest_student
