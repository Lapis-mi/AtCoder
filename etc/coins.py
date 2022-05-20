# coding: UTF-8
def coins():
  a = int(input())
  b = int(input())
  c = int(input())
  x = int(input())
  count = 0
  for aNum in range(a+1):
    for bNum in range(b+1):
      for cNum in range(c+1):
        sum = aNum * 500 + bNum * 100 + cNum * 50
        if sum == x:
          count += 1

  print(count)

coins()