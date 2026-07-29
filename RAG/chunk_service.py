from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)


def split_text(text: str) -> list[str]:
    """
    Split a large text into smaller overlapping chunks.

    Args:
        text (str): Extracted text from the PDF.

    Returns:
        list[str]: List of text chunks.
    """

    chunks = text_splitter.split_text(text)

    return chunks