# my solution before conceptual overview
def nonConstructibleChange(coins):
    if len(coins) == 0 :
        return 1

    sortedCoin = sorted(coins)
    change = 0

    for i in range(len(sortedCoin)):
        if sortedCoin[i] > change + 1:
            return change + 1
        change+=sortedCoin[i]

    return change + 1

#tim ruscia solution
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    
    return currentChangeCreated + 1
