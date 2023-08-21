import os.path
import os
import quizParser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        self.the_quiz = None
        self.quizzes = dict()
        self.results = None
        self.quiztaker = ""

        if os.path.exists(quizfolder) is False:
            raise FileNotFoundError("Quiz folder does not exists")

        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        for i, j in enumerate(dircontents):
            if j.is_file():
                parser = quizParser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(j)
    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"{k}: {v.name}")

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        pass

    # prints the results of the most recently taken quiz
    def print_results(self):
        pass

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("quizes")
    qm.list_quizzes()