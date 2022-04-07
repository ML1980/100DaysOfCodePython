class QuizzBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_number = self.question_number
        current_question = self.question_list[current_number]
        user_answer = input(f"Q{current_number+1}: {self.question_list[current_number].text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That´s wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
