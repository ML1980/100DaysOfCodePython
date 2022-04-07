from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for one_quest in question_data:
    question_bank.append(Question(one_quest["question"], one_quest["correct_answer"]))

#print(question_bank[0].answer)

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You comleted the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



