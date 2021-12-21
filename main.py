import math

def calculation(c):
  z = math.cos(c)
  if (z < 0):
    y = math.sin(z) + math.tan(z)
  elif (z > 8):
    y = z ** 2 + math.log(z ** 2)
  else:
    y = (math.cos(z)) ** 3 + 3 / z
  return y

enter = float(input('Введите c: '))
answer = calculation(enter)
print('y равняется', answer)
