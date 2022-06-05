# coding: UTF-8
def sunuke():
  n = int(input())

  # 例 4 8 12
  # ↓はPython2系のinputなので、菊池さんは前の答えと同じinputを使ってください
  arr = list(map(int, raw_input().split()))
  
  # arrを大きい順に並べ替える

  # アリスの得点は＋、ボブの得点は-として計算するためのsumという変数を準備
  sum = 0

  # 並べ替えた配列arr一個一個に対して処理していく（each文？）
    
    # if 配列0,2,4...番目なら、アリスの得点としてsumに＋する
    # else 配列1.3.5...番目なら、ボブの得点としてsumに-する

  # sumを出力する