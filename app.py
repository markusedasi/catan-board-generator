from flask import Flask, render_template
from generator_logic import *

app = Flask(__name__)

@app.route('/')
def home():
    tile_set = generate_board()
    structured_board = structure_board(tile_set)
    return render_template("index.html", board=structured_board)

if __name__ == '__main__':
    app.run(debug=True)
