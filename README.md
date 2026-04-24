# Prompt DB (Django)

画像生成用・LP作成用など、用途別にプロンプトを保存/検索できる Django Web アプリです。  
Python + Django で構築し、Render にデプロイできる構成になっています。

---

## 0. 最短でローカル実行する（コピペ用）

```bash
git clone <your-repo-url>
cd prompt-db
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY='dev-secret-key'
export DEBUG='True'
export ALLOWED_HOSTS='127.0.0.1,localhost'
python manage.py migrate
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` を開けば動作確認できます。  
管理画面を使う場合は、別途 `python manage.py createsuperuser` を実行してください。

---

## 1. できること

- プロンプト登録（タイトル / 用途 / 本文 / タグ / メモ）
- 一覧表示
- キーワード検索（タイトル・用途・タグ・本文）
- 詳細表示
- Django Admin からカテゴリ管理

---

## 2. ローカル環境セットアップ（開発用）

> 前提: Python 3.10 以上 / Git

### 2-1. プロジェクト取得

```bash
git clone <your-repo-url>
cd prompt-db
```

### 2-2. 仮想環境作成と有効化

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2-3. 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

### 2-4. 環境変数を設定（任意だが推奨）

`.env.example` を参考に環境変数を設定してください。

最低限以下を設定すると安全です。

```bash
export SECRET_KEY='your-secret-key'
export DEBUG='True'
export ALLOWED_HOSTS='127.0.0.1,localhost'
```

### 2-5. DBマイグレーション

```bash
python manage.py migrate
```

### 2-6. 管理ユーザー作成（任意）

```bash
python manage.py createsuperuser
```

### 2-7. 開発サーバー起動

```bash
python manage.py runserver
```

アクセス:

- アプリ: http://127.0.0.1:8000/
- 管理画面: http://127.0.0.1:8000/admin/

---

## 3. Render へアップロード（デプロイ）する方法

このリポジトリには `render.yaml` があるため、**Blueprint デプロイ**が最短です。

### 3-1. 事前準備

1. GitHub/GitLab にこのリポジトリを push
2. Render アカウントを作成

### 3-2. Blueprint でデプロイ

1. Render ダッシュボードで **New +** → **Blueprint**
2. 対象リポジトリを選択
3. `render.yaml` を Render が読み取り、以下を自動作成
   - Web Service (`prompt-db`)
   - PostgreSQL (`prompt-db-postgres`)
4. **Apply** で作成開始

### 3-3. Render 側の環境変数

`render.yaml` 内で次が設定されます。

- `PYTHON_VERSION=3.12.2`
- `SECRET_KEY`（自動生成）
- `DEBUG=False`
- `ALLOWED_HOSTS=prompt-db.onrender.com`（必要なら自分のサービスURLに変更）
- `DATABASE_URL`（PostgreSQL 接続文字列を自動注入）

### 3-4. Build / Start の中身

- Build: `./build.sh`
  - `pip install -r requirements.txt`
  - `python manage.py collectstatic --no-input`
  - `python manage.py migrate`
- Start: `gunicorn promptdb.wsgi:application`

### 3-5. デプロイ後の確認

1. Render の Web Service URL にアクセス
2. 500 エラー時は Logs を確認
3. 必要に応じて Shell で管理ユーザー作成

```bash
python manage.py createsuperuser
```

---

## 4. 運用時の注意

- 本番では `DEBUG=False` を維持
- `ALLOWED_HOSTS` は実際のドメインに合わせる
- DB変更時は必ず migration をコミット
- Render Free プランはスリープするため、初回アクセス時に起動待ちが発生します

---

## 5. よく使うコマンド

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --no-input
```
