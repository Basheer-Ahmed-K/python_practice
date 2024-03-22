def merge_the_tools(string, k):
    ans = ''
    for i in range(0, len(string), k):
        substring = string[i: i + k]
        lst = list()
        for char in substring:
            if char not in lst:
                lst.append(char)
        for i in lst:
            ans += i
        ans += '\n'
    print(ans)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
