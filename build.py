#! /usr/bin/python
# coding = utf-8
# By Gerry @ 2019.12.28
# Usage: make chaizi dictionary for rime
# base on :
# https://github.com/mozillazg/python-pinyin
# https://github.com/kfcd/chaizi
# Modified by Max @ 2022.06.05

from datetime import datetime
from itertools import product
import pypinyin

HEADER = f'''---
name: chaizi
version: "{datetime.now().strftime("%Y.%m.%d")}"
sort: by_weight
use_preset_vocabulary: true
...\n'''


is_not_empty = lambda x: x != ' '

def chai():
    chaizi = []
    yaml = set()
    # https://github.com/kfcd/chaizi/raw/master/chaizi-jt.txt
    with open("chaizi-jt.txt") as f:
        chaizi = f.readlines()
    for line in chaizi:
        char, units = line.strip().split("\t", 1)
        if (char == "□"): continue  # 去除错误字符
        for unit in units.split('\t'):
            pinyin_list = pypinyin.pinyin(unit.split(), style=pypinyin.Style.NORMAL, heteronym=True)
            for pinyin in product(*pinyin_list):
                pinyin = "".join(filter(is_not_empty, pinyin))
                if not pinyin.isalpha(): continue
                item = f"{char.strip()}\t{pinyin}"
                yaml.add(item)
    with open("build/chaizi.dict.yaml", "w") as f:
        f.write(HEADER + "\n".join(yaml))

if __name__ == "__main__":
    chai()
