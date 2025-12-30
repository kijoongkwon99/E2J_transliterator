# converter.py
from .preprocess import PhonemePreprocessor
from .converter import (
    VowelConverter,
    ConsonantConverter,
    EpentheticVowelHandler,
    MoraeCreator,
    MoraeKanaConverter,
)


import re

PUNCT_RE = re.compile(r"^[^\w]+$")

class EngToJap:
    def __init__(self):
        self.phonemize_fn = PhonemePreprocessor().phonemizer
        self.vowel_fn = VowelConverter().convertVowel
        self.consonant_fn = ConsonantConverter().convertConsonant
        self.epenthetic_fn = EpentheticVowelHandler().addEpentheticVowel
        self.morae_fn = MoraeCreator().createMorae
        self.kana_fn = MoraeKanaConverter().convertMorae

    def ipa_word_to_kana(self, word: str, ipa: str) -> str:
        ipa = ipa.replace('.', '').replace(',','')

        print(f"word            :{word}")
        print(f"ipa             :{ipa}")
        ph1 = self.vowel_fn(word, ipa)
        print(f"vowel_fn        : {ph1}")
        ph2 = self.consonant_fn(word, ph1)
        print(f"consonant_fn    : {ph2}")
        ph3 = self.epenthetic_fn(ph2)
        print(f"epenthetic_fn   : {ph3}")
        mora = self.morae_fn(ph3)
        print(f"mora_fn         : {mora}")
        kana = self.kana_fn(mora)
        print(f"kana_fn         : {kana}\n")
        return kana
    
    def transliteration(self, text: str) -> str:
        ipa_sentence = self.phonemize_fn(text)
        ipa_words = ipa_sentence.split()

        text_tokens = text.split()  # punctuation 포함
        out = []

        ipa_idx = 0

        for token in text_tokens:
            # print("----------------------")
            # print(f"token: {token}")

            if PUNCT_RE.match(token):
                out.append(token)
                continue

            m = re.match(r"^(\w+)([^\w]+)$", token)
            if m:
                word, punct = m.group(1), m.group(2)
                ipa = ipa_words[ipa_idx]
                ipa_idx += 1

                kana = self.ipa_word_to_kana(word.lower(), ipa)
                out.append(kana + punct)
                continue

            ipa = ipa_words[ipa_idx]
            ipa_idx += 1

            out.append(self.ipa_word_to_kana(token.lower(), ipa))

        return " ".join(out)

def english_to_japanese(text: str) -> str:
    return EngToJap().transliteration(text)
