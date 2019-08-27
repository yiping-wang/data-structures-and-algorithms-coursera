# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(char=next, position=i)
            opening_brackets_stack.append(bracket)

        if next in ")]}":
            last_bracket = opening_brackets_stack[-1] if len(
                opening_brackets_stack) > 0 else None
            if ((last_bracket is None) or
                (next == ')' and last_bracket.char in "[{") or
                (next == ']' and last_bracket.char in "({") or
                (next == '}' and last_bracket.char in "[(")):
                return i + 1
            else:
                del opening_brackets_stack[-1]

    return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
