from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form["name"]
    print name
    location = request.form["location"]
    print location
    language = request.form["language"]
    print language
    comment = request.form["comment"]
    print comment
    return render_template('process.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True)