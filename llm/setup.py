#!/usr/bin/env python3
"""
Run this once after cloning to set up the LLM:
    python llm/setup.py

Downloads Qwen2.5-0.5B-Instruct (~350 MB) and installs llama-cpp-python.
The model is stored in llm/models/ and gitignored (too large for git).
"""
import subprocess
import sys
import urllib.request
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "models"
MODEL_NAME = "qwen2.5-0.5b-instruct-q4_k_m.gguf"
MODEL_PATH = MODEL_DIR / MODEL_NAME
MODEL_URL = (
    "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/"
    + MODEL_NAME
)


def _reporthook(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        pct = min(100.0, downloaded * 100.0 / total_size)
        mb_done = downloaded / 1_000_000
        mb_total = total_size / 1_000_000
        print(f"\r  {pct:5.1f}%  {mb_done:.0f} / {mb_total:.0f} MB", end="", flush=True)


def main():
    print("=== Typewriter LLM Setup ===\n")

    print("Installing llama-cpp-python...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "llama-cpp-python"])
    print()

    MODEL_DIR.mkdir(exist_ok=True)
    if MODEL_PATH.exists():
        print(f"Model already present: {MODEL_PATH}")
    else:
        print(f"Downloading {MODEL_NAME} (~350 MB)...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH, _reporthook)
        print(f"\nSaved to {MODEL_PATH}")

    print("\nSetup complete!")
    print("Usage in your Python file:")
    print("    from llm.generate import generate_sentence")
    print('    sentence = generate_sentence("english")')
    print('    sentence = generate_sentence("german")')


if __name__ == "__main__":
    main()
