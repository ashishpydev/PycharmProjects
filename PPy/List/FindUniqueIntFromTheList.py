from collections import Counter


def dev_find():
    m_list = [3, 5, 6, 7, 8, 77, 7, 3, 5, 6]
    c = Counter(m_list)
    print(c)
    dic = dict(c)
    distinct = []
    for key, val in dic.items():
        if val == 1:
            distinct.append(key)
    print(distinct)
    
dev_find()