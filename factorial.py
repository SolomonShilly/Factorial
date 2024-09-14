def factorial(int):
  n = 1
  solution = 0
  while int >= n:
    # 5 + 4 + 3 + 2 + 1
    solution = solution + n
    n += 1
  return solution

number = 5
factorial(number)
