#8bag of tokens
def bagOfTokensScore(tokens, P):
    tokens.sort()
    result, points = 0, 0
    left, right = 0, len(tokens)-1
    while left <= right:
        if P >= tokens[left]:
            P -= tokens[left]
            left += 1
            points += 1
            result = max(result, points)
        elif points > 0:
            points -= 1
            P += tokens[right]
            right -= 1
        else:
            break
    return result

tokens = [100]
P = 50
print(bagOfTokensScore(tokens, P))

