from py_secp256k1.secp256k1_utils import ecrecover_to_pub, ecsign, priv_to_pub
import binascii

priv = binascii.unhexlify('792eca682b890b31356247f2b04662bff448b6bb19ea1c8ab48da222c894ef9b')
# pub: two big interger; pub_byte: concate two int and convert into bytes
pub = (20033694065814990006010338153307081985267967222430278129327181081381512401190, 72089573118161052907088366229362685603474623289048716349537937839432544970413)
pub_byte = b'2c4aab447fc5b593be6a2bd1c54a2737666c88e0dd74b99881a52532a1d7d1269f6140a01a6719a51b4988a38135af5ede0672ab01afa6b118e8f38b661666ad'

def test_privtopub():
    # get pubkey from private key
    assert priv_to_pub(priv) == pub


def test_ecsign():
    # signature, and recover pubkey from signature
    v, r, s = ecsign(b'\x35' * 32, priv)
    assert binascii.hexlify(ecrecover_to_pub(b'\x35' * 32, v, r, s)) == pub_byte
