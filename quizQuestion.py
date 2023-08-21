import datetime
import sys


class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        pass

    def print_header(self):
        print("\n\n*******************************************")
        # TODO: print the quiz header
        print(f"QUIZ: {self.name}")
        print(f"Description: {self.description}")
        print(f"Questions: {len(self.questions)}")
        print(f"Points: {self.total_points}")

        print("*******************************************\n")

    def print_results(self, quiztaker, thefile = sys.stdout):
        print("*******************************************", file=thefile, flush=True)
        print(f"Results for {quiztaker}", file=thefile, flush=True)
        print(f"Date: {datetime.datetime.today()}", file=thefile, flush=True)
        print(f"Questions: {self.correct_count} out of {len(self.questions)}", file=thefile, flush=True)
        print(f"Score: {self.score} out of {self.total_points}", file=thefile, flush=True)
        print("*******************************************\n", file=thefile, flush=True)

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0

        for q in self.questions:
            q.is_correct = False

        self.print_header()

        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points

        print("---------------------------")

        return self.score, self.correct_count, self.total_points


class Question:

    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")
            if len(response) == 0:
                print("Try again")
                continue

            response = response.lower()

            if response[0] != "t" and response[0] != "f":
                print("Try again")

            if response == self.correct_answer:
                self.is_correct = True

            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):

            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")

            response = input("? ")
            if len(response) == 0:
                print("Try again")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

