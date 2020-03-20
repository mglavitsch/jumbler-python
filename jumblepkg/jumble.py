import random


class Jumbler:
    """
    A class for jumbling letters within words.
    """

    def __init__(self, text):
        """
        This method is automatically invoked by class instantiation.
        The 2nd argument is used to initialize the class attribute self.text.

        Arguments:
        self -- instance of the class
        text -- text to be jumbled
        """
        self.text = text

    @staticmethod
    def get_char_code_point_ranges():
        """
        Returns the list of character code point ranges where each
        UTF-8 code point of a range represents a valid character.
        A range is a two-element list with the start and end code point
        of a valid character code point range.
        """
        return [
            [0x41, 0x5a],
            [0x61, 0x7a],
            [0xc0, 0xd6],
            [0xd8, 0xf6],
            [0xf8, 0xff]
        ]

    @staticmethod
    def is_jumbable(word):
        """
        This static class method checks if the given word is jumbable,
        i.e. the word "moon" is not jumbable.

        Argument:
        word -- word to be checked
        """
        if not(isinstance(word, str)) or len(word) < 4:
            return False
        equal = True
        for i in range(1, len(word)-2):
            equal = equal and word[i:i+1] == word[i+1:i+2]
            # print(i, word[i:i+1], word[i+1:i+2], equal)
            if not(equal):
                return True
        return False

    @staticmethod
    def word(word, force=False, seed=None, max=1000):
        """
        This static class method changes the given word in that it keeps the
        first and the last character and randomly jumbles the characters of
        slice [1:len(word)-1].

        Arguments:
        word -- word to be jumbled
        force -- force jumbling (default False)
        seed -- seed for pseudo-random number generator (default None)
        max -- stop trying to force the jumbling after this number of attempts
        """
        if not(isinstance(word, str) and
               isinstance(force, bool) and
               isinstance(max, int) and
               Jumbler.is_jumbable(word)):
            return word
        if isinstance(seed, int):
            random.seed(seed)
        cnt = 0
        condition = True
        new_word = ""
        while condition:
            sub_word = word[1:-1]
            new_word = word[0]
            while len(sub_word) > 0:
                r = random.randint(0, len(sub_word)-1)
                new_word = new_word + sub_word[r]
                sub_word = sub_word[0:r] + sub_word[r+1:]
            new_word = new_word + word[-1]
            cnt += 1
            # print(cnt, new_word)
            condition = force and new_word == word and cnt < max

        return new_word

    def get_indices(self):
        """
        Takes the class attribute self.text and returns a list of ranges
        where each range represents the start and end index of a word
        in the format of a two-element list.

        Argument:
        self -- instance of the class
        """
        indices = []
        if not(isinstance(self.text, str)) or len(self.text) == 0:
            return indices
        code_point = -1
        character = True
        word = False
        start = end = -1
        for i, ch in enumerate(self.text):
            character = False
            code_point = ord(ch)
            # print(i, ch, code_point)
            for r in Jumbler.get_char_code_point_ranges():
                if r[0] <= code_point and code_point <= r[1]:
                    character = True
                    break
            if not(word) and character:
                start = i
                word = True
            elif word and not(character):
                end = i - 1
                word = False
                indices.append([start, end])
        if word:
            indices.append([start, len(self.text)-1])
        return indices

    def get_jumbled_text(self, force=False, seed=None):
        """
        Takes the class attribute self.text, identifies the words and
        jumbles the characters of those words.

        Arguments:
        self -- instance of the class
        force -- force jumbling (default False)
        seed -- seed for pseudo-random number generator (default None)
        """
        result = self.text
        indices = self.get_indices()
        if len(indices) == 0:
            return self.text
        jumbled_word = ""
        if isinstance(seed, int):
            random.seed(seed)
        for r in indices:
            if r[1] - r[0] > 2:
                jumbled_word = Jumbler.word(
                    self.text[r[0]:r[1]+1], force)
                result = result[0:r[0]] + jumbled_word + \
                    result[r[1]+1:len(result)]
        return result
