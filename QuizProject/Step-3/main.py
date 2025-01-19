from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain

""" This code snippet systematically creates Question objects for each question in question_data and stores them in the
 question_bank list. Each iteration processes one question, 
extracting its text and answer, and then uses the Question class to encapsulate the data in a structured object.
"""
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()