# 所有非役满役种组合(尚未完工)

雀魂段位场的非役满役种一共有 30 种

| 序号 |   役种   | 番数 | 类型  |  备注  |
|:--:|:------:|:--:|:---:|:----:|
| 1  |   立直   | 1  | 门前役 |
| 2  |  两立直   | 2  | 门前役 |
| 3  |   一发   | 1  | 门前役 |
| 4  |   枪杠   | 1  |     | 荣和限定 |
| 5  |  岭上开花  | 1  |     | 自摸限定 |
| 6  |  海底摸月  | 1  |     | 自摸限定 |
| 7  |  河底捞鱼  | 1  |     | 荣和限定 |
| 8  | 门前清自摸和 | 1  | 门前役 | 自摸限定 |
| 9  |   平和   | 1  | 门前役 |
| 10 |  一杯口   | 1  | 门前役 |
| 11 |  二杯口   | 3  | 门前役 |
| 12 |  七对子   | 2  | 门前役 |
| 13 |  役牌 白  | 1  |
| 14 |  役牌 发  | 1  |
| 15 |  役牌 中  | 1  |
| 16 | 役牌 门风牌 | 1  |
| 17 | 役牌 场风牌 | 1  |
| 18 |  断幺九   | 1  |
| 19 | 混全带幺九  | 2  | 食下役 |
| 20 |  一气通贯  | 2  | 食下役 |
| 21 |  三色同顺  | 2  | 食下役 |
| 22 |  三色同刻  | 2  |
| 23 |  三杠子   | 2  |
| 24 |  对对和   | 2  |
| 25 |  三暗刻   | 2  |
| 26 |  小三元   | 2  |
| 27 |  混老头   | 2  |
| 28 | 纯全带幺九  | 3  | 食下役 |
| 29 |  混一色   | 3  | 食下役 |
| 30 |  清一色   | 6  | 食下役 |

下面为了格式对整和缩减篇幅, 我将名称缩写了

|  原名称   | 缩写名称 |
|:------:|:----:|
|  两立直   |  两立  |
|  岭上开花  |  岭上  |
|  海底摸月  |  海底  |
|  河底捞鱼  |  河底  |
| 门前清自摸和 |  自摸  |
|  一杯口   |  一杯  |
|  二杯口   |  二杯  |
|  七对子   |  七对  |
|  役牌 白  |  三元  |
|  役牌 发  |  三元  |
|  役牌 中  |  三元  |
| 役牌 门风牌 |  四风  |
| 役牌 场风牌 |  四风  |
|  断幺九   |  断幺  |
| 混全带幺九  |  混全  |
|  一气通贯  |  一气  |
|  三色同顺  |  三色  |
|  三色同刻  |  三刻  |
|  三杠子   |  三杠  |
|  对对和   |  对对  |
|  三暗刻   |  三暗  |
|  小三元   |  小元  |
|  混老头   |  混老  |
| 纯全带幺九  |  纯全  |
|  混一色   |  混色  |
|  清一色   |  清色  |

## 一级冲突表

标"X"表示纵横对应的两个役种是冲突的无法复合, 其中"岭上"和"平和", "七对", "二杯"只有通过三麻的拔北才能复合, 这里算成冲突, 并用"&"注明

举例来说, "立直"可以与"两立"以外的所有其他役种复合

"两立直"能与除了"枪杠"的所以其他役种复合("枪杠"虽说可以因为国士无双枪暗杠而能和"两立直"复合, 但这样就是役满牌型了,
算番只算国士无双而不算双立直, 不符合要求, 同理"自摸"与"对对"也无法复合, 因为一定是四暗刻或四暗刻单骑)

四种偶然役("枪杠", "岭上", "海底", "河底")是绝对相互冲突的

为了进一步缩减篇幅, 这里将三元牌和四风役牌统称为"役牌"

