n = gets.to_i
line = gets.split(" ").map(&:to_i).sort.uniq
len = line.length
x = line.length / 2 # 二分
daburi = n - line.length
p "長さ"
p n # 長さ
p "ダブり"
p daburi
p "line[x]"
p line[x]
p "真ん中の数字までの項数"
p line.index(line[x]) + 1
p "空白"
p line[x] - (line.index(line[x]) + 1)
