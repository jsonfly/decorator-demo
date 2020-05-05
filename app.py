from flask import Flask, render_template

import util

app = Flask(__name__)


@app.route('/')
@util.block_odd_minutes
def hello_world():
    return 'Hello World!'


@app.route('/calculate-squares/<to>')
@util.measure_time
def calculate_squares(to):
    squares = util.get_squares(to)

    generated_html = render_template('squares.html', squares=squares)

    return generated_html


if __name__ == '__main__':
    app.run()
