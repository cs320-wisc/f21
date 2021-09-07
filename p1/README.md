# DRAFT -- don't start yet

# Project 1: Review and Git Analysis

## Corrections/Clarifications

## Overview

## Setup



# Group Part (75%)

For this portion of the project, you may collaborate with your group
members in any way (even looking at working code).  You may also seek
help from 320 staff (mentors, TAs, instructor).  You <b>may not</b>
seek receive help from other 320 students (outside your group) or
anybody outside the course.

## Review 220: Control Flow (Part 1)

### Q1: what is the type of `7/2`?

Take a look at the builtin Python functions to see if one can answer this: https://docs.python.org/3/library/functions.html

Some functions we use a lot in 220/320 are abs, dir, float, input, int, len, list, max, min, range, set, sorted, str, sum, type.

7 and 2 are ints, so the result of dividing these is an int (3, after rounding down 3.5) in most programming languages.  Python produces the mathematically correct answer, even though it is not an int (like 7 and 2).

In other cases where you want to divide 7 by 2 and get an int, you would use `7 // 2`.

### Q2: what is `error`?

Complete the code in accordance with the comment to calculate the answer.

```python
x = 4
maximum = 10
minimum = 5
error = ???? # True if x is outside the minimum-to-maximum range
error
```

Notes:
1. we don't need to specify the type of our variables as in some languages (e.g., Java) -- Python knows x is an `int` because we assigned `4`, which is an int.  Variable types are not fixed after creation as in some languages (e.g., Go) -- we could later run `x = "howdy"` if we wanted to
2. in Python, a `bool` is `True` or `False`.  We use the `and`, `or`, and `not` operators (in other programming languages, these operators are often expressed as `&&`, `||`, and `!`).

### Q3: ignoring case, does `word` end with the suffix "esque"?

Complete the following to answer:

```python
word = "KAFKAESQUE"
suffix_match = ???? # .endswith(...) method not allowed for this question! (practice slicing)
suffix_match
```

Skim string methods here: https://docs.python.org/3/library/stdtypes.html#string-methods.  Some important ones: `find`, `isdigit`, `join`, `split`, `lower`, `upper`, `strip`, `replace`.

Hints:
1. to ignore case, it's often easy to use a method to make everything upper or lower case
2. to get a single character from a string, you can use `s[INDEX]`.  0 is the first character, 1 is the second, and so on.  Python supports negative indexing, meaning `s[-1]` is the last letter, `s[-2]` is the next to last, etc.  You can also *slice* strings to get a substring by putting a colon between two indexes `s[inclusive_start:exclusive_end]`.  You can leave off one of the indexes to go to the start or end of the string.  For example, `word[:3]` would evaluate to `"KAF"`.
3. in Java, you compare strings with `s1.equals(s2)`, but in Python the correct equivalent is `s1 == s2`.  The equivalent of Java's `==` is Python's rarely used `is` operator.

### Requirement: `add` function

Your function should generally take two ints and return their sum.  For example, `add(2, 3)` should return 5.  Users of the function should also be able to call it like `add(x=2, y=3)`.  If only one argument is passed, 1 should be added.  For example, `add(3)` or `add(x=3)` would both return 4.

Python parameters may be filled with positions arguments, keyword arguments, or default arguments.  If this is unfamiliar, read the following:

1. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
2. https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions

