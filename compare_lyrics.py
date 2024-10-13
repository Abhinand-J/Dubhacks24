# Returns a boolean array of the indices you need to change in s1 in order to reach s2. 
def edit_dist_dp(s1, s2):
    if (s2 == ""):
        allFail = [False] * (len(s1))
        return allFail, len(s1)
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the known entries in dp[][]
    # If one string is empty, then answer 
    # is length of the other string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the rest of dp[][]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], min(dp[i - 1][j], dp[i - 1][j - 1]))

    indices = [False] * (m + 1)
    i = m
    j = n
    while i >= 1 and j >= 1:
        if s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] == dp[i][j] - 1:
                indices[i - 1] = True
                i -= 1
            elif dp[i][j - 1] == dp[i][j] - 1:
                indices[i] = True
                j -= 1
            else:
                indices[i - 1] = True
                i -= 1
                j -= 1
    if s1[0] != s2[0]:
        indices[0] = True
    if indices[m] == True:
        indices[m - 1] = True
    indices.pop()
    return indices, dp[m][n]
