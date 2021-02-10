class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_number = self.question_number +1
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(current_question.answer, answer)

    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            print(f"ok: score: {self.score}")
            self.score += 1
        else:
            print(f"fail: score: {self.score}")
