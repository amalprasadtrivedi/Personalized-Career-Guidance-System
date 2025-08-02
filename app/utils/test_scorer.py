from typing import List


# --------------------- Score a user's answers against correct answers --------------------- #
def score_test(user_answers: List[str], correct_answers: List[str]) -> int:
    """
    Compares user answers with the correct ones and returns the total score.
    Assumes each correct answer gives 1 mark.
    """
    score = 0
    for user_ans, correct_ans in zip(user_answers, correct_answers):
        if user_ans.strip().upper() == correct_ans.strip().upper():
            score += 1
    return score


# --------------------- Provide a basic interpretation of score --------------------- #
def evaluate_score(score: int, total_questions: int) -> str:
    """
    Interprets the score and returns a basic evaluation message.
    """
    percentage = (score / total_questions) * 100

    if percentage >= 85:
        return "Excellent! You have a strong aptitude and alignment with technical roles."
    elif percentage >= 65:
        return "Good performance! You may excel in moderately technical or analytical careers."
    elif percentage >= 45:
        return "Average score. Consider improving problem-solving and analytical skills."
    else:
        return "Low score. You may explore creative or support-oriented careers while working on aptitude skills."


# --------------------- Main test evaluation function --------------------- #
def evaluate_test(user_answers: List[str], correct_answers: List[str]) -> dict:
    """
    Complete test evaluation pipeline.
    Returns both score and evaluation summary.
    """
    total_score = score_test(user_answers, correct_answers)
    total_questions = len(correct_answers)
    evaluation = evaluate_score(total_score, total_questions)

    return {
        "total_score": total_score,
        "total_questions": total_questions,
        "evaluation": evaluation
    }
