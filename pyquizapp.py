import quizManager


class QuizApp:
    QUIZ_FOLDER = "quizes"

    def __init__(self) -> None:
        self.username = ""
        self.qm = quizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        self.greeting()

        self.username = input("Please enter your username: ")
        print(f"Welcome, {self.username}")

    def greeting(self):
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("````````Welcome to PYQUIZ```````")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        selection = ""

        while True:
            selection = input("Selection? ")
            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()

            if selection[0] == "E":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.menu_header()
            elif selection[0] == "L":
                print("\nAvailable quizzes are: ")
                self.qm.list_quizzes()
                print("-----------------------\n")
                continue
            elif selection[0] == "T":
                try:
                    quiznum = int(input("Enter quiz number please--> "))
                    print(f"You have selected quiz number {quiznum}")
                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                except:
                    self.menu_error()

            else:
                self.menu_error()
                continue

    def run(self):
        self.startup()
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
