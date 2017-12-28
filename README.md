## A wrapper of python-crypto libs
1. py_ecc, 基于椭圆曲线的签名算法，其中privkey为256位，pubkey为512位

2. pysha3, length of digest is 32 bytes

3. pyblake2, blake2b最长64bytes，blake2s最长32bytes

**bench_hash中有对几种哈希算法的性能比较**

### secp256k1主要方法：

- priv_to_pub(priv)  根据私钥计算公钥

- privtoaddr(priv)  根据私钥计算地址

- ecsign(rawhash, key)  私钥签名

- ecrecover_to_pub(rawhash, v, r, s)  根据签名恢复公钥