In Python, indents are very important.  The code inside a function/if/loop is indented (Python doesn't use `{` and `{` to indicate this, as in Java and many other languages).

### Q4: what is `add(3, 4)`?

Call your function to answer.

### Q5: what is `add(9)`?

### Q6: what is `status`?

Complete the following so that `status` says something meaningful about `x`.

```python
x = 4
if ????:
    status = "negative"
elif ????:
    status = "positive"
else:
    status = "zero"
status
```

https://docs.python.org/3/tutorial/controlflow.html#if-statements

### Requirement: `nums` list and `smart_count` function

Paste the following:

```python
nums = [3, 4, 1, 6]
for x in nums:
    print(x)
```

Python lists can be created like `[item1, item2, ...]` and indexed/sliced just like strings (strings and lists are both examples of Python *sequences*; by definition, you can index and slice any kind of sequence you encounter in Python).  This list contains just ints, but you're free to have a mix of types in Python lists.

In general, you can plug in a variable name and sequence into a `for` loop to run a piece of code for every entry in the sequence:

```python
for ???? in ????:
    # DO SOMETHING
```

More on `for` loops:
* https://docs.python.org/3/tutorial/controlflow.html#for-statements
* https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

Write a function called `smart_count` that takes a list of numbers and returns their sum.  It should also have the following features:
1. ignore numbers greater than 10
2. if there is a negative number, that number (and all that follow it, positive or negative, should be skipped)

Use `continue` to implement feature 1 and `break` to implement feature 2.

### Q7: what is `smart_count(nums)`?

### Q8: what is `smart_count([2, 1, 11, 3, 15, -1, 8, 2])`?

The answer should be 6: 2+1+3.  11 and 15 are too large, so they are skipped.  8 and 2 are skipped because they are after a negative number (which is also skipped).

## Review 220: State (Part 2)

### Requirement: lists and dicts

Copy/paste the following:

```python
header = ["A", "B", "C"]

coord1 = {"x": 8, "y": 5}
coord2 = {"x": 9, "y": 2}
coord3 = {"x": 3, "y": 1}

rows = [
    [1, 6, coord1],
    [3, 4, coord2],
    [5, 2, coord3],
]
```

Note that `rows` is a list of lists.  Each inner list contains two ints and one dict (dictionary).  For complicated nested structures like this, it's often helpful to visualize the stack of frames and heap of objects in PythonTutor: https://pythontutor.com/live.html#mode=edit.

You could copy the above to visualize it, or use the following link for your convenience:

https://pythontutor.com/visualize.html#code=header%20%3D%20%5B%22A%22,%20%22B%22,%20%22C%22%5D%0A%0Acoord1%20%3D%20%7B%22x%22%3A%208,%20%22y%22%3A%205%7D%0Acoord2%20%3D%20%7B%22x%22%3A%209,%20%22y%22%3A%202%7D%0Acoord3%20%3D%20%7B%22x%22%3A%203,%20%22y%22%3A%201%7D%0A%0Arows%20%3D%20%5B%0A%20%20%20%20%5B1,%206,%20coord1%5D,%0A%20%20%20%20%5B3,%204,%20coord2%5D,%0A%20%20%20%20%5B5,%202,%20coord3%5D,%0A%5D&cumulative=false&curInstr=7&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Both lists and dicts contain values.  With lists, each value is associated with an index (integers starting from 0).  With dicts, each value is associated with a key specified by the programmers.  Keys are often strings, but they don't need to be.

Docs:
* https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
* https://docs.python.org/3/tutorial/datastructures.html#dictionaries

### Q9: after inserting a "z" key in `coord3` (with `coord3["z"] = 3.14`), what is `rows`?

### Q10: what is the value associated with the "x" key of the dict in the last position of the first list?

**Hint:** if the question were "what is the value associated with the 'y' key of the dict in the last position of the second list?", the solution would be: `rows[1][-1]["y"]`.  You just need to tack on brackets containing indexes (for lists) or keys (for dicts) to delve deeper into a nested structure.

### Q11: what is `rows` after running the following?

Complete the following so that the first change via `v2` is NOT reflected in `rows`, but the second change via `v2` IS reflected in `rows`:

```python
import copy
v2 = ????
v2[0] = 8888    # first change
v2[1][1] = 9999 # second change
```

Relevant docs: https://docs.python.org/3/library/copy.html

To get a good intuition about the reference/shallow/deep copy, try stepping through the following slowly in PythonTutor:

```python
import copy
v1 = [[1], [], [2, 3]]
v2 = v1
v2 = copy.copy(v1)
v2 = copy.deepcopy(v1)
```

### Q12: if we imagine the list of lists structure referenced by `rows` as a table, with column names in `header`, what is the sum of values in the "B" column?

Note: the "B" column corresponds to the values at index in 1 of each list, but you are not allowed to hardcode 1 for this solution.  Instead, use `header.index(????)` to look up the position of "B" within the `header` list.

### Q13: what is `rows` after we sort it in-place by the "B" column, ascending?

Docs:
* https://docs.python.org/3/howto/sorting.html#sorting-basics
* https://docs.python.org/3/howto/sorting.html#key-functions

Hint: if we had to sort by the "A" column ascending, we could do the following:

```python
def get_column_a(row):
    print("lookup A column for a row")
    return row[header.index("A")]

rows.sort(key=get_column_a, reverse=True)
rows
```

Note that we aren't calling `get_column_a` ourselves (because there are now parentheses after it on the sort line).  Instead, we're giving the `sort` method a reference to that function; this allows `sort` to call the function on each row, to figure out what part of the row objects matters for the sort.

When we only need a function for one purpose, we can use the `lambda` syntax instead of the `def` syntax to define the function on a single line, without even giving it a name.  The following works the same as the earlier example (but without the print):

```python
rows.sort(key=lambda row: row[header.index("A")], reverse=True)
rows
```

### Q14: say you're going on vacation to Europe with 400 US dollars; how many Euros can you get at the current exchange rate?

This site provides exchange rate information in JSON format: https://www.floatrates.com/json-feeds.html.  JSON is a simple format that can represent nested dicts and lists in files and web resources.

Download a copy of `usd.json` to the directory where your project is.  An easy way is to open a terminal, `cd` to the appriate directory, then run `wget SOME_URL_HERE` to download the web resource.

Note: you can run shell commands in Jupyter, too, if you start the command with a `!` (to indicate it is not Python code).  If you do this, be sure to delete the cell after the download.  Otherwise you'll create too much traffic on the floatrates.com site, re-downloading the same thing every time you re-run your notebook.

You can read a file like this:

```python
f = open("usd.json")
data = f.read()
f.close()
```

Check the type of `data` and the first portion of it:

```python
print(type(data))
print(data[:300] + "...")
```

Even though the file contains a string that *could* be interpreted as JSON, Python won't *deserialize* it to Python dicts/lists automatically.  Instead of calling `.read()`, we need to use the `load` function in the `json` module:

https://docs.python.org/3/library/json.html#json.load

When reading documentation, start by focusing on parameters that can't take default arguments.

## Review 220: Data Science (Part 3)

# Individual Part (25%)

You have to do the remainder of this project on your own.  Do not
discuss with anybody except 320 staff (mentors, TAs, instructor).

