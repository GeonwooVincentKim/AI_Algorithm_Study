n, m = map(int, input().split())
print(n, m)
#1
mylist = [0 for _ in range(n)]

for i in range(n):
    mylist[i] = list(map(int, input().split()))
    print(mylist[i])


# #2
# mylist = []
# for i in range(n):
#     mylist.append(list(map(int, input().split())))


# #3
# mylist = [list(map(int, input().split())) for _ in range(n)]
