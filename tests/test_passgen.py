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

    def test_random_passphrase(self):
        test_phrase = wolfram_vault.random_passphrase()
        for words in test_phrase:
            self.assertGreaterEqual(len(words), 4)
            self.assertTrue(words.isalnum())

    def test_random_username(self):
        test_username = wolfram_vault.random_username()
        self.assertTrue(test_username.isalnum())


if __name__ == "__main__":
    unittest.main()
