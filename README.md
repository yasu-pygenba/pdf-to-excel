v1.0 pdfをexcelに変換

📦 必要環境

Python 3.9+

インストールが必要なライブラリ：

pip install pandas openpyxl tabula-py camelot-py pdf2image pytesseract

🚀 使い方

変換したい PDF を input.pdf として配置

以下のスクリプトを実行

python main.py


変換結果が output.xlsx として保存されます

📂 プロジェクト構成
project/
├── main.py        # メインの変換スクリプト
├── requirements.txt # 必要ライブラリ一覧
├── README.md      # このファイル
└── sample.pdf     # サンプルPDFや出力例


⚠️ 注意点

スキャンPDF（画像形式）の場合はOCR処理が必要です

表の罫線や列幅は完全には保持されません。必要に応じてExcel側で整形してください

📜 ライセンス

MIT License
