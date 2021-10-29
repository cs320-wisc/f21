from flask import Flask, Response, request
from matplotlib import pyplot as plt
# I/O => input/output
from io import StringIO, BytesIO
import pandas as pd
import random

app = Flask("lec 1 demo")
plt.rcParams["font.size"] = 18

purchases = [3,2,6]

@app.route("/insert", methods=["POST"])
def insert():
    nums = str(request.get_data(), "utf-8").split(",")
    for x in nums:
        purchases.append(float(x))
    return f"{len(nums)} inserted!\n"

@app.route("/")
def home():
    purchases.append(random.gauss(10, 3))
    return """
    <html>
    <body>
    <h1>My Dashboard</h1>
    <h2>CDF (Cumulative Dist Func)</h2>
    <img src="cdf.png" width=250>
    <h2>Histogram</h2>
    <img src="histo.png" width=250>
    <h2>PNG Example</h2>
    <img src="plot1.png" width=250>
    <h2>SVG Example</h2>
    <img src="plot2.svg" width=250>
    </body>
    </html>
    """

@app.route("/cdf.png")
def plot_cdf():
    fig, ax = plt.subplots()
    # 1. swap the x and y
    # 2. rescale the observation num (0-to-N) to (1 to 100)
    
    s = pd.Series(sorted(purchases))
    s_rev = pd.Series(100*(s.index+1)/len(s), index=s.values)
    s_rev.plot.line(ax=ax, ylim=(0,100))
    
    ax.set_xlabel("Purchase Amt")
    ax.set_ylabel("Perc of Purchases")
    plt.tight_layout() # don't crop anything
    f = BytesIO()
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "example2": "this does nothing"
    })

@app.route("/histo.png")
def plot_histo():
    fig, ax = plt.subplots()
    pd.Series(purchases).hist(bins=200)
    ax.set_ylabel("Purchases")
    plt.tight_layout() # don't crop anything
    f = BytesIO()
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "example2": "this does nothing"
    })

@app.route("/plot1.png")
def plot_png():
    fig, ax = plt.subplots()
    pd.Series(purchases).plot.line(ax=ax)
    ax.set_ylabel("Purchases")
    plt.tight_layout() # don't crop anything
    f = BytesIO()
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "example2": "this does nothing"
    })

@app.route("/plot2.svg")
def plot_svg():
    fig, ax = plt.subplots()
    ax.set_ylabel("Purchase")
    plt.tight_layout() # don't crop anything
    f = BytesIO()
    fig.savefig(f, format="svg")
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/svg+xml",
    })

app.run("0.0.0.0", debug=True, threaded=False)