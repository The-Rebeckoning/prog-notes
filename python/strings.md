# Strings 
Strings processing works very well in python. 

They can be delimited by a single (' '), double (" "), triple single (''' ''') or triple double (""" """).

They can also contain a tab (\t) or newline (\n) character.

        test_string = "Rebecca"
        test_string
        'Rebecca'
       
## Indexing

By referencing index numbers, we can isolate one of the characters in a string. We do this by putting the index numbers in square brackets. 

        ss = "Sammy Shark!"
        print(ss[4])
 
        Output
        y

### index()

The index() method returns the index of a substring inside the string (if found). 

        text = 'Python is fun'

        # find the index of is
        result = text.index('is')
        print(result)
        # Output: 7
    
### str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

        print 'ab123'.isalnum()
        True
        print 'ab123#'.isalnum()
        False

### str.isalpha()

This method checks if all the characters of a string are alphabetical (a-z and A-Z).

        print 'abcD'.isalpha()
        True
        print 'abcd1'.isalpha()
        False

### str.isdigit()
This method checks if all the characters of a string are digits (0-9).

        print '1234'.isdigit()
        True
        print '123edsd'.isdigit()
        False

### str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

        print 'abcd123#'.islower()
        True
        print 'Abcd123#'.islower()
        False

### str.isupper()
Return true if all cased characters 4 in the string are uppercase and there is at least one cased character, false otherwise.

For 8-bit strings, this method is locale-dependent.

### .upper
The upper() method returns a string where all characters are in upper case.

        txt = "Hello my friends"
        x = txt.upper()
        print(x)
        HELLO MY FRIENDS
### . count()

The count() method returns the number of occurrences of a substring in the given string.

        Example
        message = 'python is popular programming language'
        number of occurrence of 'p'
        print('Number of occurrence of p:', message.count('p'))
        Output: Number of occurrence of p: 4
        
        
### split()

Use str.split() with a string as str to return a list with each element as a word in the string. Use len(iterable) with the list as iterable to count the number of elements.

        a_string = "one two three"
        word_list = a_string.split()
        Split `a_string` by whitespace

        number_of_words = len(word_list)
        print(number_of_words)
        
        3

### capitalize()

The capitalize() method returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter while making all other characters in the string lowercase letters.

    s = "rebecca anne hayes"
    list_of_names=s.split()
    full_cap_name_list = []
    result = ""
    for name in list_of_names:
        full_cap_name_list.append(name.capitalize())
    for name in full_cap_name_list:
        result=result+str(name)+" "
    
    print (full_cap_name_list)
    
    Rebecca, Anne, Hayes

###strip()

strip() returns a new string after removing any leading and trailing whitespaces including tabs (\t).
