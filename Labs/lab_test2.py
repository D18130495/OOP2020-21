# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# Yushun Zeng
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.__characters = []
        self.__cursor = 0
        self.__file_name = file_name

    # get the characters
    @property
    def full_characters(self):
        return self.__characters

    # set the characters
    @full_characters.setter
    def full_characters(self, value):
        self.__characters = value

    # get the length of the cursor
    @property
    def cursor_length(self):
        return self.__cursor

    # set the value of the current cursor
    @cursor_length.setter
    def cursor_length(self, value):
        self.__cursor = value

    # getter to get the files name
    @property
    def file_name(self):
        return self.__file_name

    # setter to set the file name
    @file_name.setter
    def file_name(self, value):
        # if value of files not a string:
        if type(value) != str:
            raise TypeError

        self.__file_name = value

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.full_characters.insert(self.cursor_length, character)
        self.cursor_length += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """

        if self.cursor_length <= len(self.full_characters):
            del self.full_characters[self.cursor_length]
        else:
            print('backward steps is greater than the length of characters')


    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.file_name, 'w') as f:
            f.write(''.join(self.full_characters))

        print(f"Your file {self.file_name} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor_length += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        # cursor can not greater then steps, if 10 characters in the self.characters
        # backward can not back over 10 characters
        if self.cursor_length >= steps:
            self.cursor_length -= steps
        else:
            raise ValueError


# initialising an object and using the class
doc = Document("lab_t2.txt")

# Ask input and check if it a string
keep_input = True

while keep_input:
    try:
        characters = str(input("Enter your text: "))
    except:
        print("Enter a string")
        continue

    for letter in characters:
        doc.insert(letter)

    keep_input = False

doc.backward(4)
doc.delete()
doc.insert('n')
doc.save()
