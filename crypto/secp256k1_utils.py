from py_ecc.secp256k1 import privtopub, ecdsa_raw_recover, ecdsa_raw_sign

from crypto.utils import encode_int32, normalize_key, sha3


def ecrecover_to_pub(rawhash, v, r, s):
    result = ecdsa_raw_recover(rawhash, (v, r, s))
    if result:
        x, y = result
        pub = encode_int32(x) + encode_int32(y)
    else:
        raise ValueError('Invalid VRS')
    assert len(pub) == 64
    return pub

def ecsign(rawhash, key):
    v, r, s = ecdsa_raw_sign(rawhash, key)
    return v, r, s

def priv_to_pub(priv):
    x, y = privtopub(priv)
    return x, y

def privtoaddr(k):
    k = normalize_key(k)
    x, y = privtopub(k)
    return sha3(encode_int32(x) + encode_int32(y))[12:]


if __name__ == '__main__':
    import binascii
    priv = binascii.unhexlify('792eca682b890b31356247f2b04662bff448b6bb19ea1c8ab48da222c894ef9b')
    print(priv_to_pub(priv))
    addr = privtoaddr(priv)
    print(binascii.hexlify(addr))

    print('\n============')
    v, r, s = ecsign(b'\x35' * 32, priv)
    print(v, r, s)
    pub = ecrecover_to_pub(b'\x35' * 32, v, r, s)
    print(pub)
    print(binascii.hexlify(pub))
