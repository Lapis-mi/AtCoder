def knights()
  arr = gets.split(" ")
  x = arr[0].to_i
  y = arr[1].to_i
  if (x + y) % 3 == 0
    div = (x + y) / 3
    sa = x - div
    count = 0
    bunshi = 1
    bunbo = 1
    (1..div).each do |num|
      if count == sa
        break
        bunshi = bunshi % (10 ** 9 + 7)
      end
      bunshi *= div - num + 1
      bunbo *= num
      count += 1
      puts num
    end
    puts (bunshi / bunbo) % (10 ** 9 + 7)
  else
    puts 0
  end
end

knights()
