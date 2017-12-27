## python secp256k1
py_ecc库的使用, secp256k1中privkey为256位，pubkey为512位。

### 主要方法：

- priv_to_pub(priv)  根据私钥计算公钥

- privtoaddr(priv)  根据私钥计算地址

- ecsign(rawhash, key)  私钥签名

- ecrecover_to_pub(rawhash, v, r, s)  根据签名恢复公钥
