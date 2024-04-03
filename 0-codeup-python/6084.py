h, b, c, s = map(int, input().split(' '))
memory = (h * b * c * s) / 8
memory_mb = memory / (2 ** 10 * 2 ** 10)

print(format(memory_mb, ".1f"), "MB")