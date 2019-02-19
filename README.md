# First programming assignment in Python


## I. Python ramp up

1. Console play and experiment.
   
   Python is an _interpreted_ language. This means that it is read and executed line-by-line by the interpreter. More on the interpreter later. This enables Python to have an _interactive console_, where you can type a single-line expression at the console prompt and have it evaluated upon hitting **Enter/Return**.
   
   In PyCharm, click on the **Python Console** in the bottom bar to open a console.
   
   Write the following types of expressions on the console. When you are done, select all the contents of the Python console and overwrite the contents of the `console.log` file in the repository.
   
   1. Numbers, integers or reals. They evaluate to themselves. These are called _primitive datatypes_.
   
   2. Strings, that is, text in _single quotes_ or _double quotes_ (e.g. 'computer' or "computer"). They evaluate to themselves.
   
   3. Assignments (e.g. `a = 6` or `string = 'engineering'`). They evaluate to the value of the right-hand side (without displaying the value), but have the side effect that they _declare_ a variable with the name on the left-hand side. In PyCharm, you will see the declared variables in the window on the right.
   
   4. Expressions with variables (e.g. `a + b` or `'engine' + 'ering'`). "Addition" of strings is _concatenation_.
   
   5. Complex assignments (e.g. `c = a + 3 + 2*b` or `'deadbeef' * 5`) using the built-in [operators](https://www.tutorialspoint.com/python/python_basic_operators.htm). Try _arithmetic_, _comparison_ (e.g. `a > 8`) _assignment_, _bitwise_ (e.g. `a ^ b`), and _logical_ (e.g. `not (a <= 9)`) operators. Logical and comparison operations evaluate to the _boolean_ values `True` or `False`.
   
   6. Declare a **list** (e.g. `l = []`), one of the principal built-in complex datatypes in Python, append to it (e.g. `l.append('aes dana')` and `l.append(45)`) several times, and examine the list to see how it accumulates the appended values. You can also see it on the right. **Note:** Appending happens to the _end_ of the list.

   7. PyCharm has very rich _autocompletion_. After doing the previous exercise, type `l.` at the console prompt and see the pop-up drop-down menu with all the methods you can execute against the list `l`, along with the familiar `append`. Try a few to see what they do.
   
   8. Declare a **dictionary** (e.g. `d = {}`), the other principal built-in complex datatype in Python, add elements to it (e.g. `d[0] = 'zero'` and `d['mana'] = 'Mexican pop group'`), query if for elements (e.g. `d[0]` and `d[1]`), and display it with `d` to see how it changes. You can, of course, see it on the right.
   
   9. Do the autocompletion trick from above with the dictionary `d` to see what methods it has. 
   
   10. In Python, everything is an _object_ (a collection of data and the methods that can be executed on the data). Objects are _instances_ of _classes_. For example, the dictionary `d` is of type `<class 'dict'>`. Try it yourself: type `type(d)`, `type(l)`, `type('abba')`, and `type(5)` at the console prompt. For this reason, Python is considered an _object-oriented_ language.
   
2. Executing a script.

   Python is considered a _scripting_ language, meaning that you can write a bunch of lines of Python in a file and then "run" the script (that is, the file). It will be executed line-by-line, from top to bottom.
   
   Files afford a much more flexible and rich _syntax_. For example, we can create _loops_, define _functions_ and _classes_, control the flow of our program with conditional statements, etc.
   
   Note that if you want output from the running of a file, you need to insert `print` statements (e.g. `print('blah-blah')` or `print(d)`).
   
   Create a new Python file in the assignemtn project directory on the left. Then try the following code in a file and run the file after each new statement.
   
   1. For each of the items you typed in the console, type them in the file, and run the script.
   
   2. Loops allow repetitive execution of the same (or similar) code. In general, loops run until some terminal condition becomes `True`, at which time the loop terminates. There are two major types of loops in Python (and most of the other languages): `for` loops and `while` loops. `for` loops have a loop variable, which changes its value each time through the loop. There are two major varieties of `for` loops: with `range` and `in`. The `range()` is a function that takes arguments and returns an _iterable_ object, that is, an object that can supply the next (different) value for the loop variable. It looks as follows:
   
      ```python
      for i in range(10):
       print(i)
      ```
   
      Run this loop. Notice the following:
        - the loop variable is `i`
        - the `range(10)` function makes `i` change its value in order from 0 to 9
        - there is a _colon_ (`:`) at the end of the `for` statement, which marks the start of the beginning of the loop's _code block_
        - the code block is indented **4 spaces** in relative to the `for` keyword, and contains just a `print()` statement
     
      Create a `for` loop with `range` of your own. Experiement with `range` and different code in the code block. The code may or may not depend directly on the value of `i`.
   
   3. The second variety of `for` loop uses the operator `in`, which, when followed by a list, assigns the loop variable the values of consecutive elements of the list. It looks as follows:
    
      ```python
      l = [4, 5, 6]
      for i in l:
       print(i)
      ```
   
      Run this loop to observe its behavior. Create your own `for` loop with `in`. Experiment with the list elements and code block that depends on `i`. 
   
   4. The `while` loop takes a condition and executes until the condition evaluates to `True`. Here is an example:
   
      ```python
      i = 8
      while i > 0:
          print(i)
          i = i - 1
      ```
   
      Run this loop. Notice the following:
        - the condition is `i > 0` and depends on the current value of `i`
        - `i` is not a loop variable in the sense like the one in the `for` loops
        - the loop code block changes the value of `i`, in this case decrementing it
        - the moment `i` becomes zero, the loop will stop
      
      Create your own `while` loop and experiment with it.
   
   5. A `while` loop can stop if some condition becomes `True` _inside_ the code block itself. This is accomplished with the keyword `break`. Here is an example:
   
      ```python
      i = 8
      while True:
          if i <= 0:
              break
          i = i - 1
      ```
   
      Run this loop and think how it may be different from the one without a `break` statement. Also think in what cases one is may be preferable to the other and vice versa. Write your own `while` loop with `break` to illustrate.
   
   6. While playing with `while` loops, we also saw a _conditional statement_, namely the line starting with `if`. This is one of the most powerful tools in programming. It allows the programmer to control the order of execution of the code based on various conditions. Depending on the value of a condition, one of two code blocks is executed and the other bypassed and ignored. Here's an example:
   
      ```python
      i = 8
      if i > 0:
          print("i is greater than zero")
      else:
          print("i is less than or equal to zero")
      ```
   
      Notice the colons (`:`) at the end of the `if` and `else` statements and the **4-space** indentation of their corresponding code blocks. Create your own `if` conditional statement and experiment with it.
   
   7. Write your own loop with a conditional statement in the code block which causes the result of the execution of the code block to be different each time through the loop. Here is an extended variety of the `if` statement:
   
      ```python
      i = 8
      if i > 0:
          print("i is greater than zero")
      elif i < 4:
          print("i is between 0 and 4")
      else:
          print("i is greater than or equal to four")
      ```
   
      This variety allows you to check fine-grained conditions. You can have as many `elif` (which stands for _else if_) and the `else`, as with all `if` statements, is optional. Note that you have to be careful with stringing conditions like this because they are evaluated one after the other and the code block of the first one that evaluates to `True` is executed. Only insert a new condition which is _still possibly true_ after all the conditions before it have evaluated to `False`. Experiment with the value of `i` and write your own `if` "cascades".  
   
   8. Create and run a loop that breaks if one of the conditions in an `if` cascade is `True`.
   
   9. A **function** is a _named code block_. The code block is executed when the function is _called_. Here's a very simple example:
   
      ```python
      def my_function():
          i = 8
          if i > 0:
              print("i is greater than zero")
          elif i < 4:
              print("i is between 0 and 4")
          else:
              print("i is greater than or equal to four")
      ```
      Run this code. Notice the following:
        - this is a _function definition_, which means defining the code block and its name
        - a definition always starts with the keyword `def`
        - notice the familiar colon (`:`) which indicates where the code block begins
        - each code block is indented **4 spaces in** relative to the one that contains it, in this case the blocks of the `if` cascade relative to the funcion's code block
        - the name of the function is `my_function`
   
      Write your own and experiment with it. Call the function by writing `my_function()` by itself on a line in a code block.
   
   10. The function above is more or less useless. The power of functions is that they are code blocks that can take input and give output. The input of a function is called **arguments** and they are declared between the parentheses after the function name. The output of the function (apart from any `print()` statements) is specified by a `return` statement. Here's an example of a slightly more useful function:
   
       ```python
       def add(a, b):
           return a + b
       ```
   
       This function is simple and self-explanatory. It takes two arguments and returns their "sum". Notice that there is no type checking: the arguments can be two integers, two floats, two strings, two whatever, or can be two different whatevers :-P If the `+` operator happens to not be defined for the two argument types, the interpreter will throw an error. Experiment with this function by calling `add(4, 7)`, `add(5.6, 0.1)`, and `add("my", "oh, my")`. If you want to see the output of the function, call it from inside a `print` statement as follows:
   
       ```python
       print(add(3, 9))
       ```
   
       Notice the _"nested"_ function calls. They are performed and evaluated from **inside-out**. Define and call your own functions.
   
   11. Define a function and call it from inside a condition which is inside a loop. Do you get a taste of the power of programming?

   
## II. Sorting algorithms

1. Understand the code. (Get used to have the [Python documentation](https://docs.python.org/3/index.html) open.)

   Now you know enough basic Python to be dangerous. For example, you are well equipped to understand the code of `bubble_sort()`.
   
   1. List the functions used in the file **bubble_sort.py**.
   
   2. Which functions are defined inside the file and which are defined elsewhere? Some of these function are _built-in_. See a [list of all built-in functions](https://docs.python.org/3/library/functions.html) in Python.
   
   3. How many loops are there in the code? Are any of them _nested_?
   
   4. How many conditional statements are there in the code? Are they nested in loops?
   
   5. What is the deepest level of nesting in the code?
   
   6. Does the `bubble_sort` function take any arguments? If yes, what helps us determine what type they have to be?
   
   7. How is the `bubble_sort` function called?
   
   8. How can the array that is will work on be declared **after** the definition of the `bubble_sort` function?
   
   9. Is the loop variable of the outer loop in the `bubble_sort` function underlined in your editor? If yes, hover over it with the mouse and see what the IDE says. Can you explain this?
   
   10. How about the argument of the function `bubble_sort`?
   
   11. Are there any nested function calls in the code?

2. Understand the algorithm in the abstract.

   1. Read the _inline comments_ in the code of **bubble_sort.py**.
   
   2. What does the outer loop of `bubble_sort()` do?
   
   3. What does the inner loop do?
   
   4. Prove that the last `i` numbers are already sorted correctly.
   
   5. If the array is already sorted, will the outer loop run? How about the inner loop?
   
   6. Modify the algorithm to print the current array after each "bubble" pass.

3. Write some code.

   1. Try the algorithm with a list of strings. Does it work? Explain how and why?
   
   2. Create a new file in the project called **sink_sort.py** and implement a `bubble_down` algorithm that sorts like `bubble_up`, but in reverse order.
   
   3. Read, run, and understand how the the algorithm in the **insertion_sort.py** works. Output the current array after each insertion pass.
    
   4. Write inline comments in the **insertion_sort.py** file to help with the quick reading and understanding of the code.
   
   5. Modify the algorithm in **insertion_sort.py** to sort in reverse order.

