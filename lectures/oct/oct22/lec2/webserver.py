import pandas as pd
from flask import Flask, request, Response, jsonify
import time

app = Flask(__name__)
# df = pd.read_csv("main.csv")

major_counts = {}

@app.route('/major.html')
def record_major():
    # step 1: get query string value into a variable
    print(dict(request.args))
    if not "major" in request.args:
        return "need a major"
    major_name = request.args["major"]
    print(major_name)
    
    # step 2: update the stats in the dict
    if not major_name in major_counts:
        major_counts[major_name] = 0
    major_counts[major_name] += 1
    
    # step 3: share the stats with people
    return str(major_counts)

# TEMPLATING (DYNAMIC) PAGE
@app.route('/time.html')
def see_time():
    with open("time.html") as f:
        html = f.read()
       
    print("BEFORE", html)
    html = html.replace("REPLACE_ME", str(time.time()))
    print("AFTER", html)

    return html

# DYNAMIC PAGE
@app.route('/ha.html')
def laughing():
    return "<b>hahaha</b>"

# STATIC PAGE
@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()

    # return html
    return Response(html, headers={"A": "apple", "B": "banana"}, status=200)

# TODO: need a dict of last_times, one per user
last_time = time.time()

@app.route('/donotvisit')
def goaway():
    global last_time
    if time.time() - last_time < 3:
        return Response("go away", headers={"Retry-After": "3"}, status=429)
    else:
        last_time = time.time()
        return Response("welcome", status=200)
    
@app.route('/robots.txt')
def robo():
    return Response("\n".join(["User-Agent: *", "Disallow: /donotvisit"]),
                   headers={"Content-Type": "text/plain"})

# did something try to run this .py as a program
if __name__ == '__main__':
    print("START")
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!
    print("DONE")

# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.