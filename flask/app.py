from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template('index.html', content='Hello World')
    else:
        return render_template('index.html', content='Hello World')

if __name__ == "__main__":
    app.run(debug=True)