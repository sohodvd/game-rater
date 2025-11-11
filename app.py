from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return "This is my first coding project to rate the games I have played."

@app.route('/games')
def game():
    return "Here are your rated games."

if __name__ == '__main__':
    app.run(debug=True)