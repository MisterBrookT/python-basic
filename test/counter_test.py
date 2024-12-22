from advanced.utils import Counter

def test_counter():
    counter = Counter()
    assert next(counter) == 0
    assert next(counter) == 1
    assert next(counter) == 2
    counter.reset()
    assert next(counter) == 0
    assert next(counter) == 1
    assert next(counter) == 2
    assert next(counter) == 3
    assert next(counter) == 4
    assert next(counter) == 5
    counter.reset()
    assert next(counter) == 0
    assert next(counter) == 1
    assert next(counter) == 2
    assert next(counter) == 3
    assert next(counter) == 4
    assert next(counter) == 5

