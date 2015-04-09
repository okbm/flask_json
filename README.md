# python flask 練習用

# Description
- pythonの練習用リポジトリ
  - [httpbin(1): HTTP Client Testing Service](http://httpbin.org/)
    - flaskでできたシンプルなjsonを返すだけのサービス
  - これを自分で作ってみる(githubにコードはあるが見ない)

## install
- python3
  - brewで入れてもいいと思うけど、pyenv使って環境ごとに作りました
  - [macにvirtualenvでpython3いれる](https://gist.github.com/okbm/d4d7f0c6fd1fff3522d1)
- mysql
  - brew install mysql

### 1. Create Database Auth File
```sql
CREATE DATABASE flask_json DEFAULT character set=utf8;
CREATE USER 'flask_json'@localhost IDENTIFIED BY 'password'
GRANT ALL ON flask_json.* TO flask_json;

# dummy あとで消す
CREATE TABLE `user` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `created` datetime NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into user values (null,'test',now());
```

```bash
$ echo "flask_json:password" > ./flask_json/models/dbauth
```

### 2. Install Libraries
```bash
$ pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Create Tables
```bash
$ python flask/scripts/schema.py database
```

## RUN
```bash
$ python run.py
```

ブラウザでhttp://localhost:5000 を開く

## TODO
- [ ] precommitでテスト走らせる
- [ ] SQLAlchemy使ってcreate tableを走らせる
- [ ] WSGIで動かせるように
- [ ] fablicでデプロイする
- [ ] traviceCIとか使って回す

