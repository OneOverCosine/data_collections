# Data Collections in Python
Some data collections in Python include:
- Lists
- Tuples
- Dictionaries
- Sets
- etc.

## What is a list?
Lists are commonly used to store related data  
They are mutable - the data in them can be changed  
In Python, lists are create like so:
```python
shopping_list = ["bread", "chocolate", "avocados", "milk"]
number_list = [13, 42, 6.02, 23, 3.12]
```
You need to use square brackets - ``()`` will create a tuple instead  

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
---
## What is a Tuple?
Like lists, tuples are used to hold related data  
Unlike lists, they are immutable. This means that the data in them cannot be modified
You declare a tuple like so:
```python
weekdays_de = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
```
Tuples are ideal to use for information that doesn't change. Days of the week or dates of birth and death could be stored in a tuple as they don't change  

Remember that tuples are immutable.
```python
weekdays_de[0] = "Monday" # throws an error
```

This is useful for storing data you don't want to accidentally overwrite!  
The following code runs without errors
```python
shopping_list = ["bread", "chocolate", "avocados", "milk"]
mixed_list = [1, 2, 3, "one", "two", "three"]

tuple_of_lists = (shopping_list, mixed_list)
print(tuple_of_lists) # returns (['bread', 'chocolate', 'avocados', 'milk'], [1, 2, 3, 'one', 'two', 'three'])

tuple_of_lists[0][1] = "M 'n Ms"
print(tuple_of_lists) # returns (['bread', "M 'n Ms", 'avocados', 'milk'], [1, 2, 3, 'one', 'two', 'three'])
```
This is because you're changing the *list* and not where the tuple is pointing to. This technically means that you can modify the contents of a tuple, but this is an odd case

## Dictionaries
Dictionaries use key, value pairs to store data  
Data can be retrieved by its ``key`` or ``value``
Syntax:
```python
dev_ops_student = {
    dev_ops_student = {
    "name" : "Cringe Katalyst",
    "stream" : "DevOps",
    "completed_lessons" : 3,
    "completed_lessons_names" : ["Variables", "Data Types", "Collections"]
}
}
```

You can also declare lists inside a dictionary

### Indexing in Dictionaries
You use the keys to return a value
```python
print(dev_ops_student["name"]) # returns 'Cringe Katalyst'
```

This dictionary has a list in it. To get ``Data Types`` from the list you write:
```python
dev_ops_student["completed_lessons_names"][1]
```

``my_dictionary.keys()`` returns all the keys in the dictionary  
Similarly, ``my_dictionary.values()`` returns all the values

## Sets
These are like lists, but they are unordered
```python
car_parts = {"wheels", "windows", "doors"}
```
You declare them using ``{}``  

To add to a set you use the ``add(item)`` method
```python
car_parts.add("seats")
```
To delete an item use ``discard(item)``
```python
car_parts.discard("doors")
```
---
### Frozen Sets