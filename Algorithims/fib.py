def fib(limit):
    seed = [1, 2]
    sum = 0
    current = 0
    if limit > 1:
        for i in range(limit):
            current = seed[-1] + seed[-2]
            print(current)
            seed.append(current)
            if current % 2 == 0:
                sum += current
            del seed[0]
            if current > limit:
                break
        print("sum of even numbers: %i" % sum)
        print(seed)
    else:
        print("ERROR, USAGE: LIMIT MUST BE GREATER THAN 1")


if __name__ == "__main__":    
    fib(4000000)