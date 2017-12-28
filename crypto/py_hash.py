from _pysha3 import sha3_256, keccak_256
from pyblake2 import blake2b, blake2s
from crypto.utils import sha3
import binascii

'''
    # blake2b 最大支持64位摘要
    blake2b(data=b'', digest_size=64, key=b'', salt=b'', \
                person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0,  \
                node_depth=0, inner_size=0, last_node=False)

    # blake2s 最大支持32位摘要，两者相同位数哈希值不同
    blake2s(data=b'', digest_size=32, key=b'', salt=b'', \
                person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0,  \
                node_depth=0, inner_size=0, last_node=False)
'''

def py_blake2b():
    h = blake2b(digest_size=32)
    h.update(b'Hello World')
    return h.hexdigest()

def py_blake2s():
    s = blake2s(digest_size=32)
    s.update(b'Hello World')
    return s.hexdigest()

def py_sha3():
    m = sha3_256()
    m.update(b'Hello World')
    return m.hexdigest()

# keccak_256 as same as util_sha3
def py_keccak_256():
    k = keccak_256()
    k.update(b'Hello World')
    return k.hexdigest()

def util_sha3():
    return binascii.hexlify(sha3(b'Hello World'))

if __name__ == '__main__':
    print(py_blake2b())
    print(py_blake2s())
    print(py_sha3())
    print(py_keccak_256())
    print(util_sha3())
