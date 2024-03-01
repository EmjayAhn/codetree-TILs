import sys

def make_upper(string):
    return string.upper()

for _ in range(5):
    input_array = list(map(make_upper, sys.stdin.readline().split()))
    for each_letter in input_array:
        print(each_letter, end=' ')
    print()