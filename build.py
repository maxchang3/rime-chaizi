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
    chaizi = []
    yaml = [HEADER]
    is_empty = lambda x: x != ' '
    # https://github.com/kfcd/chaizi/raw/master/chaizi-jt.txt
    with open("chaizi-jt.txt") as f:
        chaizi = f.readlines()
    for line in chaizi:
        char, units = line.strip().split("\t", 1)
        if (char == "□"): continue  # 去除错误字符
        for unit in units.split('\t'):
            pinyin_list = lazy_pinyin(unit.split())
            pinyin = "".join(filter(is_empty, pinyin_list))
            if not pinyin.isalpha(): continue
            item = f"{char.strip()}\t{pinyin}"
            if (item in yaml): continue  # 去重
            yaml.append(item)
    with open("build/chaizi.dict.yaml", "w") as f:
        f.write("\n".join(yaml))

if __name__ == "__main__":
    chai()
