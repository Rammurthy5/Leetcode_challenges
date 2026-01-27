def find_element_pascaltriangle(n, r):
    if r > n or r < 0:
        return 0
    res = 1
    r = min(r, n - r) # without this, ncR(1000, 999) does way more than needed
    
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res

print(find_element_pascaltriangle(5, 3)) # using ncr formula n! / c! * (n-c)!

def print_nth_row_pascaltriangle(n):
  pass
