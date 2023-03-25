from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template('index.html', content='Hello World')
    else:
        return render_template('index.html', content='Hello World')
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        return render_template('add.html', content='Hello World')
    else:
        return render_template('add.html', content='Hello World')
    
@app.route('/notification', methods=['GET', 'POST'])
def notification():
    if request.method == "POST":
        return render_template('notification.html', content='Hello World')
    else:
        return render_template('notification.html', content='Hello World')

@app.route('/help_request', methods=['GET', 'POST'])
def help_request():
    if request.method == "POST":
        return render_template('help_request.html', content='Hello World')
    else:
        return render_template('help_request.html', content='Hello World')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == "POST":
        return render_template('emergency.html', content='Hello World')
    else:
        return render_template('emergency.html', content='Hello World')

if __name__ == "__main__":
    app.run(debug=True)