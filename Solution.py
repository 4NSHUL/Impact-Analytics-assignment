# This file contains the Solution and its explanation.

# 1. number of ways of attending classes without any restriction = 2^N (each day, you may be present or absent)

# 2. Let S(n) be the number of ways of attending classes by missing 4 consecutive days.
# then S(n) = 2^(n-4) + S(n-1) + S(n-2) + S(n-3) + S(n-4)
# Same concept as no N consecutive 1's in binary string is used here in order to form recurrence relation.

# Then the number of ways of attending classes without missing 4 consecutive days
# C(n) = 2^n - S(n)

# Now, the desired probability is
# S(n) / 2^n

def ways_to_miss_class(n):
    """
    This function is used to find the attendance using recurrence relation.
    """
    if n == 4:
        return 1
    attendance = [0,0,0,1]
    for i in range(4,n):
        attendance.append(2**(i-3)+attendance[i-1]+attendance[i-2]+attendance[i-3]+attendance[i-4])
    return attendance[-1]

def count_ways(n):
    """
    This function is used to count ways/valid ways/total ways
    """
    total_ways = 2**n
    misses= ways_to_miss_class(n)
    # answer of first question
    valid_ways = total_ways - misses
    # probability will be misses/total_ways
    probability = misses/total_ways
    final_answer = str(probability)+"/"+str(valid_ways)
    return final_answer

print(count_ways(10))

