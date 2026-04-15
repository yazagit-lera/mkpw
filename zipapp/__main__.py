#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""A password generator."""

from argparse import ArgumentParser
from make_password import make_password

def main() -> None:
    make_passphrase_help = "Make a passpharse"
    no_punctuation_help = "Do not use the default punctuation charset"
    custom_chars_help = "Add the custom chars"
    length_help = "Set the password length"
    epilog = (
        "https://cheatsheetseries.owasp.org/cheatsheets"
        "/Authentication_Cheat_Sheet.html"
    )
    parser = ArgumentParser(
        description="Make a password", epilog=epilog)
    parser.add_argument(
        "-d", "--no_punctuation", action="store_true",
        help=no_punctuation_help)
    parser.add_argument("-o", "--custom_chars", help=custom_chars_help)
    parser.add_argument(
        "-w", "--make_passphrase", action="store_true",
        help=make_passphrase_help)
    parser.add_argument("-n", "--length", type=int, help=length_help)
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode")
    args = parser.parse_args()

    if args.interactive:
        make_passphrase = input(make_passphrase_help + " (y/n) ") == "y"
        if make_passphrase:
            no_punctuation = False
            custom_chars = ""
        else:
            no_punctuation = input(no_punctuation_help + " (y/n) ") == "y"
            custom_chars = input(custom_chars_help + " (optional) ")
        length = int(input(length_help + " "))
    else:
        make_passphrase = args.make_passphrase
        no_punctuation = args.no_punctuation
        custom_chars = args.custom_chars
        length = args.length
    if not length:
        length = 14 if make_passphrase else 40
    elif length < 4:
        parser.error("Too short length")
    password = make_password(
        length, make_passphrase, no_punctuation, custom_chars)
    print(password)

if __name__ == "__main__":
    main()
