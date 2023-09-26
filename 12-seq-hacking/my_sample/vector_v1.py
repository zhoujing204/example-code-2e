from array import array
import reprlib
import math

class Vector:
    
    typecode = 'd'
    
    def __init__(self, components):
        """Initiate the Vector instance. The self._components instance
        "protected" attribute will hold an array with the Vector components.        
        """
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        """Iterate the items of _components. This method is called when
        tuple(self) appear. Return an iterator over self._components.
        """
        return iter(self._components)
    
    def __repr__(self):
        """
        <3> Use reprlib.repr() to get a limited-length representation of
        self._components(e.g. array('d',[0.0, 1.0, 2.0, 3.0, 4.0, ...]))
        <4> Remove the array('d', prefix, and the trailing) before plugging
        the string into a Vector constructor call.
        Return the formatted string of the Vector instance. 
        
        Because of repr's role in debugging, calling repr() on an object
        should never raise an exception. If something goes wrong inside
        your implementation of __repr__, you must deal with the issue and
        do your best to produce some serviceable output that gives the user
        a chance of identifying the receiver(self).       
        """
        components = reprlib.repr(self._components) # <3>
        components = components[components.find('['):-1] # <4>
        return f'Vector({components})'
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        """Build a bytes object directly from self._components"""
        return (bytes([ord(self.typecode)]) +  
                bytes(self._components))  # <5>
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        """Since Python 3.8 math.hypot accepts N-dimensional points.
        The return ia as same as the expression: 
        math.sqrt(sum(x*x for x in self)).
        """
        return math.hypot(*self)   # <6>
    
    def __bool__(self):
        """Return True if abs(self) is not zero, otherwise return False."""
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        """Pass the memoryview directly to the constructor, without 
        unpacking with * as we did before.
        """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)    # <7>
    
    