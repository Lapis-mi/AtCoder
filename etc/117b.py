def polygon():
    n = int(input())
    l = list(map(int, raw_input().split()))
    newlist = sorted(l, reverse=True)
    answer = "No"
    print(sum(newlist[0:(n-1)]))
    # if newlist[0] < sum(newlist[1:(n-1)]):
    #     answer = "Yes"
    # print(answer)

polygon()