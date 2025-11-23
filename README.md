## バレーボール分析アプリ

## 概要
このアプリは、バレーボールの試合データを個人ごとに入力・管理し、スパイクやサーブの成功率・効率・ミス率などを分析するための Web アプリです。

## 機能
- 試合データの入力（試合日、対戦相手、スパイク数、サーブ数、反省コメントなど）
- データの閲覧・編集・削除
- 選手ごとの分析結果表示（スパイク成功率・効率・被ブロック率、サーブ成功率・効率・ミス率）
- 削除時の確認ダイアログ

## 使用技術

Python 3.12.12
Flask 3.1.2
Flask-SQLAlchemy 3.1.1
SQLite 3.51.0
HTML / CSS
Bootstrap

## ファイル構成
webapp_vb
├── README.md
├── anly.py
├── instance
│   └── todo.db
├── requirements.txt
├── static
│   └── css
│       ├── bootstrap-grid.css
│       ├── bootstrap-grid.css.map
│       ├── bootstrap-grid.css.map:Zone.Identifier
│       ├── bootstrap-grid.css:Zone.Identifier
│       ├── bootstrap-grid.min.css
│       ├── bootstrap-grid.min.css.map
│       ├── bootstrap-grid.min.css.map:Zone.Identifier
│       ├── bootstrap-grid.min.css:Zone.Identifier
│       ├── bootstrap-grid.rtl.css
│       ├── bootstrap-grid.rtl.css.map
│       ├── bootstrap-grid.rtl.css.map:Zone.Identifier
│       ├── bootstrap-grid.rtl.css:Zone.Identifier
│       ├── bootstrap-grid.rtl.min.css
│       ├── bootstrap-grid.rtl.min.css.map
│       ├── bootstrap-grid.rtl.min.css.map:Zone.Identifier
│       ├── bootstrap-grid.rtl.min.css:Zone.Identifier
│       ├── bootstrap-reboot.css
│       ├── bootstrap-reboot.css.map
│       ├── bootstrap-reboot.css.map:Zone.Identifier
│       ├── bootstrap-reboot.css:Zone.Identifier
│       ├── bootstrap-reboot.min.css
│       ├── bootstrap-reboot.min.css.map
│       ├── bootstrap-reboot.min.css.map:Zone.Identifier
│       ├── bootstrap-reboot.min.css:Zone.Identifier
│       ├── bootstrap-reboot.rtl.css
│       ├── bootstrap-reboot.rtl.css.map
│       ├── bootstrap-reboot.rtl.css.map:Zone.Identifier
│       ├── bootstrap-reboot.rtl.css:Zone.Identifier
│       ├── bootstrap-reboot.rtl.min.css
│       ├── bootstrap-reboot.rtl.min.css.map
│       ├── bootstrap-reboot.rtl.min.css.map:Zone.Identifier
│       ├── bootstrap-reboot.rtl.min.css:Zone.Identifier
│       ├── bootstrap-utilities.css
│       ├── bootstrap-utilities.css.map
│       ├── bootstrap-utilities.css.map:Zone.Identifier
│       ├── bootstrap-utilities.css:Zone.Identifier
│       ├── bootstrap-utilities.min.css
│       ├── bootstrap-utilities.min.css.map
│       ├── bootstrap-utilities.min.css.map:Zone.Identifier
│       ├── bootstrap-utilities.min.css:Zone.Identifier
│       ├── bootstrap-utilities.rtl.css
│       ├── bootstrap-utilities.rtl.css.map
│       ├── bootstrap-utilities.rtl.css.map:Zone.Identifier
│       ├── bootstrap-utilities.rtl.css:Zone.Identifier
│       ├── bootstrap-utilities.rtl.min.css
│       ├── bootstrap-utilities.rtl.min.css.map
│       ├── bootstrap-utilities.rtl.min.css.map:Zone.Identifier
│       ├── bootstrap-utilities.rtl.min.css:Zone.Identifier
│       ├── bootstrap.css
│       ├── bootstrap.css.map
│       ├── bootstrap.css.map:Zone.Identifier
│       ├── bootstrap.css:Zone.Identifier
│       ├── bootstrap.min.css
│       ├── bootstrap.min.css.map
│       ├── bootstrap.min.css.map:Zone.Identifier
│       ├── bootstrap.min.css:Zone.Identifier
│       ├── bootstrap.rtl.css
│       ├── bootstrap.rtl.css.map
│       ├── bootstrap.rtl.css.map:Zone.Identifier
│       ├── bootstrap.rtl.css:Zone.Identifier
│       ├── bootstrap.rtl.min.css
│       ├── bootstrap.rtl.min.css.map
│       ├── bootstrap.rtl.min.css.map:Zone.Identifier
│       └── bootstrap.rtl.min.css:Zone.Identifier
└── templates
    ├── analyze.html
    ├── base.html
    ├── index.html
    ├── reflect.html
    ├── update.html
    └── write.html
## 起動方法
pip install -r requirements.txt
python anly.py

## webアプリの画像
<img width="1387" height="910" alt="スクリーンショット 2025-11-21 151228" src="https://github.com/user-attachments/assets/f4b7abf6-8286-46bf-98a1-92849fa55efa" />
<img width="1014" height="833" alt="スクリーンショット 2025-11-21 151237" src="https://github.com/user-attachments/assets/66be0efd-4f3d-415d-a268-57f4420cf52f" />
<img width="1358" height="885" alt="スクリーンショット 2025-11-21 151255" src="https://github.com/user-attachments/assets/9c57169d-1bc9-42cf-ac7d-bfe1ee068860" />
<img width="703" height="658" alt="スクリーンショット 2025-11-21 151304" src="https://github.com/user-attachments/assets/936f51fe-8728-44d4-a30b-820366b58b06" />
<img width="1258" height="833" alt="スクリーンショット 2025-11-21 151315" src="https://github.com/user-attachments/assets/e7b9aab1-ccdb-4a43-b7b6-45cf88f259e5" />
<img width="797" height="289" alt="スクリーンショット 2025-11-21 151320" src="https://github.com/user-attachments/assets/aee6e9d0-037b-4ba1-9b1c-2052a95041cb" />









    
