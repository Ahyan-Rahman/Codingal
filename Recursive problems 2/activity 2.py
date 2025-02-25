def paren(s, l, r, p, n):
    if p == 2 * n:
        for ss in s:
            print(ss, end='')
        print("\n")
        return
    
    if l > n:

        s[p] = "("
        paren(s, l + 1, r, p+1, n)

    if r<l:
        s[p] = ")"
        paren(s, l, r +1, p+1, n)

n = int(input("Enter the number of parenthesis pairs: "))
s = [""] * (2 * n)
print("\n")
paren(s, 0, 0, 0, n)
