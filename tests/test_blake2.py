from pyblake2 import blake2b, blake2s

def test_blake2b():
    h = blake2b()
    h.update(b'Hello World')
    assert h.hexdigest() == '4386a08a265111c9896f56456e2cb61a64239115c4784cf438e36cc851221972da3fb0115f73cd02486254001f878ab1fd126aac69844ef1c1ca152379d0a9bd'

def test_blake2b_32():
    h = blake2b(digest_size=32)
    h.update(b'Hello World')
    assert len(h.digest())== 32
    assert h.hexdigest() == '1dc01772ee0171f5f614c673e3c7fa1107a8cf727bdf5a6dadb379e93c0d1d00'

def test_blake2bs_32():
    h = blake2s(digest_size=32)
    h.update(b'Hello World')
    assert len(h.digest()) == 32
    assert h.hexdigest() == '7706af019148849e516f95ba630307a2018bb7bf03803eca5ed7ed2c3c013513'
