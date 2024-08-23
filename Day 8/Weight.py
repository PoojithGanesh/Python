'''You are given an set of items each item conists of weight & values v and you will be given a bag with capacity C. print the items which will gives you more profit when you fill the bag 
condition: You should exit the bag capacity, you can take or either leave the item'''
def knapsack(capacity, weights, values):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]

    return result

# test the function
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print("Items to take:", knapsack(capacity, weights, values))
