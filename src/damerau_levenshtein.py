def damerau_levenshtein(s1, s2):
    """Finds the distance between two strings.

    Args:
        s1: String input from user
        s2: String from trie
    """
    l1, l2 = len(s1), len(s2)


    distance = [[0 for j in range(l2+1)] for i in range(l1+1)]

    for i in range(l1+1):
        distance[i][0] = i
    for j in range(l2+1):
        distance[0][j] = j

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                distance[i][j] = distance[i-1][j-1]
            else:
                distance[i][j] = 1+min(distance[i-1][j], distance[i][j-1], distance[i-1][j-1])
    
    return distance[l1][l2]

