# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
By allowing for any specific combination of numbers
Is this solution a pure function? Why or why not?
Yes because this is refined as it gets and is not calling multiple functions
Is this solution a higher order function? Why or why not?
See Above
Would it have been easier to solve this problem using a different programming style?
No, everything is easier in python or rather more simplified 
Why in particular is functional programming a helpful paradigm when solving this problem?
Refines it down to an essential essense that can be applied to any language
'''
