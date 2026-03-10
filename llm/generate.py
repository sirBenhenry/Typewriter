"""
LLM sentence generator for Typewriter.

Usage:
    from llm.generate import generate_sentence, load_model

    load_model()  # optional — call at startup to pre-load (avoids delay on first sentence)

    sentence = generate_sentence("english")
    sentence = generate_sentence("german")

Supported language values: "english", "en", "german", "de", "deutsch"
"""
import os
import random
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "models" / "qwen2.5-0.5b-instruct-q4_k_m.gguf"

_llm = None


def load_model():
    """Pre-load the model. Call this at app startup to avoid delay on first generate call."""
    global _llm
    if _llm is not None:
        return
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}\n"
            "Run setup first:  python llm/setup.py"
        )
    from llama_cpp import Llama

    _llm = Llama(
        model_path=str(MODEL_PATH),
        n_ctx=256,
        n_threads=os.cpu_count() or 4,
        verbose=False,
        seed=random.randint(0, 2**31),
    )


def generate_sentence(language: str = "english") -> str:
    """
    Generate one short nonsense sentence in the given language.

    Args:
        language: "english"/"en" or "german"/"de"/"deutsch"

    Returns:
        A sentence string (no trailing newline).
    """
    load_model()

    lang = language.lower().strip()
    if lang in ("german", "de", "deutsch"):
        prompt = (
            "Schreibe genau einen sinnlosen deutschen Satz mit 8 bis 12 Wörtern. "
            "Nur den Satz, nichts anderes:\n"
        )
    else:
        prompt = (
            "Write exactly one nonsense sentence in English, 8 to 12 words long. "
            "Only output the sentence, nothing else:\n"
        )

    result = _llm(
        prompt,
        max_tokens=40,
        stop=["\n", "\r", "."],
        echo=False,
        temperature=1.0,
        repeat_penalty=1.1,
    )
    text = result["choices"][0]["text"].strip()
    if text and not text.endswith("."):
        text += "."
    return text
