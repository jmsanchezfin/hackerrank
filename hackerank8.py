# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}
query = []
N = int(input())

while N > 0:
    key, value = input().split(' ')
    phoneBook[key] = value
    N -= 1

while True:
    try:
        name=input()
    except EOFError:
        break

    if name:
        query.append(name)
    else:
        break

for name in query:
    if phoneBook.get(name):
        print(name + '=' + phoneBook.get(name))
    else:
        print('No phone')