# Python implementation of Cauchy-Crofton formula

## Auther

* Hyosang Kang (DGIST)

## How to use

The `cc` class implements Cauchy-Crofton algorithm to approximate the length of a curve in the given file. For the best result, the file should be a black-and-white image with the curve drawn in black.

```
c = cc(filename, actual_width, actual_height)
c.run(distance_increment, angle_increment)
```

For test result, run `cc.py`.
```
$ python3 cc.py
```
This will compute the length of curve (a circle) in `test.png`.