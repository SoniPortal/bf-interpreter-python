# bf-interpreter-python
An interpreter for the language brainfuck written in Python.


## Use:
```python
bf = Brainfuck() # For a custom number of cells, put the amount of cells you want between the brackets, e.g.
bf = Brainfuck(256) # The default amount of cells is 30000.

# To run a program:
bf.run('program') # replace program with the program you want to run, e.g.
bf.run(',[>,]<[.<]')

# To reset the tape to 0 (e.g. before running another program):
bf.reset()
```

## TODO:
* add option to configure live input when running (choice of one character input every time necessary or supply with full input at start)
* different cell sizes, e.g.
  * byte per cell
  * two bytes per cell
  * unbounded integer
  * zero+positive integers (raising error on below zero)
  * custom
* different memory types, e.g.
  * non-wrapping (raising error when outside of memory range)
  * unbounded
  * unbounded in positive direction
