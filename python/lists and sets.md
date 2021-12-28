# Lists

Lists are the Python equivalent of arrays in other languages. You use brackets to create a list. They can be sliced, diced, appended, etc. compared to tuples. They are created by using brackets.

        List=[]


## List Methods
### append()

        cards=["Empress", "Hierophant"]
        cards.append("The Fool")
        print (cards)
        ['Empress', 'Hierophant', 'The Fool']

## List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

        newlist = [expression for item in iterable if condition == True]

### Examples
*Only accept items that are not "apple"*

      newlist = [x for x in fruits if x != "apple"]
     
*We see how this performs a function on a list*

        vec = [2, 4, 6]
        [3*x for x in vec]
        [6, 12, 18]


*Here we apply a method call to each item in a sequence*

        [[x, x**2] for x in vec]
        [[2, 4], [4, 16], [6, 36]]


*Allows you to multiple two values by one another*

        vec1 = [2, 4, 6]
        vec2 = [4, 3, -9]
        print([x*y for x in vec1 for y in vec2])
        [8, 6, -18, 16, 12, -36, 24, 18, -54]


# Sets

An unordered collection of objects used when membership and uniqueness are main things you need to know.

Are immutable and hashable: ints, floats and strings can be members of a set but lists and dictionaries can't be.

## Find unique members of a list using sets 

        numbers = [1, 2, 2, 3, 3, 4, 5]
        unique_numbers = list(set(numbers))
        print(unique_numbers)
        # Result: [1, 2, 3, 4, 5]


