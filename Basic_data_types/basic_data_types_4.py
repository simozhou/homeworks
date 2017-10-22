if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m = max(arr)
    print max(takewhile(lambda x: x < m, sorted(arr)))