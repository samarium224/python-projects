# class Human:
#     def __init__(self, username , id):
#         self.username = username
#         self.id = id
#         self.point = 0

#     def wakeup(self, time):
#         self.wakeup_time = time
#         self.point += 1

#     pass


# user_1 = Human('samir',1)
# user_1.wakeup(40)
# print(user_1.point)


question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        pass

question_bank = []
score = 0

for items in question_data:
    question_bank.append(Question(items["text"],items["answer"].lower()))


print("Welcome to quiz game")



for number in range(0,len(question_bank)):

    print(question_bank[number].text)
    a = input("True or false ? : ")
    if a == question_bank[number].answer:
        score += 1
        print(f"Right answer | Your score: {score}/{number+1}")

    else:
        print(f"Wrong answer | Your score: {score}/{number+1}")

    print("\n \n")

