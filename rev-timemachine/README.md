# rev-timemachine

## Решение
Находим какие параметры необходимы для выполнения логического условия. (pass=1338; cnt=32).
``` c++
(((((((((pass << 3) << 2) >> 1) << 7) ^ 832515) ^ 763) ^ 6125124) << 2) == 31474416 && ((((cnt << 7) ^ 3) >> 4) >> 1) == 16)
```
Передать эти параметры можно будет либо с помощью прямого вызова ```gen_flag()```, либо же написав обертку для ```time()``` и использовав ее через ```LD_PRELOAD```. Флаг обернуть в LKLCTF{}

## Флаг
```Th4t_w4s_3asy_d0esnt_1t```