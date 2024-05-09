# magic_number

## 平方：太神奇了！

Find three numbers which the sum of square is eqaul to sum of square of its reversed number.

For example, `(2, 3, 8)` and `(6, 5, 4)`. `26**2+35**2+84**2=62**2+53**2+48**2=8957`

This experiment is also extend the 2-bit, 3-bit and n-bit numbers. 

The code is written in Python using the exhaustion method.

Talk is cheap show me the [code](magic_number.py).

See also [平方：太神奇了！](https://mp.weixin.qq.com/s/BnI1KjDKHCFi15QbInyrJw).

```shell
> python magic_number.py
try to solve one-bit magic number
For total 62, found 2 solutions: [[1, 5, 6], [7, 3, 2]]
For example, 17**2+53**2+62**2=6942, and 71**2+35**2+26**2=6942

For total 69, found 2 solutions: [[1, 2, 8], [7, 4, 2]]
For example, 17**2+24**2+82**2=7589, and 71**2+42**2+28**2=7589

For total 74, found 2 solutions: [[1, 3, 8], [7, 4, 3]]
For example, 17**2+34**2+83**2=8334, and 71**2+43**2+38**2=8334

For total 77, found 2 solutions: [[2, 3, 8], [6, 5, 4]]
For example, 26**2+35**2+84**2=8957, and 62**2+53**2+48**2=8957

For total 86, found 2 solutions: [[1, 2, 9], [7, 6, 1]]
For example, 17**2+26**2+91**2=9246, and 71**2+62**2+19**2=9246

For total 89, found 2 solutions: [[2, 6, 7], [8, 4, 3]]
For example, 28**2+64**2+73**2=10209, and 82**2+46**2+37**2=10209

For total 90, found 2 solutions: [[1, 5, 8], [7, 5, 4]]
For example, 17**2+55**2+84**2=10370, and 71**2+55**2+48**2=10370

For total 94, found 2 solutions: [[2, 3, 9], [7, 6, 3]]
For example, 27**2+36**2+93**2=10674, and 72**2+63**2+39**2=10674

For total 98, found 2 solutions: [[1, 4, 9], [8, 5, 3]]
For example, 18**2+45**2+93**2=10998, and 81**2+54**2+39**2=10998

For total 101, found 3 solutions: [[1, 6, 8], [9, 4, 2], [4, 6, 7]]
For example, 19**2+64**2+82**2=11181, and 91**2+46**2+28**2=11181

For total 110, found 2 solutions: [[2, 5, 9], [7, 6, 5]]
For example, 27**2+56**2+95**2=12890, and 72**2+65**2+59**2=12890

For total 122, found 2 solutions: [[3, 7, 8], [9, 5, 4]]
For example, 39**2+75**2+84**2=14202, and 93**2+57**2+48**2=14202

For total 146, found 2 solutions: [[1, 8, 9], [9, 7, 4]]
For example, 19**2+87**2+94**2=16766, and 91**2+78**2+49**2=16766

For total 149, found 2 solutions: [[2, 8, 9], [8, 7, 6]]
For example, 28**2+87**2+96**2=17569, and 82**2+78**2+69**2=17569

try to solve two-bit magic number
For total 521, found 2 solutions: [[10, 14, 15], [16, 12, 11]]
For example, 1016**2+1412**2+1511**2=5309121, and 1610**2+1214**2+1115**2=5309121

For total 602, found 2 solutions: [[11, 15, 16], [17, 13, 12]]
For example, 1117**2+1513**2+1612**2=6135402, and 1711**2+1315**2+1216**2=6135402

For total 614, found 2 solutions: [[10, 15, 17], [18, 13, 11]]
For example, 1018**2+1513**2+1711**2=6253014, and 1810**2+1315**2+1117**2=6253014

For total 621, found 2 solutions: [[10, 11, 20], [16, 14, 13]]
For example, 1016**2+1114**2+2013**2=6325421, and 1610**2+1411**2+1320**2=6325421
...
```

## 奇妙的平方数

Find bit-with number which the squrare of it is a revserse result of the reverse original number.

For example, 12**2=144, and 21**2=441 for decimal number.

For example, 0x12**2=0x144, and 0x21**2=0x441 for hexadecimal number.

Do you find some interesting results?

The code is written in Python using the exhaustion method.

Talk is cheap show me the [code](fantastic_squares.py).

see also [奇妙的平方数](https://mp.weixin.qq.com/s/naHCaGI6EtTSwlRGy7EVaA).

```shell
> python fantastic_squares.py 
processing ...

Try to solve bit width 2-5 for radix 8 fantastic squares
For bit 2 radix 8 numbers, found 4 solutions: ['11', '12', '21', '33'] or [9, 10, 17, 27] in decimal number format, for example: 11**2=121, and 11**2=121 in 8-radix number format
For bit 3 radix 8 numbers, found 11 solutions: ['101', '102', '111', '112', '121', '201', '211', '303', '306', '333', '603'] or [65, 66, 73, 74, 81, 129, 137, 195, 198, 219, 387] in decimal number format, for example: 101**2=10201, and 101**2=10201 in 8-radix number format
For bit 4 radix 8 numbers, found 22 solutions: ['1001', '1002', '1011', '1012', '1021', '1101', '1102', '1111', '1112', '1121', '1201', '1211', '2001', '2011', '2101', '2111', '3003', '3006', '3033', '3303', '3333', '6003'] or [513, 514, 521, 522, 529, 577, 578, 585, 586, 593, 641, 649, 1025, 1033, 1089, 1097, 1539, 1542, 1563, 1731, 1755, 3075] in decimal number format, for example: 1001**2=1002001, and 1001**2=1002001 in 8-radix number format

Try to solve bit width 2-5 for radix 10 fantastic squares
For bit 2 radix 10 numbers, found 6 solutions: ['11', '12', '13', '21', '22', '31'] or [11, 12, 13, 21, 22, 31] in decimal number format, for example: 11**2=121, and 11**2=121 in 10-radix number format
For bit 3 radix 10 numbers, found 15 solutions: ['101', '102', '103', '111', '112', '113', '121', '122', '201', '202', '211', '212', '221', '301', '311'] or [101, 102, 103, 111, 112, 113, 121, 122, 201, 202, 211, 212, 221, 301, 311] in decimal number format, for example: 101**2=10201, and 101**2=10201 in 10-radix number format
For bit 4 radix 10 numbers, found 39 solutions: ['1001', '1002', '1003', '1011', '1012', '1013', '1021', '1022', '1031', '1101', '1102', '1103', '1111', '1112', '1113', '1121', '1122', '1201', '1202', '1211', '1212', '1301', '2001', '2002', '2011', '2012', '2021', '2022', '2101', '2102', '2111', '2121', '2201', '2202', '2211', '3001', '3011', '3101', '3111'] or [1001, 1002, 1003, 1011, 1012, 1013, 1021, 1022, 1031, 1101, 1102, 1103, 1111, 1112, 1113, 1121, 1122, 1201, 1202, 1211, 1212, 1301, 2001, 2002, 2011, 2012, 2021, 2022, 2101, 2102, 2111, 2121, 2201, 2202, 2211, 3001, 3011, 3101, 3111] in decimal number format, for example: 1001**2=1002001, and 1001**2=1002001 in 10-radix number format

Try to solve bit width 2-5 for radix 16 fantastic squares
For bit 2 radix 16 numbers, found 8 solutions: ['11', '12', '13', '21', '22', '23', '31', '32'] or [17, 18, 19, 33, 34, 35, 49, 50] in decimal number format, for example: 11**2=121, and 11**2=121 in 16-radix number format   
For bit 3 radix 16 numbers, found 25 solutions: ['101', '102', '103', '111', '112', '113', '121', '122', '123', '131', '132', '201', '202', '203', '211', '212', '213', '221', '222', '231', '301', '302', '311', '312', '321'] or [257, 258, 259, 273, 274, 275, 289, 290, 291, 305, 306, 513, 514, 515, 529, 530, 531, 545, 546, 561, 769, 770, 785, 786, 801] in decimal number format, for example: 101**2=10201, and 101**2=10201 in 16-radix number format
For bit 4 radix 16 numbers, found 81 solutions: ['1001', '1002', '1003', '1011', '1012', '1013', '1021', '1022', '1023', '1031', '1032', '1101', '1102', '1103', '1111', '1112', '1113', '1121', '1122', '1123', '1131', '1132', '1201', '1202', '1203', '1211', '1212', '1213', '1221', '1222', '1231', '1301', '1302', '1311', '1312', '1321', '2001', '2002', '2003', '2011', '2012', '2013', '2021', '2022', '2023', '2031', '2032', '2101', '2102', '2103', '2111', '2112', '2113', '2121', '2122', '2131', '2132', '2201', '2202', '2203', '2211', '2212', '2221', '2301', '2302', '2311', '2312', '3001', '3002', '3011', '3012', '3021', '3022', '3101', '3102', '3111', '3112', '3121', '3201', '3202', '3211'] or [4097, 4098, 4099, 4113, 4114, 4115, 4129, 4130, 4131, 4145, 4146, 4353, 4354, 4355, 4369, 4370, 4371, 4385, 4386, 4387, 4401, 4402, 4609, 4610, 4611, 4625, 4626, 4627, 4641, 4642, 4657, 4865, 4866, 4881, 4882, 4897, 8193, 8194, 8195, 8209, 8210, 8211, 8225, 8226, 8227, 8241, 8242, 8449, 8450, 8451, 8465, 8466, 8467, 8481, 8482, 8497, 8498, 8705, 8706, 8707, 8721, 8722, 8737, 8961, 8962, 8977, 8978, 12289, 12290, 12305, 12306, 12321, 12322, 12545, 12546, 12561, 12562, 12577, 12801, 12802, 12817] in decimal number format, for example: 1001**2=1002001, and 1001**2=1002001 in 16-radix number format

```
