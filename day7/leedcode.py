def minDistance(s, t):
    m = len(s)
    n = len(t)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters are same
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # Insert, Delete, Replace
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],     # Insert
                    dp[i - 1][j],     # Delete
                    dp[i - 1][j - 1]  # Replace
                )

    return dp[m][n]


# Input
s = input("Enter first string: ")
t = input("Enter second string: ")

# Output
print("Minimum operations:", minDistance(s, t))
