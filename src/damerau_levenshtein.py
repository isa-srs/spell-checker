def damerau_levenshtein(s1, s2):
    """Finds the distance between two strings.

    Args:
        s1: String input from user
        s2: String from trie
    """
    l1, l2 = len(s1), len(s2)


    d = [[0 for j in range(l2+1)] for i in range(l1+1)]

    for i in range(l1+1):
        d[i][0] = i
    for j in range(l2+1):
        d[0][j] = j

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            d[i][j] = min(d[i][j-1]+1,      # kirjaimen poisto
                          d[i-1][j]+1,      # kirjaimen lisäys
                          d[i-1][j-1]+cost) # kirjaimen vaihto

            if s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                d[i][j] = min(d[i][j], d[i-2][j-2]+cost)    # transpoosi / kahden vierekkäisen kirjaimen vaihto
    
    return d[l1][l2]

