## RLP(Recursive Length Prefix)
   RLP是Ethereum中主要的序列化和反序列化方法。
   具体参考 [Ethereum RLP wiki](https://github.com/ethereum/wiki/wiki/RLP)
   [Source code](https://github.com/ethereum/pyrlp)

### RLP is defined as follows:

- `单字节`，值在[0x00, 0x7f]间，RLP编码为它本身；

- `string`，可以认为是固定字节数的二进制数据，根据字符串长度分为两种：

    - 0-55字节长，RLP编码的第一个字节为0x80加字符串长度，即值在[0x80, 0xb7]间，后面字节为string的字节表示；
    
    - 大于55字节长，RLP编码的第一个字节为0xbf加字符串长度的字节长度(如：1024字节的字符串，1024需要用2字节'\x04\x00'
    表示，所以它的第一个字节为0xb9), 紧跟字节为字符串长度(如：\x04\x00)，最后字节为String的字节表示；

- `list`，根据大小也分为两种：

    - 0-55字节长，RLP编码的第一个字节为0xc0加列表字节长度，值在[0xc0, 0xf7]间，后面字节为列表中每项RLP编码的联结；
    
    - 大于55字节长，RLP编码的第一个字节为0xf7加列表字节长度的长度，值在[0xf8, 0xff]，紧跟字节为列表长度，最后字节为
    列表中每项RLP编码的联结；
