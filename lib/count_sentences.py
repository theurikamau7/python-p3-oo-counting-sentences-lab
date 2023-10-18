#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print('The value must be a string.')
    value = property(get_value, set_value)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        
        sentence_endings = r'[.!?]'
        sentences = re.split(f'(?<={sentence_endings})\s+', self.value)
        # Filter out empty strings and strings that only contain punctuation
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)