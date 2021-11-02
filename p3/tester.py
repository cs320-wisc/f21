from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import subprocess, traceback, sys, json
from subprocess import Popen
import importlib as imp
import os
import time

options = Options()
options.headless = True

port = "5000"
page="Node_1.html"
address = f"http://localhost:{port}/{page}"
add=f"http://localhost:{port}/"
pass_bfs_file="MADCITY"
pass_dfs_file="COVID19"
password_bfs = "1234567"
password_dfs = "9874563"


def FileScraper_go(fscraper):
    l1=fscraper.go("1")
    l4=fscraper.go("4")
    test=("".join(l1)!= "24") or ("".join(l4)!= "367")
    if test:
        print("unexpected go method for file scraper")
    return not(test)
def WebScraper_go(scraper):
    l1=[f"http://localhost:{port}/Node_{index}.html" for index in ["2","4"]]
    l4=[f"http://localhost:{port}/Node_{index}.html" for index in ["3","6","7"]]
    l1_exp=scraper.go(f"http://localhost:{port}/Node_1.html")
    test1=(l1!= l1_exp)
    l4_exp=scraper.go(f"http://localhost:{port}/Node_4.html")
    test2=(l4!=l4_exp)
    test=test1 or test2
    if test:
        print("unexpected go method for web scraper")
    return not(test)
    
def dfs_pass_file_test(fscraper):
    fscraper.dfs_search("1")
    rv="".join(fscraper.DFSorder)
    expected = pass_dfs_file
    if rv != expected:
        print(f"unexpected dfs pass: {repr(rv)}")
    return rv == expected

def bfs_pass_file_test(fscraper):
    fscraper.bfs_search("1")
    
    rv="".join(fscraper.BFSorder)
    expected = pass_bfs_file
    if rv != expected:
        print(f"unexpected bfs pass: {repr(rv)}")
    return rv == expected


def dfs_pass_test(scraper):
    rv = scraper.dfs_pass(address)
    expected = password_dfs
    if rv != expected:
        print(f"unexpected dfs pass: {repr(rv)}")
    return rv == expected

def bfs_pass_test(scraper):
    rv = scraper.bfs_pass(address)
    expected = password_bfs
    if rv != expected:
        print(f"unexpected bfs pass: {repr(rv)}")
    return rv == expected

def protected_df_test_bfs(scraper):
    points = 0
    df = scraper.protected_df(add,password_bfs)
    
    print("\nFound Dataframe:")
    print(df)
   
    if df.iloc[0, -1] == "Picnic Point in Madison":
        points += 0.5
    else:
        print(f"did not expect {repr(df.iloc[0, -1])} in top-right cell for protected_df (BFS)")
    if len(df) == 8:
        points += 0.5
    else:
        print(f"did not expect {len(df)} rows for protected_df (BFS)")

    return points


def protected_df_test_dfs(scraper):
    points = 0

    # BFS
    
    df = scraper.protected_df(add,password_dfs)
        
    print("\nFound Dataframe:")
    print(df)
    
    
    if df.iloc[0, -1] == "Picnic Point in Madison":
        points += 0.5
    else:
        print(f"did not expect {repr(df.iloc[0, -1])} in top-right cell for protected_df (DFS)")
    if len(df) == 8:
        points += 0.5
    else:
        print(f"did not expect {len(df)} rows for protected_df (DFS)")

    return points

def main():
    # load student code
    student_file_name=sys.argv[1] if len(sys.argv) > 1 else "scrape"
    imp.import_module(student_file_name)
    results = {"score": 0}
    score = 0
    
    #tests the revised part
    # test the FileScraper class for BFS and DFS
    print("*** Testing GraphScraper and FileScraper ***\n")
    print("-"*50+"\n")
    test_revised=[dfs_pass_file_test, bfs_pass_file_test,FileScraper_go]
    FScraper = imp.import_module(student_file_name).FileScraper
    # use informative outputs to console
    labels1=["FileScraper.dfs_search(node)",\
            "FileScraper.bfs_search(node)",\
            "FileScraper.go(url)"]
    errors=[]
    for j,test_fn in enumerate(test_revised):
        score=0
        try:
            print("Testing: "+labels1[j]+"\n") 
            fscraper=FScraper()
            score = float(test_fn(fscraper))
        except Exception as e:
            print("TEST EXCEPTION:", str(e))
            traceback.print_exc()
            errors.append(f"{test_fn.__name__} : {e}")
            
       
        results["score"] += score
        results[test_fn.__name__] = score
        print(f"\nScore : {score} out of 1.0")
        print("\n"+"-"*50+"\n")
    
    # start server and test the web part 
    print("\n*** Testing WebScraper ***\n")
    print("-"*50+"\n")
    
    try:
        Scraper = imp.import_module(student_file_name).WebScraper
    except Exception: 
        # if WebScraper doesn't exist use fake TestWebScraper below and continually throw errors
        # for each function test
        Scraper= TesterWebScraper;
   
    f = open("logfile.txt", "a") 
    p = Popen(["python3", "application.py", port], stdout=f, stderr=f, stdin=f)

    # start fresh browser/scraper
    os.system("pkill -f -9 chromium")
    my_window = webdriver.Chrome(options=options, executable_path="chromium.chromedriver")
    scraper = Scraper(my_window)
    # tests for WebScraper 
    tests= [WebScraper_go,dfs_pass_test, bfs_pass_test,protected_df_test_dfs, protected_df_test_bfs]
    # labels to show students so they are a bit more informative 
    labels=["WebScraper.go(url)",\
            "WebScraper.dfs_pass(start_url)",\
            "WebScraper.bfs_pass(start_url)",\
            "WebScraper.protected_df(url,dfs_password)",\
            "WebScraper.protected_df(url,bfs_password)"]
    
    # for each test get the score from each test, 
    #if it throws an error print out that error to console
    
    for j,test_fn in enumerate(tests):
        score=0
        try:
            # test each function 
            print("Testing: "+labels[j]+"\n") 
            score=float(test_fn(scraper))
        except Exception as e:
            print("TEST EXCEPTION:", str(e))
            traceback.print_exc()
            errors.append(f"{test_fn.__name__} : {e}")
            
        # increment the total score
        # print out score for that functon test
        results["score"] += score
        results[test_fn.__name__] = score
        print(f"\nScore : {score} out of 1.0")
        print("\n"+"-"*50+"\n")
    
    
    # close the chromium window
    my_window.close()
    results["score"] *= 100 / (len(tests)+len(test_revised))
    results["errors"]=errors
    print(f"\n\nFinal score:%0.2f"%results["score"])
    with open("results.json", "w") as f:
        json.dump(results, f, indent=True)
    print("\n*** Final Results ***\n")
    print(results)
    
    # shut down application.py 
    p.terminate()
    
    time.sleep(5) # wait for shutdown
    
    
 # trick to make WebScraper fail if it is not specified. Future TA could probably do this more cleanly by rewriting the code above, but it works! 
class TesterWebScraper:
    # required
    def	__init__(self,driver):
        print("** No WebScraper class FOUND ** \n\n")
    # these three can be done as groupwork
    def go(self, url):
        raise Exception("No go function specified")
    def dfs_pass(self, start_url):
        raise Exception("No dfs_pass function specified")

    def bfs_pass(self, start_url):
        raise Exception("no bfs_pass function specified")

    # write the code for this one individually
    def protected_df(self, url, password):
        raise Exception("no protected_df function specified")

if __name__ == "__main__":
    main()
