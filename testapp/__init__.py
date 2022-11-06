# 実行後、一番最初に実行する(コンストラクタみたいな)ファイルなので
# WEBアプリ全体に使用したい設定を作ると便利
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask構成開始
app = Flask(__name__)

# 設定ファイル
app.config.from_object('testapp.config')

# モジュールを導入
from testapp.test import test_module
app.register_blueprint(test_module)
from testapp.janken import janken_module
app.register_blueprint(janken_module)

# sqlite
db = SQLAlchemy(app)
from .models import employee
import os;
if os.path.exists('./instance/sample_flask.db') == False:
    with app.app_context():
        db.drop_all()
        db.create_all()

# views.pyの内容を読み込み(ホームページ)
import testapp.views