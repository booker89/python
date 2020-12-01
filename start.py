# 第一隻程式
print("hello python 2")
{1,2,3}
x=3
print(x)
# True t一定要大寫
x=True
print(x)
x={3,5,6}
print(x)

# -----------
# 小數除法
y=3/6
print(y)
#整數除法(小數的部分不看)
z=3//6
print(z)

#次方表達用兩個**
x=2**3
print(x)
# 開根號的話就用0.5
x=2**0.5
print(x)
# 取餘數
x=7%3
print(x)

#字串運算
# 在雙引號前面打\代表跳脫
s="hello\"k"
print(s)

# 字串的串接可以用+或用空白鍵
s="hello" "world"
print(s)

# 寫多行文字用\n或是用三個雙引號、三個單引號
s="hello\nworld"
print(s)
s="""hello
hi

world"""
print(s)

# 用乘法可以把文字重複
s="Hello"*3+"world"
print(s)

# 字串會對內部的字元編號(索引)，從0開始算起
# 開頭:結尾(取到的數字包含開頭，不包含結尾)
s="hello"
print(s[0:3])
