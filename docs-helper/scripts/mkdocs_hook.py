"""MkDocs hook: regenerate docs/llms.txt before every build or live-reload rebuild."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_llms_txt


def on_pre_build(config, **kwargs):
    generate_llms_txt.main()
