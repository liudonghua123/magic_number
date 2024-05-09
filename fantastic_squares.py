#!/usr/bin/env python3


def format_radix(number, r=10):
    """
    Convert  number number to any radix formatted number string
    number: int - the number to be converted
    radix: int - the radix to be converted to, between 2 and 36, default to 10

    reference:
    1. https://github.com/Dartt0n/radix_string_python/blob/master/radix_string/__init__.py
    2. https://codegolf.stackexchange.com/questions/536/integer-to-string-with-given-radix
    """
    import string

    result = ""
    basic_alphabet = string.digits + string.ascii_lowercase
    while number:
        number, rdigit = divmod(number, radix)
        result = basic_alphabet[rdigit] + result
    return result or "0"


def solve(bit=2, radix=10):
    """
    Find bit-with number which the squrare of it is a revserse result of the reverse original number
    """
    solutions = []
    for number in range(radix ** (bit - 1), radix**bit):
        square = number**2
        reversed_square = int(format_radix(number, radix)[::-1], radix) ** 2
        if format_radix(square, radix) == format_radix(reversed_square, radix)[::-1]:
            solutions.append(number)
    return solutions


def process_results(bit, radix, solutions):
    print(
        f"For bit {bit} radix {radix} numbers, found {len(solutions)} solutions: {[format_radix(solution, radix) for solution in solutions]} or {solutions} in decimal number format, for example: {format_radix(solutions[0], radix)}**2={format_radix(solutions[0]**2, radix)}, and {format_radix(solutions[0], radix)[::-1]}**2={format_radix(int(format_radix(solutions[0], radix)[::-1], radix)**2, radix)} in {radix}-radix number format"
    )


if __name__ == "__main__":
    print("processing ...")

    radix = 8
    bit_start, bit_end = 2, 5
    print(
        f"\nTry to solve bit width {bit_start}-{bit_end} for radix {radix} fantastic squares"
    )
    for bit in range(bit_start, bit_end):
        solutions = solve(bit, radix)
        if solutions:
            process_results(bit, radix, solutions)

    radix = 10
    bit_start, bit_end = 2, 5
    print(
        f"\nTry to solve bit width {bit_start}-{bit_end} for radix {radix} fantastic squares"
    )
    for bit in range(bit_start, bit_end):
        solutions = solve(bit, radix)
        if solutions:
            process_results(bit, radix, solutions)

    radix = 16
    bit_start, bit_end = 2, 5
    print(
        f"\nTry to solve bit width {bit_start}-{bit_end} for radix {radix} fantastic squares"
    )
    for bit in range(bit_start, bit_end):
        solutions = solve(bit, radix)
        if solutions:
            process_results(bit, radix, solutions)
