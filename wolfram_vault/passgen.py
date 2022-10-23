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

    password = "".join(secrets.choice(character_set) for i in range(length))

    return password


def random_passphrase():
    pass
