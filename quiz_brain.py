class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_number = self.question_number +1
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
