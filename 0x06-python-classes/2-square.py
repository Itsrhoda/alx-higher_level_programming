#!/usr/bin/python3
''' A Module that creates a Square object '''

class Square;
''' Creating an Object template '''

    def __init__(self, size = 0):
        '''

            The init method initializes that class instance

        @self:
            A parameter used to refer to the class instance

        @size:
            The sizze of the square, must be a +ve integer
        '''
        If type(sizze) is int:
            if size < 0:
                raise ValueError('Size must be >= 0')
            else:
                    self.__size = size
        else:
            raise TypeError('Size must be an integer')
