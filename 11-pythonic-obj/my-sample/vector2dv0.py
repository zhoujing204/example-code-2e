from array import array
import math

class Vector2D:
    """A vector2D class
    
    <1> typecode is a class attribute we'll use when 
    converting Vector2d instances to/from bytes.
    
    <2> __iter__ makes a Vector2d iterable;
    this is what makes unpacking work(e.g., x, y = my_vector).
    We implement it simply by using a generator expression to yield
    the components.
    
    <3> __repr__ builds a string by interpolating the components with {!r}
    to get their repr; *self feeds the x and y components to format.
    
    <4> __str__ is to build a tuple and feed it to str.
    
    <5> __bytes__ writes the byte representation by concatenating the typecode.
    
    <6> We iterate over the Vector fields to build an array of bytes.
    
    <7> __eq__ uses the tuple(self) to compare the components of both vectors.
    
    <8> __abs__ uses hypot to compute the magnitude.
    
    <9> __bool__ uses abs(self) to compute the magnitude, then converts it to bool,
    so 0.0 becomes False, nonzero values become True.
    
    
    """
    
    typecode = 'd' # <1>
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __iter__(self):
        return (i for i in (self.x, self.y)) # <2>
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) # <3>  
    
    def __str__(self) -> str:
        return str(tuple(self)) # <4>
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + # <5>
                bytes(array(self.typecode, self))) # <6>
    
    def __eq__(self, other):
        return tuple(self) == tuple(other) # <7>
    
    def __abs__(self):
        return math.hypot(self.x, self.y) # <8>
    
    def __bool__(self):
        return bool(abs(self)) # <9>
    

    