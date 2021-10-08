# wl-machine
重み付き抽選をしてくれるプログラム

以下のサンプル人名は[すごい名前生成器](https://namegen.jp/)で生成しています。

## 入力
以下の形式のCSVファイルを入力する
|choice|weight|
|---|---|
|金子 謙也 | 1 |
|松本 晃一 |1 |
|鈴木 和真 |1 |
|松田 啓介 |5 |
|藤原 裕一 |4 |
|石川 雅也 |3 |
|小島 雄太 |2 |
|天野 賢一 |1 |

抽選の設定ファイルを読み込む。
```ini
num = 3
overlap = 0 # 重複当選Okなら1,なしなら0
```

## 出力
以下の形式のCSVファイルを出力する。
|choice|weight|result|
|---|---|---|
|金子 謙也 | 1 | C |
|松本 晃一 |1 | |
|鈴木 和真 |1 | |
|松田 啓介 |5 | A |
|藤原 裕一 |4 | |
|石川 雅也 |3 | |
|小島 雄太 |2 | B |
|天野 賢一 |1 | |