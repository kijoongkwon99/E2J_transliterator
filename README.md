# eng2jap

A lightweight, rule-based English-to-Japanese pronunciation transliterator using phonemizer (IPA) with espeak-ng as the backend.

---

## Overview

**eng2jap** converts English words and full sentences into **approximate Japanese-style pronunciations** (katakana-oriented phonetic forms).

This project does **not rely on dictionary lookup**.  
Instead, it uses a **rule-based phoneme transformation pipeline**, allowing it to generate plausible Japanese pronunciations even for:

- Words not found in English dictionaries  
- Newly coined or informal spellings  
- Mixed or punctuation-containing sentences  

Internally, English text is first converted into IPA using **espeak-ng via the phonemizer library**, and then mapped into Japanese phonological structures.

---

## Features

- **Rule-based pronunciation transliteration**
- **No dictionary lookup**
  - Robust to out-of-vocabulary (OOV) words
  - Suitable for open-vocabulary scenarios
- Preserves punctuation and sentence structure
- Designed for stability and predictable behavior
- Lightweight and easy to integrate into other systems

---

## Requirements

- Python >= 3.11
- phonemizer >= 3.0.0

---

## Quick Start

### 1. Create a conda environment (recommended)

```bash
conda create -n eng2jap python=3.11
conda activate eng2jap
```

### 2. Install via pip from GitHub

```bash
pip install git+https://github.com/kijoongkwon99/E2J_transliterator.git
```

---

## Usage

### Basic Example

```python
from eng2jap import english_to_japanese

print(english_to_japanese("Hello, world!"))
```

Example output (approximate):

```text
ハロー, ウォルド!
```

---

## How to Use

```python
from eng2jap import english_to_japanese

print(
    english_to_japanese(
        "This module was designed to handle place names, personal names, and loanwords in TTS systems, such as Gangnam, Naruto, and Pytorch, while preserving punctuation."
    )
)

print(
    english_to_japanese(
        "To reduce additional training requirements and computational cost, the system is implemented using a rule-based approach instead of data-driven models."
    )
)

print(
    english_to_japanese(
        "English input is converted into Japanese-style pronunciation, and similar effects can be achieved for other languages by applying romanization beforehand."
    )
)

```

### Output Example

Example TTS outputs for the generated pronunciations are provided in the `example/` directory.

```text
ジス モジュール ワズ ディザインド ツー ハンダル プレイス ネインズ, ペサナル ネインズ, アンド ローンウォッズ イン ティーティーエス シスタンズ, サッチ アズ ギャングナム, ナールートー, アンド パイトーチ, ワイル プリゼビング パンクチューエイシャン.

ツー リッドゥース アッディッシャナル トレイニング リックァイアーマントス アンド コンピューテイシャナル コスト, ザ シスタム イズ インプリマンティッド ユージング エイ ルールベイスト アプローチ インステッド オブ デイタッドリバン モッダルズ.

イングリッシュ インプット イズ カンベティッド インツ ジャパニーズスタイル プラナンシエイシャン, アンド シミラー イフェックトス キャン ビー アッチーブド フォー オザー ラングィジズ バイ アプライーング ローマニゼイシャン ビフォルハンド.
```

---

## System Pipeline

```text
English
→ IPA (espeak-ng)
→ phoneme normalization
→ mora-based converting
→ Japanese pronunciation (katakana-style)
```

This design ensures **stable and consistent phonetic results**, even for previously unseen inputs.

---

## Notes

- This tool focuses on **pronunciation**, not semantic translation
- Output may differ from standard or officially adopted loanword spellings
- The system prioritizes **faithful reflection of English phonetics**
- Probably suitable for:
  - TTS preprocessing
  - Cross-lingual pronunciation transfer
  - Text normalization during speech model training

---

## License

MIT License
