class LengthMismatchException(Exception):
    pass

def weave(l1, l2):
    try:
        if len(l1) != len(l2):
            raise LengthMismatchException("The lengths of the lists do not match.")
        return l1 + l2
    except LengthMismatchException as e:
        print("Caught an exception:", e)
ans = weave([1, 2], [3,4])  
print(ans)