import unittest

def func(arr):
    first_positive = None
    second_positive = None
    summa = 0

    for i, num in enumerate(arr):
        if num > 0:
            if first_positive is None:
                first_positive = i
            elif second_positive is None:
                second_positive = i
                break

    if first_positive is not None and second_positive is not None:
        for num in arr[first_positive + 1:second_positive]:
            summa += num

    return summa

class test_func(unittest.TestCase):
    def test_no_second_positive(self):
        arr = [-1, 2, 3, -4, -5, -3, -6, -7]
        self.assertEqual(func(arr), 0)

    def test_no_positives(self):
        arr = [-1, -2, -3, -4, -5, -3, -6, -7]
        self.assertEqual(func(arr), 0)

    def test_single_positive(self):
        arr = [-1, -2, 3, -4, -5, -3, -6, -7]
        self.assertEqual(func(arr), 0)

    def test_empty_array(self):
        arr = []
        self.assertEqual(func(arr), 0)

if __name__ == '__main__':
    unittest.main()