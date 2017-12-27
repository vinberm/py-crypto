import time
from pyblake2 import blake2s, blake2b
from _pysha3 import keccak_256
'''
**Test result**
BLAKE2b hashing 1000 MiB
  ***** 7a713959d80959732842f06bb35dc8561fcff9cb46f0b6ab79e8ac12fc6027eb
  time for 1000 MiB hashed: 1.502 seconds
  hashed 665.60 MiB per second

BLAKE2s hashing 1000 MiB
  ***** 078945a14a3b5c32b00641bd23344a3a24ae240e824c23e9cee5d94f6d834e58
  time for 1000 MiB hashed: 1.889 seconds
  hashed 529.40 MiB per second

KECCAK256 hashing 1000 MiB
  ***** eedc42479d3dbfc8457d3881e9cb9c8dcff2884c941280eb88dd6b914fa41b47
  time for 1000 MiB hashed: 3.490 seconds
  hashed 286.52 MiB per second
ending... see you next time!
'''

mib = 2 ** 20
text = b'v' * mib

def bench2b(bytes=1):
    mibs = mib * bytes
    print('')
    print('BLAKE2b hashing %s MiB' % (bytes))

    t0 = time.time()
    b2b = blake2b(digest_size=32)
    for i in range(bytes):
        b2b.update(text)
    digest = b2b.hexdigest()
    t1 = time.time()

    print('  ***** %s' % digest)

    elapsed = t1 - t0
    print('  time for %d MiB hashed: %.3f seconds' % (bytes, elapsed))
    print('  hashed %.2f MiB per second' % (mibs/mib/elapsed))


def bench2s(bytes=1):
    mibs = mib * bytes
    print('')
    print('BLAKE2s hashing %s MiB' % (bytes))

    t0 = time.time()
    b2s = blake2s(digest_size=32)
    for i in range(bytes):
        b2s.update(text)
    digest = b2s.hexdigest()
    t1 = time.time()

    print('  ***** %s' % digest)

    elapsed = t1 - t0
    print('  time for %d MiB hashed: %.3f seconds' % (bytes, elapsed))
    print('  hashed %.2f MiB per second' % (mibs / mib / elapsed))

def bench_keccak256(bytes=1):
    mibs = mib * bytes
    print('')
    print('KECCAK256 hashing %s MiB' % (bytes))

    t0 = time.time()
    kecc256 = keccak_256()
    for i in range(bytes):
        kecc256.update(text)
    digest = kecc256.hexdigest()
    t1 = time.time()

    print('  ***** %s' % digest)

    elapsed = t1 - t0
    print('  time for %d MiB hashed: %.3f seconds' % (bytes, elapsed))
    print('  hashed %.2f MiB per second' % (mibs / mib / elapsed))

if __name__ == '__main__':
    print('start bench...')
    b = 1000
    bench2b(b)
    bench2s(b)
    bench_keccak256(b)
    print('ending... see you next time!')
