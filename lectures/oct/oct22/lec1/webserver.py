import pandas as pd
from flask import Flask, request, Response, jsonify
import time

app = Flask(__name__)

major_counts = {}

@app.route('/major.html')
def major():
    # step 1: extract the query strings from the args dict
    print(dict(request.args))
    if not "major" in request.args:
        return "please specify a major"
    major_name = request.args["major"]
    
    # step 2: use it to compute stats
    print(major_name)
    if major_name not in major_counts:
        major_counts[major_name] = 0
    major_counts[major_name] += 1
    
    # step 3: share the stats with whoever visited the page
    return str(major_counts)

# DYNAMIC TEMPLATED PAGE
@app.route('/time.html')
def time_page():
    with open("time.html") as f:
        html = f.read()
    print("HTML (before)", html)
    html = html.replace("REPLACE_ME", str(time.time()))
    print("HTML (after)", html)

    return html

# DYNAMIC PAGE
@app.route('/ha.html')
def laughing():
    return "<b>hahahaha</b>"

# STATIC PAGE
@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()

    #return html
    return Response(html)

# TODO: have a dict of last visit times (one per user)
last_visit = time.time()

@app.route('/donotvisit')
def hidden():
    global last_visit
    if time.time() - last_visit > 3:
        last_visit = time.time()
        return Response("thanks for visiting")
    else:
        return Response("go away", status=429, headers={"Retry-After": "3"})

@app.route('/robots.txt')
def robots():
    return Response("\n".join(["User-Agent: *", "Disallow: /donotvisit"]),
                   headers={"Content-Type": "text/plain"})


if __name__ == '__main__':
    # 0.0.0.0 is a fake IP address, use whatever my virt machines public IP is
    # 127.0.0.1 is a fake IP address, means listen to local (same computer) requsets only
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!
    print("AFTER")

# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.