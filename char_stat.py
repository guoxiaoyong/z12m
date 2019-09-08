import pathlib
import scipy.stats
import numpy as np
from collections import defaultdict

filename = 'enwik8'
path = pathlib.Path(filename)
text = path.read_text()
chars = sorted(set(text))

stats = defaultdict(int)
for c in text:
  stats[c] += 1

freq = np.array(sorted(list(stats.values())))
freq = freq / freq.sum()

total = scipy.stats.entropy(freq, base=2) * len(text)
print(total/1024/1024/8)
