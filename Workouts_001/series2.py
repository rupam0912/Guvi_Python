n = int(input("Enter the range: "))

temp = []
temp.append(6)
for i in range(1,n):
    temp.append(temp[i-1]+4)

res = []
res.append(3)

for i in range(1,n):
    res.append((temp[i-1]+res[i-1]))

ans = []
for i in res:
    ans.append(i*2)

print(ans)