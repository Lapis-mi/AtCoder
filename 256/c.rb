def fillingArray()
  h1, h2, h3, w1, w2, w3 = gets.chomp.split(" ").map(&:to_i)
  if h1 + h2 + h3 != w1 + w2 + w3
    puts 0
  else
  end
  puts 28 ** 9
end

fillingArray()
