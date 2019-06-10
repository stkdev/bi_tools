# ゆるめの分析環境作り

**まだ作り中です** 

## 初回セットアップ

[前提] docker, docker-composeインストール済み

```
# ここのリポジトリ
git clone https://github.com/stkdev/bi_tools.git
cd bi_tolls

# バックグランド実行
docker-compose up -d

# redashのDB初期セットアップ
docker-compose run --rm server create_db
docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"
```

- redash
    - [localhost:5000](localhost:5000)
- jupyter Lab
    - [localhost:8888](localhost:8888)


## 入れたいツール
ひとまず
- JupyterLab
- redash 


動いて欲しいフレームワーク
- Shiny (R)
- Dash (Python)

## 参考資料色々
### redash関連

- [Docker Based Developer Installation Guide](https://redash.io/help/open-source/dev-guide/docker)
- [DockerHub redash](https://hub.docker.com/r/redash/redash)
- [GitHub docker-compose.yml サンプル](https://github.com/getredash/redash/blob/master/setup/docker-compose.yml)

### JupyterLab

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
- [DockerHub jupyter](https://hub.docker.com/r/jupyter/datascience-notebook/)

### 他

- [plotly | Dash](https://plot.ly/products/dash/)
- [Shiny from R Studio](https://shiny.rstudio.com/)


