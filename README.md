## バレーボール分析アプリ

## 概要
このアプリは、バレーボールの試合データを個人ごとに入力・管理し、スパイクやサーブの成功率・効率・ミス率などを分析するための Web アプリです。

## 機能
- 試合データの入力（試合日、対戦相手、スパイク数、サーブ数、反省コメントなど）
- データの閲覧・編集・削除
- 選手ごとの分析結果表示（スパイク成功率・効率・被ブロック率、サーブ成功率・効率・ミス率）
- 削除時の確認ダイアログ

## 使用技術
Python 3
Flask
Flask-SQLAlchemy
SQLite
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



    
