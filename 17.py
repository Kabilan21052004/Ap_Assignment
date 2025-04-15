def list_fn(li):
    if len(li) >= 4:
        print(f"The fourth element {li[3]}")
    else:
        print("Element not available")
    if li[2:]:
        print(li[2:])
    else:
        print("[]")
    print(li[::-1])
    maxi = 0
    mini = float("inf")
    sums = 0
    for terms in li:
        sums += terms
        if terms > maxi:
            maxi = terms
        if terms < mini:
            mini = terms
    print(f"Minimum element is {mini}")
    print(f"Maximum element is {maxi}")
    print(f"Sum of element {sums}")
    if 0 in li:
        print(f"Index of zero is {li.index(0)}")
    else:
        print(-1)
    print(f"Sorted list in ascending order {sorted(li)}")
    print(f"Sorted list in descending order {sorted(li,reverse=True)}")

list_fn([1,8,4,7,3,0,2,6,7])