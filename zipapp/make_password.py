# SPDX-License-Identifier: 0BSD
"""Make a password."""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from secrets import SystemRandom
from get_wordlist import get_wordlist

def make_password(
    length: int = 40,
    make_passphrase: bool = False,
    no_punctuation: bool = False,
    custom_chars: str = "",
    separator: str = "."
) -> str:
    system_random = SystemRandom()
    if make_passphrase:
        wordlist = get_wordlist()
        raw_password = system_random.choices(wordlist, k=length)
    else:
        charsets = (
            "" if no_punctuation else punctuation,
            custom_chars if custom_chars else "",
            ascii_lowercase, ascii_uppercase, digits
        )
        required_chars = [
            system_random.choice(charset) for charset in charsets if charset
        ]
        charsets_count = sum(1 if charset else 0 for charset in charsets)
        extra_length = length - charsets_count
        charset = "".join(charsets)
        random_chars = system_random.choices(charset, k=extra_length)
        raw_password = required_chars + random_chars
        system_random.shuffle(raw_password)
        separator = ""
    password = separator.join(raw_password)
    return password
