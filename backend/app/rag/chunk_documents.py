from pathlib import Path
from typing import List, Dict
import re

KNOWLEDGE_BASE_DIR = (
    Path(__file__).resolve()
    .parents[3]
    / "knowledge-base"
)
def get_markdown_files() -> List[Path]:
    """
    Returns all markdown files inside the knowledge-base directory.
    """

    return sorted(KNOWLEDGE_BASE_DIR.rglob("*.md"))
def read_markdown_file(file_path: Path) -> str:
    """
    Reads a markdown file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def split_into_sections(content: str):
    """
    Splits markdown into sections using ## headings.
    """

    pattern = r"^##\s+(.*)$"

    matches = list(
        re.finditer(
            pattern,
            content,
            flags=re.MULTILINE,
        )
    )

    sections = []

    for i, match in enumerate(matches):

        section_name = match.group(1).strip()

        start = match.end()

        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(content)
        )

        section_content = content[start:end].strip()

        sections.append(
            {
                "section": section_name,
                "content": section_content,
            }
        )

    return sections
def chunk_markdown_file(file_path: Path) -> List[Dict]:
    """
    Converts one markdown document into chunks.
    """

    markdown = read_markdown_file(file_path)

    sections = split_into_sections(markdown)

    chunks = []

    for section in sections:

        chunks.append(
            {
                "document_name": file_path.name,
                "section_name": section["section"],
                "content": section["content"],
            }
        )

    return chunks
def chunk_knowledge_base() -> List[Dict]:
    """
    Reads every markdown file and creates chunks.
    """

    all_chunks = []

    for markdown_file in get_markdown_files():

        chunks = chunk_markdown_file(markdown_file)

        all_chunks.extend(chunks)

    return all_chunks
if __name__ == "__main__":

    chunks = chunk_knowledge_base()

    print(f"Total Chunks: {len(chunks)}")

    print()

    for chunk in chunks[:10]:

        print("=" * 80)

        print("Document :", chunk["document_name"])

        print("Section  :", chunk["section_name"])

        print()

        print(chunk["content"][:250])

        print()