"""
Refactored script: Cleaned up messy code using AI assistance.
Originally lacked functions, used single-letter variables, and had no input validation.
"""

def calculate_grade(score):
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    return "F"

def display_student_report(name, scores):
    avg_score = sum(scores) / len(scores)
    grade = calculate_grade(avg_score)
    print(f"Student: {name} | Average: {avg_score:.2f} | Final Grade: {grade}")

if __name__ == "__main__":
    display_student_report("Alex", [88, 92, 79, 95])
