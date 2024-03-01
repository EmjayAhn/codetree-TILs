import sys

for _ in range(4):
    input_list = list(map(int, sys.stdin.readline().split()))
    print(sum(input_list))