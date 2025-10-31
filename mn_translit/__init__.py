"""mn_translit package public API.

Exposes transliteration helpers and the main class. Package metadata such as
version is sourced from the installed distribution metadata to avoid
duplication with pyproject.toml.
"""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

from .translit import (
    MongolianTransliterator,
    cyrillic_to_latin,
    latin_to_cyrillic,
    number_to_words,
    transliterate,
    words_to_number,
)

try:  
    __version__ = _pkg_version("mn-translit")
except PackageNotFoundError:  
    __version__ = "0.0.0"

__all__ = [
    "latin_to_cyrillic",
    "cyrillic_to_latin",
    "transliterate",
    "number_to_words",
    "words_to_number",
    "MongolianTransliterator",
    "__version__",
]
