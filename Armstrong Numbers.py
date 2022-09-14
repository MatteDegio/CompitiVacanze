def is_armstrong_number(number):
  return number == sum(int(k) ** len(str(number)) for k in str(number))
