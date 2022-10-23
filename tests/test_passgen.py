import string
import unittest

import wolfram_vault


class TestPassGen(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_random_password(self):
        test_pass = wolfram_vault.random_password(length=20)
        self.assertTrue(test_pass)
        self.assertEqual(len(test_pass), 20)

        ntest_pass = wolfram_vault.random_password(uppercase=False, punctuation=False)
        self.assertFalse(
            any(
                True
                for char in ntest_pass
                if char in string.ascii_uppercase + string.punctuation
            )
        )


if __name__ == "__main__":
    unittest.main()
