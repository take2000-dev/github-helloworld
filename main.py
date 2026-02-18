from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # 1. GASの console.log のように手軽に使う print（もっとも一般的）
    print("Log: print function was called!") 

    # 2. プロの現場で使われる logging（情報のレベルを指定できる）
    app.logger.info("Info: 正常なアクセスを記録しました。")
    app.logger.warning("Warning: 何か注意が必要な状態です。")
    app.logger.error("Error: エラーが発生しました！（シミュレーション）")
    
    # 3. デバッグ時だけ詳細に出したい情報
    app.logger.debug("Debug: 開発者にしか見せたくない詳細データ")
    return 'Hello from Cloud Shell Editor!!!'

if __name__ == '__main__':
    app.run()
