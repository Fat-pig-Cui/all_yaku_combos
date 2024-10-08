# 所有非役满役种组合之: 只含混全和混色的二杯口专题

因为能与二杯口复合的役很少, 而且大部分已经在之前的专题中用到了, 这里手牌役就只剩 混全带幺九 和 混一色 了

其他能复合的役种: [断幺](../一般形断幺九专题), [平和](../无断幺的平和专题),
[清一色](../无断幺平和的一般形清一色专题), [纯全带幺九](../无平和清一色的纯全带幺九专题)

打"&"表示只有三麻的拔北可以做到, 不计数

## 二杯口一级复合表(只含混全带幺九, 混一色)

| 役种  | 番数 |            备注            |
|:---:|:--:|:------------------------:|
| 立直  | 1  |
| 一发  | 1  |
| &岭上 | 1  | 自摸限定, 只有三麻的拔北能做到, 且一定有自摸 |
| 海底  | 1  |       自摸限定, 一定有自摸        |
| 河底  | 1  |           荣和限定           |
| 自摸  | 1  |           自摸限定           |
|     |    |
| 两立  | 2  |
| 混全  | 2  |
|     |    |
| 混色  | 3  |

### 拆分: 手牌役部分

| 役种 | 番数 | 备注 |
|:--:|:--:|:--:|
| 混全 | 2  |
|    |    |
| 混色 | 3  |

### 拆分: 条件役部分

| 役种  | 番数 |            备注            |
|:---:|:--:|:------------------------:|
| 立直  | 1  |
| 一发  | 1  |
| &岭上 | 1  | 自摸限定, 只有三麻的拔北能做到, 且一定有自摸 |
| 海底  | 1  |       自摸限定, 一定有自摸        |
| 河底  | 1  |           荣和限定           |
|     |    |
| 自摸  | 1  |           自摸限定           |
|     |    |
| 两立  | 2  |

## 3番

|    | 
|:--:|
| 二杯 |

**3番总计: 1**

## 5番

|    |    |
|:--:|:--:|
| 二杯 | 混全 |

**3番总计: 1**

## 6番

|    |    |
|:--:|:--:|
| 二杯 | 混色 |

**6番总计: 1**

## 8番

|    |    |    |
|:--:|:--:|:--:|
| 二杯 | 混色 | 混全 |

**8番总计: 1**

## 二杯口 小计: 4

| 番数 | 总数 |
|:--:|:--:|
| 3  | 1  |
| 4  | 0  |
| 5  | 1  |
| 6  | 1  |
| 7  | 0  |
| 8  | 1  |

该总计表格赋值给 `table` 和 `new_table`

## 条件役展开

"枪杠"无法与"二杯"复合, 这里剔除"枪杠"

"岭上"也无法与"二杯"复合, 但最后会提一下

### 1番

|    |
|:--:|
| 立直 |
| 河底 |
| 自摸 |

小计: 3

### 2番

|    |
|:--:|
| 两立 |

|     |    |
|:---:|:--:|
| 立直  | 一发 |
| 立直  | 河底 |
| 立直  | 自摸 |
|     |    |
| &岭上 | 自摸 |
| 海底  | 自摸 |

小计: 5

### 3番

#### 3番_2+1

|    |    |
|:--:|:--:|
| 两立 | 一发 |
| 两立 | 河底 |
| 两立 | 自摸 |

#### 3番_1+1+1

|     |    |    |
|:---:|:--:|:--:|
| 立直  | 一发 | 自摸 |
| &立直 | 岭上 | 自摸 |
| 立直  | 海底 | 自摸 |

小计: 5

### 4番

#### 4番_2+1+1

|     |    |    |
|:---:|:--:|:--:|
| 两立  | 一发 | 自摸 |
| &两立 | 岭上 | 自摸 |
| 两立  | 海底 | 自摸 |

#### 4番_1+1+1+1

|    |    |    |    |
|:--:|:--:|:--:|:--:|
| 立直 | 一发 | 海底 | 自摸 |

小计: 3

### 所用 table 汇总

| table型 | 番数 | 数量 |
|:------:|:--:|:--:|
| table  | 1  | 3  |
| table  | 2  | 5  |
| table  | 3  | 5  |
| table  | 4  | 3  |

使用 [辅助计算脚本](辅助计算脚本.py) 来进行计算得到结果

## 二杯口 总计: 68

| 番数 | 总数 |
|:--:|:--:|
| 3  | 1  |
| 4  | 3  |
| 5  | 6  |
| 6  | 9  |
| 7  | 11 |
| 8  | 11 |
| 9  | 11 |
| 10 | 8  |
| 11 | 5  |
| 12 | 3  |
|    |    |
| 总计 | 68 |

此外若考虑岭上会多 4 * 3 = 12 种
