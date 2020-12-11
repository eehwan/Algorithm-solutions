def GCD(a, b):
    while a:
        a, b = b%a, a
    return b
def solution(w,h):
    total = w*h
    multiple = GCD(w, h)
    w, h = w/multiple, h/multiple
    return total - (w+h-1)*multiple
