m = int(input())
s = set()

for _ in range(m):
    action = input().split()
    if action[0] == "add":
        s.add(int(action[1]))
    elif action[0] == "remove":
        if int(action[1]) in s:
            s.remove(int(action[1]))
    elif action[0] == "check":
        if int(action[1]) in s:
            print(1)
        else:
            print(0)
    elif action[0] == "toggle":
        if int(action[1]) in s:
            s.remove(int(action[1]))
        else:
            s.add(int(action[1]))
    elif action[0] == "all":
        s = set(range(1, 21))
    else:
        s = set()
