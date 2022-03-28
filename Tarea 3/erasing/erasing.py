from sys import stdin
maxn = 100000+5
s = [0 for _ in range(maxn)]
f = [0 for _ in range(maxn)]


def solve(N, D):
    for i in range(N+1):
        c = stdin.readline().strip()
        s[i] = c
    dex = 2; size = N - D; ndex = 1
    f[1] = s[1]
    while dex <= N and D > 0:
        while ndex > 0 and s[dex] > f[ndex] and D > 0:
            D -= 1
            ndex -= 1
        ndex += 1
        f[ndex] = s[dex]
        dex += 1
    for i in range(min(size, ndex)+1):
        print("%s" % f[i])
    size-= ndex
    for i in range(size):
        print("%s" % s[dex])
        dex += 1
    print("\n")

def main():
    line = stdin.readline().split()
    N = int(line[0]); D = int(line[1])
    while N!=0 and D!=0:
        print("N and D: ", N,D)
        solve(N, D)
        line = stdin.readline().split()
        print("second line: ", line)
        N = int(line[0]); D = int(line[1])

main()