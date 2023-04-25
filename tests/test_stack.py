"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        self.stack = Stack()
        self.stack.push("data1")
        self.stack.push("data2")
        self.assertEqual(self.stack.top.data, "data2")
        self.assertEqual(self.stack.top.next_node.data, "data1")

    def test_pop(self):
        self.stack = Stack()
        self.assertIsNone(self.stack.pop())

        self.stack.push("data1")
        self.stack.push("data2")
        self.assertEqual(self.stack.pop(), "data2")
        self.assertEqual(self.stack.pop(), "data1")
        self.assertIsNone(self.stack.pop())

    def test_str(self):
        self.stack = Stack()
        self.assertEqual(str(self.stack), "")


if __name__ == '__main__':
    unittest.main()
