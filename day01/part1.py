# Day 1 - Part 1

def solution(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

        int_list = []

        for line in lines:
            full_int = ''.join(char for char in line if char.isdigit())
            int_list.append(int(full_int[0] + full_int[-1]))

        return sum(int_list)

file_path = './input.txt'

print(solution(file_path))