import secrets
import string


def random_password(length=10, **kwargs) -> str:
    """Random password generators with default options as,
    {
        lowercase = True,
        uppercase = True,
        digits = True,
        punctuation = False
    }

    The default options can be changed, for example
    >>> random_password(uppercase=False) # uppercase  removed from character pool
    >>> random_password(punctuation=True) # punctuation added to character pool

    Args:
        length (int, optional): Defaults to 10.

    Returns:
        str: random password with len 'length'
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    options = [
        (lowercase, kwargs.get("lowercase", True)),
        (uppercase, kwargs.get("uppercase", True)),
        (digits, kwargs.get("digits", True)),
        (punctuation, kwargs.get("punctuation", False)),
    ]

    character_set = "".join(characters[0] for characters in options if characters[1])

    return "".join(secrets.choice(character_set) for i in range(length))


def random_passphrase() -> list:
    """Random passphrase generator

    Returns:
        list: fixed length of 5
    """
    return [secrets.choice(_word_list()) for _ in range(5)]


def random_username() -> str:
    """Random username generator of format `<5-letter-word><4-digit-int>`"""
    return secrets.choice(_word_list(length=5)) + str(_randint(1000, 9999))


def _randint(a: int, b: int) -> int:
    """randint[a, b] function implemented using secrets module"""
    return secrets.choice(range(a, b + 1))


def _word_list(length=4) -> list:
    """Preferred word list taken from `/usr/share/dict/words`

    Args:
        length (int, optional): Length of each word. Defaults to 4.
    """
    try:
        with open("/usr/share/dict/words") as fileobj:
            words = []
            for word in fileobj:
                sword = word.strip()
                if len(sword) > length and sword.isalpha():
                    words.append(sword.lower())

            return words

    except FileNotFoundError:
        # TODO handle this exception
        return ["neurodendron", "shuha", "undervalues", "criminologic", "jemmying"]
