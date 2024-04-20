from itertools import permutations
def late_clock(a, b, c ,d):
    res = sorted([''.join([str(i) for i in x]) for x in permutations([a, b, c, d], 4)\
    if x[0]*10+x[1]<24 and x[2]*10+x[3]<60], reverse= True)[0]
    return f'{res[:2]}:{res[2:]}'
