# Python

Reference: 
- https://www.youtube.com/watch?v=EOLPQdVj5Ac
- https://cs50.harvard.edu/web/2020/weeks/2/

## Variables

🗂️ [variables.py](variables.py)

Primitive types:

```python
a = 1      # int
b = 0.5    # float
c = "hola" # str ("value" \ 'value')
d = True   # bool (True \ False)
e = None   # NoneType
```

## Conditions

🗂️ [conditions.py](conditions.py)

Indentation matters.

```python
if a > b:
    # do something
elif b < a:
    # do something
else:
    # do something
```

## Sequences & collections

🗂️ [sequences.py](sequences.py)

**Sequence** -> order matters   
**Collection** -> order doesn't matter

```python
# List (sequence of mutable values)
a = ["uno", "dos", "tres"]

# Tuple (sequence of inmutable values)
coordinates = (0, 50)

# Set (collection of unique values)
s = set()
s.add(1)
s.add(2)

# Dict (collection of key-value pairs)
zip_codes = {
    "26570": "Quel", 
    "28035": "Madrid"
}
```

## Loops

```python
for i in [1, 2, 3]:
  print(i)

for i in range(100):
  print(i)
```

## Functions

```python
def square(n):
    return n * n
```

## Classes (OOP)

🗂️ [classes.py](classes.py)

```python
class Point():
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def some_method(self):
        print(self.x)


p = Point(10, 20)
p.some_method()
```

## Decorators (FP)

🗂️ [decorators.py](decorators.py)

```python
def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done!")
    return wrapper


@announce
def hello():
    print("Hola mundo")

hello()
```

## Lambdas (FP)

🗂️ [lambda.py](lambda.py)

Like JS arrow functions with implicit return.

```python
# normal function
def get_name(person):
    return person["name"]

# lambda expression
lambda person: person["name"]
```

## Exceptions

🗂️ [exceptions.py](exceptions.py)

```python
try:
    # do something
except ZeroDivisionError: # Exception type
    # catch exception 
    sys.exit(1) # exit with error (optional)
```