def count_infection_sequences(n, sick):
    MOD = 10**9 + 7

    # Calculate the size of each segment of healthy children
    segments = []
    start = 0
    for i in sick:
        segments.append(i - start)
        start = i + 1
    segments.append(n - start)  # Add the last segment

    # Calculate factorials preemptively to avoid repetition within the loop
    fact = [1] * (n + 1) 
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    total_ways = 1
    for segment_size in segments:
        # Number of ways within a segment: 2^(segment_size - 1)
        ways_in_segment = pow(2, segment_size - 1, MOD) 

        # Multiply by the number of ways we can arrange the segment, accounting for duplicates
        total_ways = (total_ways * ways_in_segment * fact[segment_size]) % MOD

    return total_ways
