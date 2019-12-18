from flask import Flask, render_template


class MainScore:
    def __init__(self, file_name):
        self.FILE_NAME = file_name


def score_server(name):
    try:
        # get user score
        file_name = open(name, 'r+')
        user_score = file_name.read()
        file_name.close()

        return user_score

    except IOError:
        return 'ERROR Failed to Return User Score'


app = Flask(__name__)


@app.route('/')
def show_score():
    score_from_file = score_server('Score.txt')
    return render_template("Score.html", score=score_from_file)
