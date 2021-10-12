#5Jewels and Stones
def numJewelsInStones(J, S):
      jewels = {}
      for i in J:
         jewels[i] = 1
      number = 0
      for i in S:
         if i in jewels:
            number+=1
      return number

print(numJewelsInStones("aZc", "catTableZebraPicnic"))
