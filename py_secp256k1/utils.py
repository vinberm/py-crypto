
import sha3 as _sha3

def sha3_256(x): return _sha3.keccak_256(x).digest()

from rlp.sedes import big_endian_int
import binascii
import sys


def is_numeric(x):
    return isinstance(x, int)


def encode_int32(v):
    return zpad(int_to_big_endian(v), 32) # Pad zero to 32 bytes

def int_to_big_endian(x):
    return big_endian_int.serialize(x) # Serialize interger to big endian

def zpad(x, l):
    """ Left zero pad value `x` at least to length `l`.

    >>> zpad('', 1)
    '\x00'
    >>> zpad('\xca\xfe', 4)
    '\x00\x00\xca\xfe'
    >>> zpad('\xff', 1)
    '\xff'
    >>> zpad('\xca\xfe', 2)
    '\xca\xfe'
    """
    return b'\x00' * max(0, l - len(x)) + x

def decode_hex(s):
    if isinstance(s, str):
        return bytes.fromhex(s)
    if isinstance(s, (bytes, bytearray)):
        return binascii.unhexlify(s)
    raise TypeError('Value must be an instance of str or bytes')

def normalize_key(key):
    if is_numeric(key):
        o = encode_int32(key)
    elif len(key) == 32:
        o = key
    elif len(key) == 64:
        o = decode_hex(key)
    elif len(key) == 66 and key[:2] == '0x':
        o = decode_hex(key[2:])
    else:
        raise Exception("Invalid key format: %r" % key)
    if o == b'\x00' * 32:
        raise Exception("Zero privkey invalid")
    return o

def sha3(seed):
    return sha3_256(to_string(seed))

if sys.version_info.major == 2:
    def to_string(value):
        return str(value)
else:
    def to_string(value):
        if isinstance(value, bytes):
            return value
        if isinstance(value, str):
            return bytes(value, 'utf-8')
        if isinstance(value, int):
            return bytes(str(value), 'utf-8')
