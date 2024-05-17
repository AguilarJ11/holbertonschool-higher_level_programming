class Square:
    def __init__(self, size=0, position=(0, 0)):    
        self.size = size
        self.position = position
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
         @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position     
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for t in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
