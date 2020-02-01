n = int(input())
ls = list(range(1,n+1))

even_ls = [i for i in ls if i%2 == 0]
for i in range(len(even_ls)):
    print(even_ls[i]),

odd_ls = [i for i in ls if i%2!==0]
even_sq = [i**2 for i in ls if i%2 == 0 ]
odd_sq = [i**2 for i in ls if i%2!=0]

special_list = [i**2 if i%2==0 else i for i in ls]
