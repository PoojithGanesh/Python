#Find whether given sequence is additive sequence or not
def is_additive_sequence(seq):
    for i in range(len(seq) - 2):
        if seq[i] + seq[i+1] != seq[i+2]:
            return False
    return True

seq = [1, 2, 3, 5, 8, 13]
print(is_additive_sequence(seq))  
