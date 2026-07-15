'''
4.Create a Quiz Application using Python Dictionaries.
Store at least 5 questions in a dictionary. Each question should contain:
The question
Four options (A, B, C, D)
The correct answer
Requirements
Display one question at a time.
Display all four options.
Ask the user to enter:
A, B, C, or D to answer.
S to skip the current question.
Q to quit the quiz.
If the answer is correct:
Add 1 point.
If the answer is incorrect:
Deduct 1 point.
If the user chooses Skip (S):
Move to the next question without changing the score.
If the user chooses Quit (Q):
End the quiz immediately.
After the quiz ends, display:
Final Score
Number of Correct Answers
Number of Incorrect Answers
Number of Skipped Questions
 
'''

quiz={
    1:{
        "question": "What is the output of print(2 + 3 * 2)?",
        "options": {
            "A": "10",
            "B": "8",
            "C": "12",
            "D": "6"
        },
        "answer": "B"
    },
    2:{
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "define",
            "C": "def",
            "D": "fun"
        },
        "answer": "C"
    },
     3: {
        "question": "Which data type is immutable?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Set",
            "D": "Tuple"
        },
        "answer": "D"
    },

    4: {
        "question": "Which method is used to add one element to a set?",
        "options": {
            "A": "append()",
            "B": "insert()",
            "C": "add()",
            "D": "update()"
        },
        "answer": "C"
    },

    5: {
        "question": "Which symbol is used to access a value from a dictionary using its key?",
        "options": {
            "A": "()",
            "B": "{}",
            "C": "[]",
            "D": "<>"
        },
        "answer": "C"
    }

}
correct=0
score=0
incorrect=0
skip=0
wrong_questions = []
for i in range(1,len(quiz)+1):
    print(quiz[i]['question'])
    for option, value in quiz[i]['options'].items():
        print(option + '.', value)
    choice=input('enter your choice: ').upper()
    if choice == "Q":
        break
    elif choice == "S":
        skip+= 1
        continue
    elif choice in ["A", "B", "C", "D"]:
        if choice == quiz[i]["answer"]:
            score += 1
            correct += 1
        else:
            score -= 1
            incorrect += 1
            wrong_questions.append(i)
    else:
        print('Invalid input ')
print('')
print('Quiz Finished')
print('Final Score: ',score)
print('Correct answers: ',correct)
print('Incoorect Answers: ',incorrect,'Wrong questions: ',wrong_questions)
print('skipped: ',skip)
    



