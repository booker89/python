#集合的運算
# 用in或not in判斷，回True或False
s1={1,2,3}
print(1 in s1)

# 交集&，取兩個集合中相同的資料
s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9}
s3=s1&s2
print(s3)

# 聯集|，取兩個集合中所有的資料，但不重複取
s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9}
s3=s1|s2
print(s3)

#差集-，從s1中減去和s2重疊的部分
s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9}
s3=s1-s2
print(s3)

# 反交集^，取兩個集合中，不重疊的部分
s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9}
s3=s1^s2
print(s3)

# 把字串中的字母拆解成集合：set(字串)
s=set("hello")
print("A" in s)


#字典的運算(key-value配對)