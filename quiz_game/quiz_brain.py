class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0


    def questions_left(self):
        return self.question_number < len(self.question_list)
    
    
    def next_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        usr_ans = input(f"Q.{self.question_number}: {current_ques.text} (True/False):")
        right_ans = current_ques.answer
        self.check_answer(usr_ans, right_ans)


    def check_answer(self, usr_answer, right_answer):
        if usr_answer.lower() == right_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Right answer was: {right_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")