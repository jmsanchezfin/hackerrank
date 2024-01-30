# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input()) #number of test cases
S = []
even = []
odd = []

while T > 0:
    word = input()
    S.append(word)
    T -= 1

for item in S:
    to_array = list(item)    
    for index, obj in enumerate(to_array):
        if index % 2 == 0:
            even.append(obj)
        else:
            odd.append(obj)

    print("".join(even), "".join(odd))
    even.clear()
    odd.clear()

"""""

to_array = list(S)

for index, obj in enumerate(to_array):
    if index % 2 == 0:
        even.append(obj)
    else:
        odd.append(obj)

print("".join(even), "".join(odd))
"""