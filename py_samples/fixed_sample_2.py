from pympler import tracker


class A(object):
    def __init__(self, b_instance):
        self.b = b_instance


class B(object):
    def __init__(self):
        self.a = A(self)

    # def __del__(self):
    #     print "die"


def test():
    b = B()

    for x in xrange(10000):
        b = B()

tr = tracker.SummaryTracker()
test()
tr.print_diff()
