#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
    self.value=value
    
  def get_value(self):
    return self._value

  def set_value(self, value=""):
    if (type(value) == (str)):
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value,)

  def is_sentence(self):
    return (self.value[(len(self.value)-1)] == ".")

  def is_question(self):
    return (self.value[(len(self.value)-1)] == "?")

  def is_exclamation(self):
    return (self.value[(len(self.value)-1)] == "!")
  
  def count_sentences(self):
    sentence_endings = ["!", "?", "."]
    num_sentences = 0
    for char in range(len(self.value)):
      if self.value[char] in sentence_endings and (self.value[char] != self.value[char-1]):
        num_sentences += 1
        print(self.value[char])
    return num_sentences


