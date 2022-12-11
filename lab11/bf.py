import json

# (遞迴實現)
def Perm(arrs): 
    # 若輸入 [1,2,3]，則先取出1，將剩餘的 [2,3]全排列得到 [[2,3],[3,2]]，
    #               再將 1加到全排列 [[2,3],[3,2]]上變成 [[1,2,3],[1,3,2]]
    # 同理，取出2或者3時，得到的分別是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
    if len(arrs)==1:
        return [arrs]
    result = []  # 最終的結果（即全排列的各種情況）
    for i in range(len(arrs)):  
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i個元素後剩餘的元素
        rest_lists = Perm(rest_arrs)   # 剩餘的元素完成全排列
        lists = []
        for term in rest_lists:
            lists.append(arrs[i:i+1]+term)  # 將取出的第 i個元素加到剩餘全排列的前面
        result += lists
    return result
    

def BF(input, lst):
    N = len(input)
    #設一個紀錄所有cost的list
    allcost = []
    #n為第n個在list裏頭的排列方式
    for n in range(len(lst)):
        #設定一個變數為0，之後好作加減
        x = 0
        for j in range(N):
            #a 為第n個排列的list
            a = lst[n]
            #加上input中第j列第n個lst中的第j個的行
            x += input[j][a[j]]
        #將加總的x放入allcost中
        allcost.append(x)

    #找到最小的cost   
    cost = min(allcost)
    #透過找到cost在第幾個allcost裏頭來找他是所有排列中的第幾個list
    assignment = lst[allcost.index(cost)]

    return assignment, cost

# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # show input data and number of the Tasks
        print(input)
        array = []
        for i in range(len(input)):
            array.append(i)
        a = Perm(array)
        # Brute Force Algorithm
        #將所有排列得到的list和input傳進BF
        assignment, cost = BF(input, a)


        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()
