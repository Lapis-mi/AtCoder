# 整数の入力
a = gets.to_i

# スペース区切りの整数の入力
b, c = gets.chomp.split(" ").map(&:to_i)

# 文字列の入力
s = gets.chomp

# 配列として取得
arr = gets.split(" ")

# n回インプット
arr = []
(0..(n - 1)).each do |l|
  arr[l] = gets.split(" ")
end

# 出力
puts("#{a + b + c} #{s}\n")
