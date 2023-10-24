from flask import Flask , render_template# pip install flask kwa your new venv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)