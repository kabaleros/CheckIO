# Try to find out how many zeros a given number has at the end.
#
# Input: A positive Int
#
# Output: An Int.
#
# Example:
#
# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0
# def end_zeros(num: int) -> int:
#     num = list(str(num))
#     sum_zeros = 0
#     for zero in reversed(num):
#         if zero != '0':
#             break
#         else:
#             sum_zeros +=1
#     return sum_zeros
def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")