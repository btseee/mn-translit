# mn-translit

Mongolian Latin-Cyrillic transliteration following MNS 5217:2012 standard with proper Mongolian number grammar.

## Python Version Support

- Python 3.8+

## Installation

```bash
pip install mn-translit
```

Or install from source:

```bash
git clone https://github.com/btseee/mn-translit.git
cd mn-translit
pip install -e .
```

## Usage

### Text Transliteration

```python
from mn_translit import latin_to_cyrillic, cyrillic_to_latin

# Latin to Cyrillic
print(latin_to_cyrillic("Sain baina uu?"))
# Output: Сайн байна уу?

# With automatic number conversion (digits → words)
print(latin_to_cyrillic("Bi 21 nom baina", trans_num=True))
# Output: Би хорин нэг ном байна

# Cyrillic to Latin
print(cyrillic_to_latin("Монгол"))
# Output: Mongol
```

### Command-line

Install and use the CLI directly:

```bash
echo "Sain baina uu?" | mn-translit --direction cyrillic
# → Сайн байна уу?

echo "Монгол" | mn-translit --direction latin
# → Mongol

echo "Bi 2024 ond" | mn-translit --direction cyrillic --trans-num
# → Би хоёр мянга хорин дөрвөн онд
```

### Number Conversion

```python
from mn_translit import number_to_words, words_to_number

# Number to words (proper Mongolian grammar)
print(number_to_words(21))
# Output: хорин нэг

print(number_to_words(111))
# Output: зуун арав нэг

print(number_to_words(230))
# Output: хоёр зуун гучин

print(number_to_words(2024))
# Output: хоёр мянга хорин дөрөв

# Words to number
print(words_to_number("мянга"))
# Output: 1000

print(words_to_number("хорин нэг"))
# Output: 21

print(words_to_number("хоёр зуун гучин"))
# Output: 230
```

## Character Mapping

### Basic Mapping

| Latin | Cyrillic | Latin | Cyrillic |
|-------|----------|-------|----------|
| a     | а        | n     | н        |
| e     | э        | o     | о        |
| i     | и        | u     | у        |
| ö     | ө        | ü     | ү        |

### Digraphs

| Latin | Cyrillic | Latin | Cyrillic |
|-------|----------|-------|----------|
| kh    | х        | ts    | ц        |
| ch    | ч        | sh    | ш        |
| zh    | ж        | ya    | я        |
| ye    | е        | yo    | ё        |
| yu    | ю        |       |          |

### Diphthongs

| Latin | Cyrillic | Example |
|-------|----------|---------|
| ai    | ай       | sainai → сайнай |
| ei    | эй       | erdei → эрдэй |
| ii    | ий       | kharii → харий |
| oi    | ой       | oilgokh → ойлгох |

## Number System

### Major Scales

- 100 → зуун
- 1,000 → мянга
- 10,000 → түм
- 100,000 → бум
- 1,000,000 → сая
- 1,000,000,000 → тэрбум
- 1,000,000,000,000 → их наяд

### Examples

- 21 → хорин нэг
- 31 → гучин нэг
- 41 → дөчин нэг
- 51 → тавин нэг
- 61 → жаран нэг
- 71 → далан нэг
- 81 → наян нэг
- 91 → ерэн нэг
- 111 → зуун арав нэг
- 230 → хоёр зуун гучин

## Testing

Run the test suite to verify all functionality:

```bash
python tests/test_translit.py
```

## Development

### Setting up for development

```bash
git clone https://github.com/btseee/mn-translit.git
cd mn-translit
pip install -e .
```

### Running tests

```bash
python tests/test_translit.py
```

### Publishing to PyPI

This package uses GitHub Actions for automated publishing. To publish a new version:

1. Update version in `mn_translit/__init__.py`
2. Create a new release on GitHub
3. The GitHub Action will automatically run tests and publish to PyPI

**Note:** You need to set up `PYPI_API_TOKEN` secret in your GitHub repository settings.

## License

MIT License
