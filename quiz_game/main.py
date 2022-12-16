from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    ques_txt = ques["text"]
    ques_ans = ques["answer"]
    q = Question(ques_txt, ques_ans)
    question_bank.append(q)

quiz = QuizBrain(question_bank)


while quiz.questions_left():
    quiz.next_question()


print("\n\n\nYou've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")