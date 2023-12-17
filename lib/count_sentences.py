#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        return False

    def count_sentences(self):
        if not self.value:
            return 0

        sentences = [sentence for sentence in self.value.split('.') if sentence]
        sentences = [sentence for sublist in [sentence.split('!') for sentence in sentences] for sentence in sublist if sentence]
        sentences = [sentence for sublist in [sentence.split('?') for sentence in sentences] for sentence in sublist if sentence]
        
        return len(sentences)

# Example usage with corrected test cases:
string = MyString()
string.value = "Hello World."
assert string.is_sentence() == True

string.value = "Is anybody there?"
assert string.is_question() == True

string.value = "It's me!"
assert string.is_exclamation() == True

simple_string = MyString()
simple_string.value = "one. two. three?"
assert simple_string.count_sentences() == 3
