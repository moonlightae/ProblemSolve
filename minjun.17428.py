while True:
    def sex(n, k):
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(n + 1):
            for j in range(n + 1):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0 and j > i:
                    dp[i][j] += dp[i][j - 1]

        def ksex(dhls, ekedhls, k):
            if dhls == 0 and ekedhls == 0:
                return ""
            if dhls > 0:
                cntdhls = dp[dhls - 1][ekedhls]
                if k < cntdhls:
                    return '(' + ksex(dhls - 1, ekedhls, k)
                k -= cntdhls
            if ekedhls > 0 and ekedhls > dhls:
                return ')' + ksex(dhls, ekedhls - 1, k)
            return ""

        if dp[n // 2][n // 2] <= k:
            return "-1"

        return ksex(n // 2, n // 2, k)


    n, k = map(int, input().split())
    print(sex(n, k))
