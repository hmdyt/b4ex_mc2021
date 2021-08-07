# b4ex_mc2021
特別講義 物性理論特論 A 2021 課題提出用

## 概要
ねこの名前が出てくるガチャ。

## 使い方
```bash
git clone https://github.com/hmdyt/b4ex_mc2021.git
```
```bash
cd b4ex_mc2021
```
```bash
python main.py
```

## 解説
### 確率モデルの定義について
- [neko.json](https://github.com/hmdyt/b4ex_mc2021/blob/main/neko.json)に全状態集合とそれぞれに対応する相対重みを定義している。
- 定義された相対重みから規格化定数を計算し, 累積重みを計算した([main.py](https://github.com/hmdyt/b4ex_mc2021/blob/main/main.py) 内の関数 calc_accum_weights)。
### 使用した疑似乱数
python 3.9.5の標準ライブラリrandom.random()を用いた。この関数はメルセンヌツイスタによって実装されている([公式ドキュメント](https://docs.python.org/ja/3/library/random.html))。