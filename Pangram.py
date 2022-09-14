def is_pangram(string):
  stringa = [char for char in string.lower() if 'a' <= char <= 'z']
  set_of_letters = set(stringa)
  return len(set_of_letters) == 26