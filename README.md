## Open Resources: Code, Tutorial, and Leaderboard

Note: For the sake of anonymity during review, this package consolidates the modified code, tutorial, and experiment materials. The open-source release will follow after the review process at which point this archive will be obsolete.

### Modified pnpl library

We provide a modified version of the open-source `pnpl` library (original: `https://github.com/neural-processing-lab/frozen-pnpl`) to support word-level tasks. The implementation is located in `modified-pnpl/` and enables full signal-to-word as well as single- and multi-keyword detection with similar ergonomics to the existing `LibriBrainSpeech` and `LibriBrainPhoneme` datasets.

#### Word‑level task

```python
from pnpl.datasets import LibriBrainWord

dataset = LibriBrainWord(
    data_path="./data/",
    partition="train",
    tmin=0.0,
    tmax=0.8,
)
```

#### Single‑keyword task

```python
from pnpl.datasets import LibriBrainWord

dataset = LibriBrainWord(
    data_path="./data/",
    partition="train",
    keyword_detection="watson",
)
```

#### Multi‑keyword task

```python
from pnpl.datasets import LibriBrainWord

dataset = LibriBrainWord(
    data_path="./data/",
    partition="train",
    keyword_detection=["sherlock", "holmes"],
)
```

#### Notes

- For single/multi‑keyword detection, sample length is inferred from the longest keyword duration and can be extended with `positive_buffer` and `negative_buffer`. You may override with `tmin`/`tmax` if desired.
- For full signal‑to‑word, `tmin`/`tmax` overrides are disabled by default and a reasonable window is used instead.
- The `keyword_detection` variant validates that the specified keyword(s) exist in the dataset. If not, it defaults to using sessions with the highest prevalence as validation and test sets. The signal‑to‑word variant uses the default validation/test splits.

### Tutorial notebook

The tutorial (in `tutorial/`) is a Colab‑friendly Jupyter Notebook. Within Colab Free Tier constraints (T4 GPU), it trains on ~10% of LibriBrain and achieves clearly above‑chance performance in under one hour.

### Experiment code

To support full reproducibility, the code used for experiments and analysis is provided in `experiments/`.

