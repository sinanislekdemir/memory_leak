from pympler import tracker


def f(a=None):
    if not a:
        a = []
    a.append('test' * 10)


def test():
    for x in xrange(100000):
        f()

track = tracker.SummaryTracker()
test()
track.print_diff()
