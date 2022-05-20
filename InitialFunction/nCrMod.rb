def COMinit()
  max = 510000,
  mod = 10 ** 9 + 7
  fac = []
  finv = []
  inv = []

  fac[0] = fac[1] = 1
  finv[0] = finv[1] = 1
  inv[1] = 1
  i = 2
  while i <
        fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod / i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod
    i += 1
  end
  puts "a"
end

COMinit()
