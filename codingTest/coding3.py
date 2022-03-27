candles = [4,5,2]

day = 0
result = 0
finish= True

while finish:

    day+=1
    candles.sort(reverse=True)
    if day > len(candles):
        break
    for d in range(day):
        

        if candles[d] >= 1:
            candles[d]-=1
        else:
            finish =False
            break
        print(candles)

    if finish:    
        result+=1
    print("")

print(result)
    

