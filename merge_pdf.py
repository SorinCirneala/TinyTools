from pypdf import PdfMerger

pdfs = ["input_1.pdf", "input_2.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
