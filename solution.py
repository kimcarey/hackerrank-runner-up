if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    sorted_list = sorted(arr, reverse=True)
    runner_up = sorted_list[1]
    print(runner_up)