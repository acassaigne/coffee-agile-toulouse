import unittest
from collections.abc import Callable


class Foo:

    def a_method(self) -> int:
        return 4

    def a_method_b(self, n : int) -> int:
        return 4 + n

def my_function(this_a_callable: Callable, p: int) -> int:
    return 10 + this_a_callable(p)


class MyTestCase(unittest.TestCase):

    def test_something(self):
        f = Foo()

        self.assertIsInstance(f, Foo)
        self.assertIsInstance(f.a_method(), int)
        self.assertEqual(4, f.a_method())

    def test_a_methode_b(self):
        f = Foo()

        self.assertEqual(4 + 2, f.a_method_b(2))

    def test__a_function_taking_a_method(self):

        f = Foo()
        result = my_function(this_a_callable=f.a_method_b, p=3)

        self.assertEqual(17, result)
