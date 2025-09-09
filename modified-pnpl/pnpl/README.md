# 🍍PNPL Brain Data Deep Learning Library
Note: This package is a lightweight, modified build of the PNPL library (originally from the Neural Processing Lab, University of Oxford) that we adapted for word‑detection tasks. It adds `LibriBrainWord` for word‑level classification and keyword detection.

## Installation
```
pip install pnpl
```

This will also take care of all requirements.

## Usage
The core functionality of the library is contained in the three dataset classes `LibriBrainSpeech`, `LibriBrainPhoneme`, and `LibriBrainWord` (word‑level detection).
Check out the basic usage:

### LibriBrainSpeech
This wraps the LibriBrain dataset for use in speech detection problems.
```python
from pnpl.datasets import LibriBrainSpeech

speech_example_data = LibriBrainSpeech(
    data_path="./data/",
    include_run_keys = [("0","1","Sherlock1","1")]
)

sample_data, label = speech_example_data[0]

# Print out some basic info about the sample
print("Sample data shape:", sample_data.shape)
print("Label shape:", label.shape)
```

### LibriBrainPhoneme
This wraps the LibriBrain dataset for use in phoneme classification problems.
```python
from pnpl.datasets import LibriBrainPhoneme

phoneme_example_data = LibriBrainPhoneme(
    data_path="./data/",
    include_run_keys = [("0","1","Sherlock1","1")]
)

sample_data, label = phoneme_example_data[0]

# Print out some basic info about the sample
print("Sample data shape:", sample_data.shape)
print("Label shape:", label.shape)
```

### LibriBrainWord
This wraps the LibriBrain dataset for word classification and keyword detection.
```python
from pnpl.datasets import LibriBrainWord

word_data = LibriBrainWord(
    data_path="./data/",
    include_run_keys=[("0","1","Sherlock1","1")],
    keyword_detection="watson",  # optional: binary label for 'watson'
)

sample_data, label = word_data[0]
print("Sample data shape:", sample_data.shape)
print("Label:", int(label))
```
