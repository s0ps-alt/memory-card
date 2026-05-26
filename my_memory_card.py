from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGroupBox, QRadioButton
from random import shuffle

app = QApplication([])

lb_Question = QLabel("Question")
lb_Question.setAlignment(Qt.AlignCenter)

rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

box_Answers = QGroupBox("Answer options")
layout_answers = QVBoxLayout()
for rb in answers:
    layout_answers.addWidget(rb)
box_Answers.setLayout(layout_answers)

lb_Result = QLabel()
lb_Result.setAlignment(Qt.AlignCenter)

lb_Correct = QLabel()
lb_Correct.setAlignment(Qt.AlignCenter)

box_Result = QGroupBox("Test result")
layout_result = QVBoxLayout()
layout_result.addWidget(lb_Result)
layout_result.addWidget(lb_Correct)
box_Result.setLayout(layout_result)
box_Result.hide()

btn_OK = QPushButton("Answer")

layout = QVBoxLayout()
layout.addWidget(lb_Question)
layout.addWidget(box_Answers)
layout.addWidget(box_Result)
layout.addWidget(btn_OK, alignment=Qt.AlignCenter)

window = QWidget()
window.setLayout(layout)
window.setWindowTitle("Memory Card")
window.resize(400, 300)

questions = [
    ("The national language of Brazil", "Portuguese", "Spanish", "Italian", "Brazilian"),
    ("2 + 2 =", "4", "3", "5", "22"),
    ("Capital of France", "Paris", "Berlin", "Madrid", "Rome"),
    ("Largest ocean", "Pacific", "Atlantic", "Indian", "Arctic")
]

shuffle(questions)
current = 0
total = 0
correct = 0

def show_question():
    box_Result.hide()
    box_Answers.show()
    btn_OK.setText("Answer")
    for rb in answers:
        rb.setChecked(False)

def show_result():
    box_Answers.hide()
    box_Result.show()
    btn_OK.setText("Next question")

def ask(q):
    lb_Question.setText(q[0])
    shuffle(answers)
    answers[0].setText(q[1])
    answers[1].setText(q[2])
    answers[2].setText(q[3])
    answers[3].setText(q[4])
    lb_Correct.setText("Correct answer: " + q[1])
    show_question()

def check_answer():
    global total, correct
    total += 1
    if answers[0].isChecked():
        correct += 1
        lb_Result.setText("Correct!")
    else:
        lb_Result.setText("Incorrect!")

    print(f"Answered: {total}, Correct: {correct}, Rating: {correct/total*100:.1f}%")
    show_result()

def next_question():
    global current
    current += 1
    if current >= len(questions):
        shuffle(questions)
        current = 0
    ask(questions[current])

def click():
    if btn_OK.text() == "Answer":
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click)

ask(questions[current])
window.show()
app.exec()
