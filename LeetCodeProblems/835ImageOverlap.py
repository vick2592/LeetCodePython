import copy

#Video Guide to problem
#https://www.youtube.com/watch?v=zfjBapE3Y6E

class Solution:
    def largestOverlap(img1, img2):
        crs = Solution()
        #rowSize = len(img1)
        #colSize = len(img1[0])

        #Test countIdenticalOnes Method
        #count = crs.countIdenticalOnes(img1, img2, rowSize, colSize)

        #Test all shift methods.
        #tempImg1 = crs.shiftRight(img1, rowSize, colSize)
        #print("Shift Right: ", tempImg1)
        #tempImg2 = crs.shiftLeft(img1, rowSize, colSize)
        #print("Shift Left: ", tempImg2)
        #tempImg3 = crs.shiftUp(img1, rowSize, colSize)
        #print("Shift Up: ", tempImg3)
        #tempImg4 = crs.shiftDown(img1, rowSize, colSize)
        #print("Shift Down: ", tempImg4)


        return max(crs.shift_count(img1, img2), crs.shift_count(img2,img1))

    def shift_count(self, img1, img2):
        n, count = len(img1), 0
        for x in range(n):
            for y in range(n):
                temp = 0
                for i in range(y,n):
                    for j in range(x,n):
                        if(img1[x][y] == 1 and img2[i-y][j-x] == 1):
                            temp+=1
                count = max(count, temp)
        
        return count

    #Count the number of positions with one in both images
    #def countIdenticalOnes(self, img1, img2, rowSize, colSize):
    #    count = 0
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if (img1[i][j] == 1 and img2[i][j] == 1):
    #                count += 1

    #    return count

    #Check to see if shifting removed all ones from image
    #def noOnesLeft(self, img1, rowSize, colSize):
    #    onesLeft = False
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if(img1[i][j] == 1):
    #                onesLeft = True

    #    return onesLeft

    #def shiftRight(self, img, rowSize, colSize):
    #    copyImg = copy.deepcopy(img)
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if (j+1 == colSize):
    #                copyImg[i].pop()
    #            #temp = img[i][j]
    #            if(j == 0):
    #                copyImg[i].insert(j,0)
    #                continue

    #    return copyImg

    #def shiftLeft(self, img, rowSize, colSize):
    #    #Note you need to use deepcopy as a shallow copy references the same elements into the list. deepcopy or a recursive copy fixes the issue
    #    #where after running one shift the elements at each position stay fixed to a value.
    #    #Recursive solution
    #    #copyImg = []
    #    #for i in range(rowSize):
    #    #    copyImg.append([img[i][j] for j in range(colSize)])
    #    copyImg = copy.deepcopy(img)
    #    #print("Current image is: ", img)
    #    #print("The Value for image at pos 0,1 is: ", img[0][1])
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if (j+1 == colSize):
    #                copyImg[i].insert(j,0)
    #            if(j==0):
    #                copyImg[i].pop(j)

    #    return copyImg

    #def shiftUp(self, img, rowSize, colSize):
    #    copyImg = copy.deepcopy(img)
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if(i == 0):
    #                copyImg.pop(i)
    #                break
    #            if (i+1 == rowSize):
    #                copyImg.insert(i,colSize * [0])
    #                break

    #    return copyImg

    #def shiftDown(self, img, rowSize, colSize):
    #    copyImg = copy.deepcopy(img)
    #    for i in range(0, rowSize):
    #        for j in range(0, colSize):
    #            if (i+1 == rowSize):
    #                copyImg.pop(i)
    #                break
    #            if (i == 0):
    #                copyImg.insert(i, colSize * [0])
    #                break


    #    return copyImg

#img1test = [[0,1], [1,0]]
#print("Image 1 Test: ", img1test)
#img2test = [[1,1],[0,0]]
#answerTest = Solution.largestOverlap(img1test, img2test)
#print(answerTest)
img1 = [[1,1,0],[0,1,0],[0,1,0]]
print("Image 1: ", img1)
img2 = [[0,0,0],[0,1,1],[0,0,1]]

answer = Solution.largestOverlap(img1, img2)
#answer = Solution()
#answer.largestOverlap(img1, img2)
print(answer)