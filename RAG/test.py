from loader import load_pdf
from chunk_service import split_text


text = load_pdf(r"C:\Users\malar\Downloads\Resume.pdf")

chunks = split_text(text)

print(f"\nTotal Chunks : {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"--------------- Chunk {i+1} ---------------")
    print(chunk)
    print()