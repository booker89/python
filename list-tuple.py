# 有順序可變動列表list(用中括號)
grades=[12,60,15,50]
grades[0]=55 #把55放到列表中第一個位置，12會被取代
print(grades)

# 取得列表中特定資料
grades=[12,60,15,50,100]
print(grades[1:4])

#連續刪除從列表中編號1到4(不包含)的資料
grades=[12,60,15,50,100]
grades[1:4]=[]
print(grades)

#列表串接
grades=[12,60,15,50,100]
grades=grades+[110,120,130]
print(grades)

# 取得列表的長度，用len(列表資料)
grades=[12,60,15,50,100]
print(len(grades))

#巢壯列表及取代
data=[[1,2,3],[4,5,6]]
print(data[1][2])

data=[[1,2,3],[4,5,6]]
data[1][0:2]=[3,3,3]
print(data[1])


# 有順序不可變動列表tuple(用小括號)
data=(1,2,3,4,5,6)
print(data)
data[0]=5 #錯誤，因為tuple的資料不能變動
print(data)