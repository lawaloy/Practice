from collections import deque
def shortestPath(source, target, words):

    if not source or not target or not words:
        return -1

    words_set = set(words)
    if target not in words_set:
        return -1

    word_char_set = set()
    for word in words:
        for char in word:
            word_char_set.add(char)

 
    count = 0
    queue = deque([(source, count)])
    while queue:
        curWord, count = queue.popleft()

        if curWord == target:
            return count
        for w in range(len(curWord)):
            for c in word_char_set:
                sec = curWord[:w] + c + curWord[w+1:]
                if sec in words_set:
                    
                    words_set.remove(sec)
                    queue.append((sec, count+1))

    return -1

print(shortestPath("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]))
