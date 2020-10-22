class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def ScrambleW(self):
        print("The user input was: ", self.user_input)

        if len(self.user_input) > 3:
            new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] \
                  + self.user_input[3:]
        else:
            new_word = self.user_input

        print(new_word)

    def ScrambleS(self):
        print("The user input was: ", self.user_input)

        sentence = self.user_input.strip().split()

        for index, word in enumerate(sentence):
            if len(word) > 3:
                temp_word = list(word)
                temp = temp_word[1]
                temp_word[1] = temp_word[2]
                temp_word[2] = temp

                swapped_word = ''.join(temp_word)
                sentence[index] = swapped_word
            else:
                sentence[index] = word

        the_swap = ' '.join(sentence)

        print(the_swap)


scramble = WordScramble()
#scramble.ScrambleW()
scramble.ScrambleS()