# 1. sort scores.csv in decreasing order by
# (a) value of the third column 
# (b) sum of column values. 

def loadCSV(path):
    # create an empty array to store the csv
    scores_ = []
    with open (path, "r") as file:
        count = -1
        for line in file: 
            count = count + 1
            linearray = line.split(",")
            # print(linearray)
            # if  on  second line  convert elements to int
            if count >= 1:
                for i in range(len(linearray)):
                    # print(int(linearray[i]))
                    linearray[i] =  int(linearray[i])

            scores_.append(linearray)
        # print(len(scores_))
    return scores_

def sortByThirdColumn(arr):
    result = sorted(arr,key = lambda x: x[2],reverse = True)
    return result
def sortBySum(arr):
    result = sorted(arr,key = lambda x: sum(x),reverse = True)
    return result

def save2dArray2File(arr,filename):
    with open(filename,mode='w',newline='') as file:
        for row in arr:
            line = ','.join(map(str,row))
            file.write(line + '\n')

scores = loadCSV("./scores.csv")
# print(scores[1:])
sortedbyThird = sortByThirdColumn(scores[1:])
sortedbySum = sortBySum(scores[1:])
# print(sortedArray)
save2dArray2File(sortedbyThird,'sortedByThirdCol.csv')
save2dArray2File(sortedbySum,'sortedBysum.csv')




