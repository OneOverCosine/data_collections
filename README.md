# Data Collections in Python
Some data collections in Python include:
- Lists
- Tuples
- Dictionaries
- Sets
- etc.

## What is a list?
Lists are commonly used to store related data  
The are mutable - the data in them can be changed  
In Python, lists are create like so:
```python
shopping_list = ["bread", "chocolate", "avocados", "milk"]
```
### You need to use square brackets - ``()`` will create a tuple instead  
---
### Indexing
You can access items in a list by indexing to them

```python
print(shopping_list[0])
print(shopping_list[-2]) # negative indexing also works
```
Output:
```
bread
avocados
```
---
### A List's Mutability
Since lists are mutable, you can replace items  
Using the list from earlier...
```python
shopping_list[0] = "orange" # Use assignment to overwrite an item in a list
```
... the list you're left with: ``
['orange', 'chocolate', 'avocados', 'milk']
``

You can add items too with ``append()``
```python
shopping_list.append("apple juice")
```
And you get: ``['orange', 'chocolate', 'avocados', 'milk', 'apple juice']``

And delete, using ``pop()`` or ``remove()``
```python
shopping_list.pop(0) # returns the value you delete
shopping_list.remove("orange")
```
to get: ``['chocolate', 'avocados', 'milk', 'apple juice']``

## Mixed Lists
You can have lists with different datatypes
```python
mixed_list = [1, 2, 3, "one", "two", "three"]
```