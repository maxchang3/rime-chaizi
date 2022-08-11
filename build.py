#! /usr/bin/python
# coding = utf-8
# By Gerry @ 2019.12.28
# Usage: make chaizi dictionary for rime
# base on :
# https://github.com/mozillazg/python-pinyin
# https://github.com/kfcd/chaizi
# Modified by Max @ 2022.06.05

from datetime import datetime
from pypinyin import lazy_pinyin

HEADER = f'''---
name: chaizi
version: "{datetime.now().strftime("%Y.%m.%d")}"
sort: by_weight
use_preset_vocabulary: true
...'''

def chai():
    lines = []
    # https://github.com/kfcd/chaizi/raw/master/chaizi-jt.txt
    with open("chaizi-jt.txt") as f:
        lines = f.readlines()
    res = []
    res.append(HEADER)
    for line in lines:
        data = line.strip().split("\t")
        if (data[0] == "□"): continue  # 去除错误字符
        for i in range(1, len(data)):
            py = "".join(lazy_pinyin(data[i].replace(" ", "")))
            if not py.isalpha(): continue
            item = f"{data[0].strip()}\t{py}"
            if (item in res): continue  # 去重
            res.append(item)
    with open("src/chaizi.dict.yaml", "w") as f:
        f.write("\n".join(res))

if __name__ == "__main__":
    chai()
