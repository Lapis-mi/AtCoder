n = gets.to_i

puts (1 + n) * n / 2 -
       (3 + n - n % 3) * (n / 3) / 2 -
       (5 + n - n % 5) * (n / 5) / 2 +
       (15 + n - n % 15) * (n / 15) / 2