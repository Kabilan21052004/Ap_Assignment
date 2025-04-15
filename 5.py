class InvalidShiftException(Exception):
    pass

def shift(s, count=0, acount=0):
    if count < 0 or acount < 0:
        raise InvalidShiftException("Shift values must be non-negative integers.")

    length = 0
    for _ in s:
        length += 1

    acount = acount % length if length != 0 else 0
    count = count % length if length != 0 else 0

    left_shifted = ""
    for i in range(acount, length):
        left_shifted += s[i]
    for i in range(0, acount):
        left_shifted += s[i]

    right_shifted = ""
    for i in range(length - count, length):
        right_shifted += left_shifted[i]
    for i in range(0, length - count):
        right_shifted += left_shifted[i]

    return right_shifted

print(shift("NinjaHattori"))
print(shift("NinjaHattori", acount=3))
print(shift("NinjaHattori", count=3))
print(shift("NinjaHattori", count=3, acount=3))
print(shift("NinjaHattori", count=6, acount=3))
print(shift("NinjaHattori", count=3, acount=6))
