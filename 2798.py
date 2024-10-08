N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(N - 2):  # 브루트포스 알고리즘
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= M:
                result = max(result, current_sum)

print(result)

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# result = []

# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             current_sum = cards[i] + cards[j] + cards[k]
#             if current_sum <= M:
#                 result.append(current_sum)

# print(max(result))
