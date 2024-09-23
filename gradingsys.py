import openai


openai.api_key = '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'

def grade_assignment(student_response, expected_answer):
    prompt = (
        "Grade the following student response based on the expected answer. "
        "Provide a score from 0 to 100, include feedback, and give a corresponding letter grade (A, B, C, D, F).\n\n"
        "Student Response:\n"
        f"{student_response}\n\n"
        "Expected Answer:\n"
        f"{expected_answer}\n\n"
        "Grading Criteria: Clarity, completeness, correctness, and relevance."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )

        grading_feedback = response['choices'][0]['message']['content']
        return grading_feedback

    except Exception as e:
        return f"An error occurred: {e}"

def determine_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    student_response = input("Enter the student's response: ")
    expected_answer = input("Enter the expected answer: ")

    feedback = grade_assignment(student_response, expected_answer)
    
    
    try:
        
        score_str = feedback.split(",")[0]  
        score = int(score_str.split(":")[1].strip())
        letter_grade = determine_letter_grade(score)
        
        print("Grading Feedback:")
        print(feedback)
        print(f"Letter Grade: {letter_grade}")
        
    except (IndexError, ValueError):
        print("Could not extract the score from the feedback. Please check the response format.")
