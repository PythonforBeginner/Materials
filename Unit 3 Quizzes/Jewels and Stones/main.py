def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    for i in jewels:
        count += stones.count(i)
    return count

if __name__ == '__main__':
    print(numJewelsInStones("aA", "aAAbbbb"))
    print(numJewelsInStones("z", "ZZ"))
