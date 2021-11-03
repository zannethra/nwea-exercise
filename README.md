# nwea-exercise
Here we have two implementations of the flatten function in Python 3.8.9. I do not consider myself fluent in Python but thought it would be nice
to demonstrate that I can find my way around in it. And by doing this excercise (especially exploring the tail recursion option) I learned some
things about Python, such as the fact that parameters with defaults behave like static variables, so it was useful for me.

In "real life," I would choose the iterative approach because it is far more readable, and Python doesn't support tail recursion anyway. (Implementing
a tail recursion version was simply a fun extra challenge that I couldn't resist, even after determining that it wouldn't solve my recursion problem 
because it is unsupported.) I suspect handling lists nested over 900 levels deep is beyond the scope of what you are looking for in this exercise, but
if I needed to solve the deep nesting problem in real life, I would likely choose a language that supports tail recursion. On the flip side, the need to 
support lists nested that deeply is a very specific edge case that wouldn't arise in most real world applications, so if it was well beyond the limits
of expected inputs, I would simply note the issue and implement it in whatever language was most convenient.
