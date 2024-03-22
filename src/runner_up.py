def runnerUp(n):
    n = list(n)
    n.sort()
    print(n[-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerUp(set(arr))