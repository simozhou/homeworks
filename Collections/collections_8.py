import sys
from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    cnt = Counter(s)
    m_c = cnt.most_common()
    for i in sorted(m_c, key = lambda x: (-x[1], x[0]))[:3]:
        print(*i, sep = ' ')