#print("Hello World")

#loops
for i in range(0,10):
    print(i)
"""
while i < 10:
    print("Greater than 10")

"""
#Linear search
arr = []
for i in range(0,25,2):
    arr.append(i)

for i in arr:
    print(i)

search = 16
for i in arr:
    if arr[i] == search:
        print("Match Found")
    else:
        print("Match not found")
