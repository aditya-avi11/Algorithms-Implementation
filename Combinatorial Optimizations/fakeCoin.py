def find_fake_coin(coins, start, end):
    # Base case: if there is only one coin left, it must be the fake one
    if end - start == 1:
        return start
    
    # Divide coins into three groups
    third = (end - start) // 3
    group1 = coins[start:start + third]
    group2 = coins[start + third:start + 2 * third]
    group3 = coins[start + 2 * third:end]
    
    # Weigh group1 against group2
    if sum(group1) < sum(group2):
        # Fake coin is in group1
        return find_fake_coin(coins, start, start + third)
    elif sum(group1) > sum(group2):
        # Fake coin is in group2
        return find_fake_coin(coins, start + third, start + 2 * third)
    else:
        # Fake coin is in group3
        return find_fake_coin(coins, start + 2 * third, end)

# Example usage:
# Define coins with one fake coin. Here, coins[3] is fake and lighter (weight 0)
coins = [1, 1, 1, 0, 1, 1, 1, 1, 1]
fake_index = find_fake_coin(coins, 0, len(coins))
print(f"The fake coin is at index {fake_index}")
