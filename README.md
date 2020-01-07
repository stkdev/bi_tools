# ゆるめの分析環境作り

**まだ作り中です** 

## 概要
個人or少人数チームで使う想定の分析ツール群です。

- データの蓄積にMySQL 8
- データの確認・集計・可視化・ダッシュボード作成に[superset](https://superset.apache.org/)
- プログラミングにjupyterLab

## 初回セットアップ

[前提] docker, docker-composeインストール済み

```
# ここのリポジトリ
git clone https://github.com/stkdev/bi_tools.git
cd bi_tolls

# 設定ファイル作成と記述
cp superset/.env.example superset/.env

# バックグランド実行
docker-compose up -d

# 初期設定
docker-compose run --rm superset /bin/bash -c 'source ./init.sh'
```

- superset
    - [localhost:7077](http://localhost:7077)
- jupyter Lab
    - [localhost:7777](http://localhost:7777)



