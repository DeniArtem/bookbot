def word_count(TEXT):
    count_word = TEXT.split()
    return len(count_word)

def characters(TEXT):
    COUNT = {}
    for char in TEXT:
        char = char.lower()
        if char in COUNT:
            COUNT[char] += 1
        else:
            COUNT[char] = 1
    return COUNT

def sort_on(a):
    return a["count"]

def sortlist(COUNT):
    listchar = []
    for key in COUNT:
        listchar.append({"char": key, "count": COUNT[key]})
    listchar.sort(reverse=True, key=sort_on)
    return listchar

