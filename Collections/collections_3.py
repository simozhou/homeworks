from collections import namedtuple
n, Student = input(), namedtuple('Student', ','.join(raw_input().split()))
students_marks = map(lambda x: int(x.MARKS), [Student(*raw_input().split()) for _ in xrange(n)])
print sum(students_marks)/float(len(students_marks))
