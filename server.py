from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'quiet'

@app.route('/')
def index():
    if 'click' not in session:
        session['click'] = 0
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count_():
    session['click'] += 1
    return redirect('/')

@app.route("/reset", methods=['POST'])
def reset():
    session['click'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)