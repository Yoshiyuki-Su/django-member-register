# Djangoで会員登録機能のあるWebアプリケーション

## 仮想環境の作り方
```
mkdir django-member-register
cd django-member-register
D:\source\Python\Django_samples\django-member-register>python -m venv myvenv
```


## 仮想環境を起動
```
myvenv\Scripts\activate
```

## requirementsファイルによってパッケージをインストールする
```
pip install -r requirements.txt
```

## プロジェクトの作成
```
django-admin startproject MemberRegister .
```

## データベースをセットアップする
```
python manage.py migrate
```

## ウェブサーバを起動する
```
python manage.py runserver
```

# 新しいアプリケーションの作成
```
python manage.py startapp account
```

## データベースにモデルのためのテーブルを作成する
```
python manage.py makemigrations blog

python manage.py migrate blog
```

## superuser （サイトの全てを管理するユーザー）の作成
```
python manage.py createsuperuser
```

## 参考：
> https://blog.narito.ninja/detail/38/
