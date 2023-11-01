class Solution:
    def displayTable(orders):
        orderTable = []
        orderTable.append(["Table","Beef Burrito","Ceviche","Fried Chicken","Water"])
        tableDict = {}
        for o in orders:
            tableDict.setdefault(o[1], {})

        for k,v in tableDict.items():
            v.setdefault("Beef Burrito", 0)
            v.setdefault("Ceviche", 0)
            v.setdefault("Fried Chicken", 0)
            v.setdefault("Water", 0)

        for itm in orders:
            tableDict[itm[1]][itm[2]] += 1

        #print(tableDict.items())
        sortList = []

        #As a fix you can make a new Enum list to keep track of all order titles when adding them into dictionary and using keys. For that loop over enumList
        for x, y in tableDict.items():
            tempList = []
            tempList.append(int(x))
            tempList.append(y["Beef Burrito"])
            tempList.append(y["Ceviche"])
            tempList.append(y["Fried Chicken"])
            tempList.append(y["Water"])
            sortList.append(tempList)

        sortList = sorted(sortList, key = lambda x: x[0])
        print(sortList)
        orderTable += sortList

        return orderTable

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
answer = Solution.displayTable(orders)
print(answer)