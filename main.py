from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

print(question_bank)
for question in question_bank:
    print(question.text, question.answer)
