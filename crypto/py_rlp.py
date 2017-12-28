import binascii
from math import ceil

def str_to_bytes(value):
    if isinstance(value, bytearray):
        value = bytes(value)
    if isinstance(value, bytes):
        return value
    return bytes(value, 'utf-8')

def bytes_to_str(value):
    if isinstance(value, str):
        return value
    return value.decode('utf-8')

def ascii_chr(value):
    return bytes([value])

def int_to_big_endian(value):
    byte_length = max(ceil(value.bit_length() / 8), 1)
    return (value).to_bytes(byte_length, byteorder='big')

def big_endian_to_int(value):
    return int.from_bytes(value, byteorder='big')

def is_integer(value):
    return isinstance(value, int)

'''
input: hex str or bytes
output: bytes
example: 48656c6c6f -> b'Hello', 3132666564636261 -> b'12fedcba', 'Bb14FF' -> b'\xbb\x14\xff'
'''
def decode_hex(s):
    if isinstance(s, str):
        return bytes.fromhex(s)
    if isinstance(s, (bytes, bytearray)):
        return binascii.unhexlify(s)
    raise TypeError('Value must be an instance of str or bytes')

'''
input: str or bytes
output: str
example: 'Hello' -> 48656c6c6f,  b'Hello' -> 48656c6c6f, '12fedcba' -> 3132666564636261
'''
def encode_hex(b):
    if isinstance(b, str):
        b = bytes(b, 'utf-8')
    if isinstance(b, (bytes, bytearray)):
        return str(binascii.hexlify(b), 'utf-8')
    raise TypeError('Value must be an instance of str or bytes')

def safe_ord(c):
    try:
        return ord(c)
    except TypeError:
        assert isinstance(c, int)
        return c

if __name__ == '__main__':
    a = 1000000
    b = int_to_big_endian(a)
    print('%s -- int_to_big_endian: %s' % (a, b))
    c = big_endian_to_int(b)
    print('%s -- big endian to int: %s' % (b, c))

    str1 = '12fedcba'
    e_str1 = encode_hex(str1)
    print('%s -- encode hex: %s' % (str1, e_str1))
    d_str1 = decode_hex(e_str1)
    print('%s -- decode hex: %s' % (e_str1, d_str1))
    print(type(e_str1))
    print(type(d_str1))
