from src.ingestor import LocalIngestor
from src.guardian import EdgeGuardian

# 1. Setup
ingestor = LocalIngestor()
guardian = EdgeGuardian()

# 2. Ingest
raw_text = ingestor.process_file("data/secret_contract.txt")
print(f"\n--- RAW TEXT ---\n{raw_text[:100]}...\n")

# 3. Sanitize
clean_text = guardian.sanitize(raw_text)
print(f"\n--- CLEAN TEXT (Safe for AI) ---\n{clean_text}")