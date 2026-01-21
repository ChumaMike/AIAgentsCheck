import sys
from pathlib import Path
from docling.document_converter import DocumentConverter

class LocalIngestor:
    def __init__(self):
        print("🔧 Initializing Local Docling Converter...")
        self.converter = DocumentConverter()

    def process_file(self, file_path: str) -> str:
        """
        Reads a file (PDF, TXT, MD) and converts it to clean Markdown.
        """
        path = Path(file_path)
        if not path.exists():
            return f"❌ Error: File not found at {file_path}"

        print(f"📄 Digesting file: {path.name}...")
        
        # The Magic: Docling converts ANYTHING to standardized Markdown
        result = self.converter.convert(path)
        markdown_text = result.document.export_to_markdown()
        
        return markdown_text

if __name__ == "__main__":
    # Quick test when running this file directly
    ingestor = LocalIngestor()
    print("✅ Ingestor Ready.")