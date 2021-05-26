# OGLE

This is the capstone project for `统计学习导论`, 2021 Spring

## Preparation

download the data file from [Tsinghua Cloud Storage](https://cloud.tsinghua.edu.cn/f/e5e3acbed81c4d3298b3/)(95.3MB) and put it under `data` directory.

project structure:

```
OGLE
 |--code
 |  |--main.py
 |  |--data.py
 |  `--utils.py
 |--data
 |  `--query_1621408997.07960f_startable.txt
 |--figures
 `--logs
```

## Run

from the root directory, run `python code/main.py`

## Results

train/test on 0.1 of all data, the test confusion matrix:

```
[[  931    69    26     1     0]
 [    1 44651   358     1     0]
 [  113  2980  5139     0     0]
 [    3    76     9    29     0]
 [   15     3    14     0     0]]
```

acc: 0.9326

mean acc: 0.5541