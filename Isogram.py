def is_isogram(string):
    a = "abcdefghijklmnopqrstuvwxyz"
    string = [x for x in string.lower() if x in a]
    return len(string) == len(set(string))