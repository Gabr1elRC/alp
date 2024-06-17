def eprimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(eprimo(2))
print(eprimo(7))
print(eprimo(10))