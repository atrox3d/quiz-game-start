from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# print(question_bank)
# for question in question_bank:
#     print(question.text, question.answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")