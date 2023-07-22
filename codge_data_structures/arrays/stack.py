"""
Docstring Generated by Copilot:
===============================
Stacks are a very common data structure and it's going to be important that
you know how to implement one. The basic idea is that you can add and remove
items from the "top" of the stack in O(1) time. You can think of it like a stack
of plates. If you want to add a plate to your stack, you just place it on the
top. If you want to remove a plate from the stack, you always remove it from
the top. Last plate added is the first plate that gets removed. This is called
LIFO (Last In First Out).

I'm going to need you to do some work for me. I need you to write a class for
a stack. It should have the methods push, pop, and size. LIFO (last in first
out) means that the last element added to the stack should be the first one
removed. So if you push on 3, and then push on 2, and then push on 1, you'll
need to pop off 1 first, then 2, then 3. Make sure you return the value that
is being popped off.

Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.size() # should return 3
s.pop() # should return 3
s.pop() # should return 2
s.pop() # should return 1
s.size() # should return 0
"""



if __name__ == '__main__':
    import doctest
    doctest.testmod()
