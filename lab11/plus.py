import json
#測試呈重, 體重的list, 限制次數
def check(mid, lst, turn):
    #承重
    x = 0
    #次數
    time = 1
    for i in range(len(lst)):
        #如果承重超過測試承重，則將這個x變為現在這個人的體重
        if (x+lst[i]) >= mid:
            x = lst[i]
            #次數加一
            time +=1
            #如果次數超過限制次數則回傳false
            if time > turn:
                return False
        #如果沒有超過承重則加入這個人的體重
        else:
            x +=lst[i]
    return True

with open('input_plus.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input
        a = input[0]
        b = input[1]
        #最大承重
        right = 50000
        #最小呈重
        left = 1
        #如果最大承重>最小呈重
        while left<= right:
            mid = int((left+right)/2)
            #當可以符合此測試呈重時，則將最大承重改為mid-1
            if check(mid, a, b):
                right = mid-1
            #不符合則將最小呈重改為mid+1
            else:
                left = mid+1
        print('Question: ' + str(key))
        print('Assignment:', str(left-1))
        print()
