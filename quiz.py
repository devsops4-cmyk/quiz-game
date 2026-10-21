












questions = [
    {
        "question": "What does CPU stand for?",
        "answers": [
            "A. Central Processing Unit",
            "B. Computer Processing Utility",
            "C. Central Program Unit"
        ],
        "correct answer": "A"
    },
    {
        "question": "Which language are we learning?",
        "answers": [
            "A. Java",
            "B. Python",
            "C. C++"
        ],
        "correct answer": "B"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "answers": [
            "A. function",
            "B. create",
            "C. def"
        ],
        "correct answer": "C"
    }
]

def calculate_percentage(score, total_questions):
    percentage = (score/total_questions) * 100
    return percentage


def get_result(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >=50:
        return "Pass"
    else:
        return "Fail"



# result = get_result(percentage)

def quiz_result(score, total_questions, percentage, result):
    print("==== QUIZ RESULT====")
    print("score:", score, "out of ", total_questions)
    print("Percentage: ", percentage, "%")
    print("result: ", result)



def play_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])

        for answer in question["answers"]:
            print(answer)
        while True:
            user_answer = input("Enter an answer: ").strip().upper()
            if user_answer in ["A", "B", "C"]:
                break
            print("invalid answer. Try again")

        if user_answer== question["correct answer"]:
            score+=1
            print("Correct!")
        else:
            print("Wrong!")
            
    return score



    # print(question["question"])
    # for answer in question["answers"]:
    #     print(answer)
    # for correct_answer in answer["corrcect anwer"]:
    #     print(correct_answer)







def get_total_questions(questions):
    while True:
        try:
            total = int(input("How many questions? "))

            if total > len(questions):
                print("Too many questions")

            if total >0 and total <= len(questions):
                return total
            print("invalid number of questions")

        except ValueError:
            print("Invalid input")


total_questions = get_total_questions(questions)
selected_questions = questions[:total_questions]
final_score = play_quiz(selected_questions)
percentage = calculate_percentage(final_score, total_questions)

result = get_result(percentage)




quiz_result(final_score, total_questions, percentage, result)
quiz_result(4, 5, 80.0, "Excellent")