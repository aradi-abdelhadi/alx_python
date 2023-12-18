class BaseGeometry:
    '''Base class for Geometry'''

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        """Public instance method: def area(self): that raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

