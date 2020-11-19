"""
20.5. Adding Other Methods to a Class
The key advantage of using a class like Point rather than something like a simple tuple (7, 6) now becomes apparent. We can add methods to the Point class that are sensible operations for points. Had we chosen to use a tuple to represent the point, we would not have this capability. Creating a class like Point brings an exceptional amount of “organizational power” to our programs, and to our thinking. We can group together the sensible operations, and the kinds of data they apply to, and each instance of the class can have its own state.

A method behaves like a function but it is invoked on a specific instance. For example, with a list bound to variable L, L.append(7) calls the function append, with the list itself as the first parameter and 7 as the second parameter. Methods are accessed using dot notation. This is why L.append(7) has 2 parameters even though you may think it only has one: the list stored in the variable L is the first parameter value and 7 is the second.

Let’s add two simple methods to allow a point to give us information about its state. The getX method, when invoked, will return the value of the x coordinate.

The implementation of this method is straight forward since we already know how to write functions that return values. One thing to notice is that even though the getX method does not need any other parameter information to do its work, there is still one formal parameter, self. As we stated earlier, all methods defined in a class that operate on objects of that class will have self as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.
"""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Point(7,6)
print(p.getX())
print(p.getY())
