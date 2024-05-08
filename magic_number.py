#!/usr/bin/env python3


def solve(total=77, start=1, end=10):
    """
    Find three numbers from start (inclusive) to end (exclusive) which the sum of it's square is equal to total.

    Using the exhaustion method
    """
    from itertools import combinations

    solutions = []
    for a, b, c in combinations(range(start, end), 3):
        if a**2 + b**2 + c**2 == total:
            solutions.append([a, b, c])
    return solutions


def process_solutions(solutions, bit, total):
    """
    Process the solutions for magic number
    """
    # sort the first solution asendingly, the second solution descendingly
    solutions[0].sort(key=lambda x: x)
    solutions[1].sort(key=lambda x: x, reverse=True)
    print(f"For total {total}, found {len(solutions)} solutions: {solutions}")
    # print the result
    power = 10**bit
    solution_numbers1 = [
        solutions[0][0] * power + solutions[1][0],
        solutions[0][1] * power + solutions[1][1],
        solutions[0][2] * power + solutions[1][2],
    ]
    solution_numbers2 = [
        solutions[1][0] * power + solutions[0][0],
        solutions[1][1] * power + solutions[0][1],
        solutions[1][2] * power + solutions[0][2],
    ]
    print(
        f"For example, {solution_numbers1[0]}**2+{solution_numbers1[1]}**2+{solution_numbers1[2]}**2={solution_numbers1[0]**2+solution_numbers1[1]**2+solution_numbers1[2]**2}, and {solution_numbers2[0]}**2+{solution_numbers2[1]}**2+{solution_numbers2[2]}**2={solution_numbers2[0]**2+solution_numbers2[1]**2+solution_numbers2[2]**2}\n"
    )


if __name__ == "__main__":
    # solve one-bit magic number
    bit = 1
    print("try to solve one-bit magic number")
    for total in range(1**2 + 2**2 + 3**2, 7**2 + 8**2 + 9**2):
        solutions = solve(total=total)
        if len(solutions) >= 2:
            process_solutions(solutions, bit, total)

    bit = 2
    print("try to solve two-bit magic number")
    for total in range(10**2 + 11**2 + 12**2, 97**2 + 98**2 + 99**2):
        solutions = solve(total=total, start=10, end=100)
        if len(solutions) >= 2:
            process_solutions(solutions, bit, total)

    print("try to solve three-bit magic number ...")
