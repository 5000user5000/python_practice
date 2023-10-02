from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["total.pdf", "rank.pdf"]:
    merger.append(pdf)

merger.write("final.pdf") # 合併後的檔案名稱
merger.close()