|    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 立直 | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 一发 |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 枪杠 |    |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 岭上 |    | X  | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 海底 |    |    | X  | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 河底 |    | X  | X  | X  | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 自摸 |    |    | X  |    |    | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 平和 |    |    |    | &X |    |    |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 一杯 |    |    |    |    |    |    |    |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 役牌 |    |    |    |    |    |    |    | X  |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 断幺 |    |    |    |    |    |    |    |    |    | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 两立 | X  |    | X  |    |    |    |    |    |    |    |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 七对 |    |    | X  | &X |    |    |    | X  | X  | X  |    |    | \  |    |    |    |    |    |    |    |    |    |    |    |    |    |
| 混全 |    |    |    |    |    |    |    |    |    |    | X  |    | X  | \  |    |    |    |    |    |    |    |    |    |    |    |    |
| 一气 |    |    |    |    |    |    |    |    |    |    | X  |    | X  | X  | \  |    |    |    |    |    |    |    |    |    |    |    |
| 三色 |    |    |    |    |    |    |    |    |    |    |    |    | X  |    | X  | \  |    |    |    |    |    |    |    |    |    |    |
| 三刻 |    |    |    |    |    |    |    | X  | X  |    |    |    | X  |    | X  | X  | \  |    |    |    |    |    |    |    |    |    |
| 三杠 |    |    |    |    |    |    |    | X  | X  |    |    |    | X  |    | X  | X  |    | \  |    |    |    |    |    |    |    |    |
| 对对 |    |    | X  |    |    |    | X  | X  | X  |    |    |    | X  | X  | X  | X  |    |    | \  |    |    |    |    |    |    |    |
| 三暗 |    |    |    |    |    |    |    | X  | X  |    |    |    | X  |    | X  | X  |    |    |    | \  |    |    |    |    |    |    |
| 小元 |    |    |    |    |    |    |    | X  |    |    | X  |    | X  |    | X  | X  | X  |    |    |    | \  |    |    |    |    |    |
| 混老 |    |    | X  |    |    |    |    | X  | X  |    | X  |    |    | X  | X  | X  |    |    |    |    |    | \  |    |    |    |    |
| 二杯 |    |    | X  | &X |    |    |    |    | X  | X  |    |    | X  |    | X  | X  | X  | X  | X  | X  | X  | X  | \  |    |    |    |
| 纯全 |    |    |    |    |    |    |    |    |    | X  | X  |    | X  | X  | X  |    |    |    | X  |    | X  | X  |    | \  |    |    |
| 混色 |    |    |    |    |    |    |    |    |    |    | X  |    |    |    |    | X  | X  |    |    |    |    |    |    | X  | \  |    |
| 清色 |    |    |    |    |    |    |    |    |    | X  |    |    |    | X  |    | X  | X  |    |    |    | X  | X  |    |    | X  | \  |
| /  | 立直 | 一发 | 枪杠 | 岭上 | 海底 | 河底 | 自摸 | 平和 | 一杯 | 役牌 | 断幺 | 两立 | 七对 | 混全 | 一气 | 三色 | 三刻 | 三杠 | 对对 | 三暗 | 小元 | 混老 | 二杯 | 纯全 | 混色 | 清色 |

## 非复合役种目录(按番数排列)

- 打"*"表示可以复合但一定会伴随存在其他役种, 不符合条件
- 打"^"表示只有副露使得食下役减番才满足条件

此外宝牌是不算役种的

**这里只列举简单的非复合役种, 全部内容因篇幅过长, 具体的组合详情要看对应 markdown 文件**

**因为实在是太多了, 总计少说也有7k, 应该有漏的组合, 八番及以后都尚未完工**

- [一到四番](archive/一到四番.md)
- [五番](archive/五番.md)
- [六番](archive/六番.md)
- [七番](archive/七番.md)
- [八番](archive/八番.md)
- [九番](archive/九番.md)

## 1番

### 门清状态1番

|    | 
|:--:|
| 立直 | 门前役 |
| 一发 | 门前役 |
| 枪杠 |     | 荣和限定 |
| 岭上 |     | 自摸限定 |
| 海底 |     | 自摸限定 |
| 河底 |     | 荣和限定 |
| 自摸 | 门前役 | 自摸限定 |
| 平和 | 门前役 |
| 一杯 | 门前役 |
| 三元 |
| 四风 |
| 断幺 |

小计: 15

### 副露后1番的食下役

|     | 
|:---:|
| ^混全 |
| ^一气 |
| ^三色 |

小计: 3

## 2番

### 门清状态2番

"小元"和"混老"无法单独出现, "小元"一定有两个三元役, "混老"一定有"七对"或"对对"

|     | 
|:---:|
| 两立  | 门前役 |
| 七对  | 门前役 |
| 混全  | 食下役 |
| 一气  | 食下役 |
| 三色  | 食下役 |
| 三刻  |
| 三杠  |
| 对对  |
| 三暗  |
| *小元 |
| *混老 |

小计: 11

### 副露后2番的食下役

|     | 
|:---:|
| ^纯全 |
| ^混色 |

小计: 2

## 3番

|    | 
|:--:|
| 二杯 | 门前役 |
| 纯全 | 食下役 |
| 混色 | 食下役 |

小计: 3

## 5番

### 副露后5番的食下役

|     | 
|:---:|
| ^清色 |

小计: 1

## 6番

|    | 
|:--:|
| 清色 | 食下役 |

小计: 1

