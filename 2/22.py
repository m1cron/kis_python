def f22(num):
    a_b = (num & 0x7F)
    c = (num & 0xF80) << 12
    d = (num & 0x7F000) >> 5
    e = (num & 0x7F80000) << 5
    f = (num & 0xF8000000) >> 13
    return int(e + c + f + d + a_b)

res = f22(0x76006e69)
print('0x%x'%res)
res = f22(0x6e9b1a5c)
print('0x%x'%res)