import rlp

def test_str():
    s = 'Hello World'
    se = rlp.encode(s)
    sd = rlp.decode(se)
    assert b'Hello World' == sd

def test_list():
    s = ['Hi', 1, [23, 'Nov']]
    se = rlp.encode(s)
    sd = rlp.decode(se)
    s_ = [b'Hi', b'\x01', [b'\x17', b'Nov']]
    assert s_ == sd
