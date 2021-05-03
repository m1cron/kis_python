import struct

C_SIZE = 10 #4+4+2
D_SIZE = 8+2+4+4+(4*4)+1+4+1+1
A_SIZE = 4 + 4 + 1 + (8 * 5) + 4 + 4 + 8

def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>iIh', c_bytes)
    return {'C1': c_parsed[0], 'C2': c_parsed[1], 'C3': c_parsed[2]}

def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>qHIIIIIIBibb', d_bytes)
    d3_bytes = byte_string[d_parsed[3]:d_parsed[3] + d_parsed[2] * 2]
    d3_parsed = struct.unpack('>' + 'H' * d_parsed[2], d3_bytes)
    return {'D1': d_parsed[0], 'D2': d_parsed[1], 'D3': list(d3_parsed), 'D4': list(d_parsed[4:8]),
        'D5': d_parsed[8], 'D6': d_parsed[9], 'D7': d_parsed[10], 'D8': d_parsed[11]}

def parse_b(offset, byte_string):
    b1_parsed = [parse_c(offset, byte_string),
                 parse_c(offset + C_SIZE * 1, byte_string),
                 parse_c(offset + C_SIZE * 2, byte_string),
                 parse_c(offset + C_SIZE * 3, byte_string),
                 parse_c(offset + C_SIZE * 4, byte_string)]
    b2_parsed = parse_d(offset + C_SIZE * 5, byte_string)
    b3_bytes = byte_string[offset + (C_SIZE * 5) + D_SIZE : offset + (C_SIZE * 5) + 4 + D_SIZE]
    b3_parsed = struct.unpack('>I', b3_bytes)[0]
    return {'B1': b1_parsed, 'B2': b2_parsed, 'B3': b3_parsed}

def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE]
    a_parsed = struct.unpack('>IIbqqqqqIid', a_bytes)
    return {'A1': parse_b(a_parsed[0], byte_string), 'A2': a_parsed[1], 'A3': a_parsed[2], 'A4': list(a_parsed[3:8]), 'A5': a_parsed[8], 'A6': a_parsed[9], 'A7': a_parsed[10]}

def f31(byte_string):
    return parse_a(3, byte_string)
