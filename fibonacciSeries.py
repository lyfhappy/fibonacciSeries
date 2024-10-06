def fibonacci(n):
  fib = [0,1]
  a1 = 0
  num = 1
  for num in range(1,n):
    a1 =  fib[num] + fib[num-1]
    fib.append(a1)

  print(f"Fibonacci :{fib}")


fibonacci(10)