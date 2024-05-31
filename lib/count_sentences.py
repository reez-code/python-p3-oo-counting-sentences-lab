#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    if type(value) == str:
      self.value = value
    
    print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    first_step = self.value.replace("?", ".")
    second_step = first_step.replace("!", ".")
    third_step = second_step.split(".")
    while("" in third_step):
      third_step.remove("")
    return len(third_step)

