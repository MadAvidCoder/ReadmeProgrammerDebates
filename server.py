import json

from flask import Flask, redirect, make_response
from threading import Lock
from random import randint
lock = Lock()
app = Flask(__name__)

@app.route("/")
def main():
    print("Visitor")
    return "Hi! This is a test!"

@app.route('/option-1')
def option_1():
    with lock:
        with open("votes.txt", "r+") as f:
            cur_votes = f.read()
            if cur_votes:
                if not cur_votes.strip():
                    cur_votes = '{"option1": 0, "option2": 0}'
                cur_votes = json.loads(cur_votes)
                cur_votes["option1"] += 1
            else:
                cur_votes = {"option1": 1, "option2": 0}
            f.seek(0)
            f.write(json.dumps(cur_votes))
            f.truncate()
        print("option2!")
    return redirect("https://github.com/MadAvidCoder?voted={}/#programmer-debate".format(randint(1, 999)))

@app.route('/option-2')
def option_2():
    with lock:
        with open("votes.txt", "r+") as f:
            cur_votes = f.read()
            if cur_votes:
                if not cur_votes.strip():
                    cur_votes = '{"option1": 0, "option2": 0}'
                cur_votes = json.loads(cur_votes)
                cur_votes["option2"] += 1
            else:
                cur_votes = {"option1": 0, "option2": 1}
            f.seek(0)
            f.write(json.dumps(cur_votes))
            f.truncate()
        print("option1!")
    return redirect("https://github.com/MadAvidCoder?voted={}/#programmer-debate".format(randint(1, 999)))

@app.route('/results-1')
def results_1():
    with lock:
        with open("votes.txt", "r") as f:
            cur_votes = f.read()
            if not cur_votes.strip():
                cur_votes = '{"option1": 0, "option2": 0}'
            cur_votes = json.loads(cur_votes)
    print("results 1")
    print(cur_votes)
    resp = make_response(json.dumps({"value": cur_votes["option1"]}))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route('/results-2')
def results_2():
    with lock:
        with open("votes.txt", "r") as f:
            cur_votes = f.read()
            if not cur_votes.strip():
                cur_votes = '{"option1": 0, "option2": 0}'
            cur_votes = json.loads(cur_votes)
    print("reuslts 2")
    print(cur_votes)
    resp = make_response(json.dumps({"value": cur_votes["option2"]}))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route('/reset')
def reset():
    print("resetting")
    with lock:
        with open("votes.txt", "w") as f:
            f.write('{"option1": 0, "option2": 0}')
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=41863)