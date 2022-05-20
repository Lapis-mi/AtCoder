# coding: UTF-8
def sunuke():
  # 例 3
  n = int(input())

  # 例 4 8 12
  # ↓はPython2系のinputなので、菊池さんは前の答えと同じinputを使ってください
  arr = list(map(int, raw_input().split()))
  
  count = 0
  boolean = True

  while boolean:
    # arrという配列の要素全てに実行するプログラムを書く
    # n回繰り返すfor文。（iに入るのは0,1,2)
    for i in range(n):
      if arr[i] % 2 == 0:
        arr[i] = arr[i]/2
      else:
        boolean = False
    if boolean == True:
      count += 1

  print(count)

sunuke()