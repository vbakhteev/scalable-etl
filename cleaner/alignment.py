import os
import sys
from pathlib import Path
from typing import List

import numpy as np

if 'LASER' not in os.environ:
    os.environ['LASER'] = '/project/LASER'

LASER = Path(os.environ['LASER'])
sys.path.append(str(LASER / 'source'))

from embed import SentenceEncoder

COS_THRESHOLD = 0.5

ENCODER_PATH = str(LASER / 'models' / 'bilstm.93langs.2018-12-26.pt')
ENCODER = SentenceEncoder(
    ENCODER_PATH,
    max_sentences=None,
    max_tokens=12000,
    sort_kind='mergesort',
    cpu=True,
)


def encode_text(texts: List[str], encoder):
    embs = encoder.encode_sentences(texts)
    return embs


def are_texts_aligned(text1: str, text2: str) -> bool:
    embs = encode_text([text1, text1], ENCODER)
    cos = cos_sim(embs[0], embs[1])
    return cos > COS_THRESHOLD


def cos_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


if __name__ == '__main__':
    emb = encode_text(['hello there'], ENCODER)[0]
    print(emb)
