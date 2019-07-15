# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for x in range(0, N):
    s = input()
    t = []
    y = []

    for i in range(len(s)):
        if i % 2 == 0:
            t.append(s[i])

    for j in range(len(s)):
        if j % 2 != 0:
            y.append(s[j])


    print(''.join(t) + ' ' + ''.join(y))
