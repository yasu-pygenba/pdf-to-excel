import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_path: str, excel_path: str):
    """
    PDFの表を読み込んでExcelに出力する関数
    """
    all_tables = []  # PDFから抽出した表を格納

    # PDFを開く
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                df["page"] = page_num  # ページ番号を追加
                all_tables.append(df)

    # すべてのページの表を結合
    if all_tables:
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df.to_excel(excel_path, index=False)
        print(f"✅ Excelに保存しました → {excel_path}")
    else:
        print("⚠️ PDF内に表が見つかりませんでした")


def main():
    input_pdf = 'sample.pdf'
    output_excel = 'output.xlsx'
    pdf_to_excel(input_pdf, output_excel)

# 実行例
if __name__ == "__main__":
    main()