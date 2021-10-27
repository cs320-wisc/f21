from flask import Flask, Response
from matplotlib import pyplot as plt
# I/O => Input/Output
from io import StringIO, BytesIO
import pandas as pd
import random

plt.rcParams["font.size"] = 16

app = Flask("my lec 2 example")

purchases = [3,2,6]

@app.route("/insert", methods=["POST"])
def insert_page():
    return "TODO"

@app.route("/")
def home():
    purchases.append(random.gauss(10, 5))
    return """
    <html>
    <body>
    <h1>My Dashboard</h1>
    <h3>CDF (Cumulative Distribution Func) Example</h3>
    <img src="cdf.png">
    <h3>Hinto Example</h3>
    <img src="histo.png">
    <h3>PNG Example</h3>
    <img src="plot1.png">
    <h3>SVG Example</h3>
    <img src="plot2.svg">
    </body>
    </html>"""

@app.route("/cdf.png")
def plot_cdf():
    fig, area = plt.subplots(figsize=(3,2))
    
    # 1. switch the x-axis and y-axis
    # 2. rescale obs num 0-to-N scale to a 1-to-100 % scale
    s = pd.Series(sorted(purchases))
    s_rev = pd.Series(100*(s.index+1)/len(s), index=s.values)
    s_rev.plot.line(ax=area)
    area.set_xlabel("Purchase Amt")
    area.set_ylabel("% of Purchases")
    
    f = BytesIO()
    plt.tight_layout() # don't crop stuff
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "Example 2": "this will be ignored",
    })

@app.route("/histo.png")
def plot_histo():
    fig, area = plt.subplots(figsize=(3,2))
    pd.Series(purchases).hist(ax=area, bins=200)
    area.set_ylabel("Purchase Amt")
    
    f = BytesIO()
    plt.tight_layout() # don't crop stuff
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "Example 2": "this will be ignored",
    })

@app.route("/plot1.png")
def plot_png():
    fig, area = plt.subplots(figsize=(3,2))
    pd.Series(purchases).plot.line(ax=area)
    area.set_ylabel("Purchase Amt")
    
    f = BytesIO()
    plt.tight_layout() # don't crop stuff
    fig.savefig(f)
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/png",
        "Example 2": "this will be ignored",
    })

@app.route("/plot2.svg")
def plot_svg():
    fig, area = plt.subplots(figsize=(3,2))
    pd.Series(purchases).plot.line(ax=area)
    area.set_ylabel("Purchase Amt")
    
    f = BytesIO()
    plt.tight_layout() # don't crop stuff
    fig.savefig(f, format="svg")
    plt.close() # closes the most recent fig
    return Response(f.getvalue(), headers={
        "Content-Type": "image/svg+xml",
        "Example 2": "this will be ignored",
    })

app.run("0.0.0.0", debug=True, threaded=False)