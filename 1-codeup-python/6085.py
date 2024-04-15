w, h, b = map(int, input().split(' '))
mem_bit = w * h * b
mem_byte = mem_bit / 8
mem_kb = mem_byte / 1024
mem_mb = mem_kb / 1024

print(format(mem_mb, ".2f"), "MB")