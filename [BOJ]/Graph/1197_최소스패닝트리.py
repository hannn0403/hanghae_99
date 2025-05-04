import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(a):
    if a == union_find[a]:
        return a

    else:
        union_find[a] = find(union_find[a])
        return union_find[a]


def union(a, b, c, spanning):
    real_a = find(a)
    real_b = find(b)
    # 만약 두개가 같은 집합에 속한다면 union을 하게 되면 사이클 발생
    if real_a != real_b:
        # 해당 값을 union한다면 spanning에 해당 edge 값 추가
        union_find[real_b] = union_find[real_a]
        spanning += c
    return spanning


V, E = map(int, input().split())

edge_list = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edge_list.append((c, a, b))

# print(f"정렬 전 : {edge_list}")
edge_list.sort()
# print(f"정렬 후 : {edge_list}")


spanning = 0
union_find = [i for i in range(V + 1)]

for i in range(E):
    c, a, b = edge_list[i]
    spanning = union(a, b, c, spanning)

print(spanning)
