import json

from flask import Flask, redirect

app = Flask(__name__)

processing = False

@app.route("/")
def main():
    print("Visitor")
    return "Hi! This is a test!"

@app.route('/option-1')
def option_1():
    global processing
    while processing:
        pass
    with open("votes.txt", "w") as f:
        processing = True
        cur_votes = f.read()
        if cur_votes:
            cur_votes = json.loads(cur_votes)
            cur_votes["option1"] += 1
        else:
            cur_votes = {"option1": 1, "option2": 0}
        f.write(json.dumps(cur_votes))
    processing = False
    print("option2!")
    return redirect("https://github.com/MadAvidCoder")

@app.route('/option-2')
def option_2():
    global processing
    while processing:
        pass
    with open("votes.txt", "w") as f:
        processing = True
        cur_votes = f.read()
        if cur_votes:
            cur_votes = json.loads(cur_votes)
            cur_votes["option2"] += 1
        else:
            cur_votes = {"option1": 0, "option2": 1}
        f.write(json.dumps(cur_votes))
    processing = False
    print("option1!")
    return redirect("https://github.com/MadAvidCoder")

@app.route('/results-1')
def results_1():
    global processing
    while processing:
        pass
    f = open("votes.txt", "r")
    processing = True
    cur_votes = f.read()
    cur_votes = json.loads(cur_votes)
    processing = False
    print("results 1")
    print(cur_votes)
    return cur_votes["option1"]

@app.route('/results-2')
def results_2():
    global processing
    while processing:
        pass
    f = open("votes.txt", "r")
    processing = True
    cur_votes = f.read()
    cur_votes = json.loads(cur_votes)
    f.close()
    processing = False
    print("reuslts 2")
    print(cur_votes)
    return cur_votes["option2"]

@app.route('/reset')
def reset():
    print("resetting")
    global processing
    while processing:
        pass
    with open("votes.txt", "w") as f:
        f.write("")
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=41863)