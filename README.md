# python-prog-asst01
Python programming. First assignment. 1. Ramp up. 2. Augment an algorithm.

## I. Python ramp up

1. Console play.
   
   Python is an _interpreted_ language. This means that it is read and executed line-by-line by the interpreter. More on the interpreter later. This enables Python to have an _interactive console_, where you can type a single-line expression at the console prompt and have it evaluated upon hitting **Enter/Return**.
   
   In PyCharm, click on the **Python Console** in the bottom bar to open a console.
   
   Write the following types of expressions on the console. When you are done, select all the contents of the Python console and overwrite the contents of the `console.log` file in the repository.
   
   a. Numbers, integers or reals. They evaluate to themselves. These are called _primitive datatypes_.
   
   b. Strings, that is, text in _single quotes_ or _double quotes_ (e.g. 'computer' or "computer"). They evaluate to themselves.
   
   c. Assignments (e.g. `a = 6` or `string = 'engineering'`). They evaluate to the value of the right-hand side (without displaying the value), but have the side effect that they _declare_ a variable with the name on the left-hand side. In PyCharm, you will see the declared variables in the window on the right.
   
   d. Expressions with variables (e.g. `a + b` or `'engine' + 'ering'`). "Addition" of strings is _concatenation_.
   
   e. Complex assignments (e.g. `c = a + 3 + 2*b` or `'deadbeef' * 5`) using the built-in [operators](https://www.tutorialspoint.com/python/python_basic_operators.htm). Try _arithmetic_, _comparison_ (e.g. `a > 8`) _assignment_, _bitwise_ (e.g. `a ^ b`), and _logical_ (e.g. `not (a <= 9)`) operators. Logical and comparison operations evaluate to the _boolean_ values `True` or `False`.
   
   f. Declare a **list** (e.g. `l = []`), one of the principal built-in complex datatypes in Python, append to it (e.g. `l.append('aes dana')` and `l.append(45)`) several times, and examine the list to see how it accumulates the appended values. You can also see it on the right. **Note:** Appending happens to the _end_ of the list.

   g. PyCharm has very rich _autocompletion_. After doing the previous exercise, type `l.` at the console prompt and see the pop-up drop-down menu with all the methods you can execute against the list `l`, along with the familiar `append`. Try a few to see what they do.
   
   h. Declare a **dictionary** (e.g. `d = {}`), the other principal built-in complex datatype in Python, add elements to it (e.g. `d[0] = 'zero'` and `d['mana'] = 'Mexican pop group'`), query if for elements (e.g. `d[0]` and `d[1]`), and display it with `d` to see how it changes. You can, of course, see it on the right.
   
   i. Do the autocompletion trick from above with the dictionary `d` to see what methods it has. 
   
   j. In Python, everything is an _object_ (a collection of data and the methods that can be executed on the data). Objects are _instances_ of _classes_. For example, the dictionary `d` is of type `<class 'dict'>`. Try it yourself: type `type(d)`, `type(l)`, `type('abba')`, and `type(5)` at the console prompt. For this reason, Python is considered an _object-oriented_ language.
   
2. Executing a script.

   Python is considered a _scripting_ language, meaning that you can write a bunch of lines of Python in a file and then "run" the script (that is, the file). It will be executed line-by-line, from top to bottom.
   
   Files afford a much more flexible and rich _syntax_. For example, we can create _loops_, define _functions_ and _classes_, control the flow of our program with conditional statements, etc.
   
   Note that if you want output from the running of a file, you need to insert `print` statements (e.g. `print('blah-blah')` or `print(d)`).
   
   Try the following code in a file and run the file after each new statement.
   
   a. For each of the items you typed in the console, type them in the file, and run the script.
   
   b. Create a `for` loop with `range`... TODO
   
   c. Create a `for` loop with `in`... TODO
   
   d. Create a `while` loop without `break`... TODO
   
   e. Create a `while` loop with `break`... TODO
   
   f. Create a conditional statement `if... else...`... TODO
   
   g. Run a loop with a conditional statement... TODO
   
   h. Run a loop that breaks if a condition is `True`... TODO
   
   i. Define a function... TODO
   
   j. Run a function inside a loop... TODO

   
## II. Bubble sort

1. Understand the algorithm in the abstract... TODO

2. Understand the code... TODO

3. Modify the code... TODO

