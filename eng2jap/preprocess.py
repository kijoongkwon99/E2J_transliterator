# preprocessing.py

from phonemizer import phonemize


class PhonemePreprocessor:
    def __init__(
        self,
        language: str = "en-us", 
        backend: str = "espeak",
        puncts: str = "-.,:;?!()\"' ",
        ipa_replace_map: dict | None = None,
    ):
        self.language = language
        self.backend = backend
        self.PUNCTS = set(puncts)

        self.ipa_replace_map = ipa_replace_map or {
            "dʒ": "ʤ",
            "tʃ": "ʧ",
            "ᵻ": "ɪ",
            "ɐ": "ʌ",
            "ː": "",
            "ɡ": "g",
            "ɾ": "t",
            "ʑ": "z",
            "ɯ": "u",
            "q": "k",
            "ɫ": "l",
            "tɕ": "j",
            "ɜ": "ʌ"
        }

    # -------------------------
    # IPA normalization
    # -------------------------
    def normalize_ipa(self, ph: str) -> str:
        if not ph:
            return ph

        for src in sorted(self.ipa_replace_map, key=len, reverse=True):
            ph = ph.replace(src, self.ipa_replace_map[src])

        return ph

    # -------------------------
    # Tokenization
    # -------------------------
    def split_with_punct(self, text: str):
        tokens = []
        i = 0
        n = len(text)

        while i < n:
            ch = text[i]

            if ch == '-':
                i += 1
                continue
            if ch in self.PUNCTS:
                tokens.append((None, ch))
                i += 1
                continue

            j = i
            while j < n and text[j] not in self.PUNCTS:
                j += 1

            tokens.append((text[i:j], None))
            i = j

        return tokens

    # -------------------------
    # Main pipeline
    # -------------------------
    def phonemizer(self, text: str) -> str:
        tokens = self.split_with_punct(text)

        words = []
        for word, punct in tokens:
            if word is not None:
                words.append(word.lower())

        ipa_words = phonemize(
            words,
            language=self.language,
            backend=self.backend,
            strip=True,
        )

        processed = [None] * len(tokens)
        w_idx = 0

        for i, (word, punct) in enumerate(tokens):
            if punct is not None:
                processed[i] = punct
            else:
                processed[i] = ipa_words[w_idx]
                w_idx += 1

        result = []
        for item in processed:
            if item in self.PUNCTS:
                if result:
                    result[-1] += item
                else:
                    result.append(item)
            else:
                result.append(item)

        out = "".join(result)
        out = self.normalize_ipa(out)

        return out

def preprocess(text: str) -> str:
    return PhonemePreprocessor().phonemizer(text)


if __name__ == "__main__":
    text = "While substantial advances have been achieved in TTS for languages such as English and Mandarin, Korean remains comparatively underrepresented due to the lack of rigorous preprocessing methods, systematically constructed datasets, a shortage of standardized Korean TTS benchmarks, and explicitly optimized models for Korean. To address these limitations, we propose a Korean-tailored data-refinement and coreset selection pipeline."
    text = "Jejudo"
    print(text)
    print(preprocess(text))