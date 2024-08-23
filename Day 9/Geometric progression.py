#Find whether given sequence is geometric progression or not.
def is_geometric_progression(seq):
    ratio = seq[1] / seq[0]
    for i in range(2, len(seq)):
        if seq[i] / seq[i-1] != ratio:
            return False
    return True

seq = [2, 6, 18, 54, 162]
print(is_geometric_progression(seq))  # Output: True
