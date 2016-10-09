def way_1(n):
    """
    This approach has a problem: it builds up a call stack of size
    O(n), which makes our total memory costO(n). This makes it vulnerable
    to a stack overflow error, where the call stack gets too big and runs out of space.
    """
    # we assume n >= 1
    print n * way_1(n - 1) \
        if n > 1 \
        else 1


def way_2(n):
    """
    This approach uses
    O(1) space O(n) time).
    """
    # we assume n >= 1

    result = 1
    for num in range(1, n+1):
        result *= num

    print result


way_2(10)