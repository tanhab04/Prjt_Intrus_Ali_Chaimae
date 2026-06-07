import os
import json
import numpy as np
import tqdm

DATA_DIR = r"C:\PFA_Malware\data\raw\ember2018"

train_files = [
    os.path.join(DATA_DIR, f"train_features_{i}.jsonl")
    for i in range(6)
]

# Compter les lignes totales
print("Comptage des lignes...")
nrows = 0
for f in train_files:
    with open(f, "r") as fh:
        nrows += sum(1 for _ in fh)
print(f"  → {nrows} samples trouvés")

# Recréer y_train.dat
y_train_path = os.path.join(DATA_DIR, "y_train.dat")
y_train = np.memmap(y_train_path, dtype=np.float32, mode="w+", shape=(nrows,))

print("Lecture des labels...")
idx = 0
for fpath in train_files:
    print(f"  Traitement {os.path.basename(fpath)}...")
    with open(fpath, "r") as fh:
        for line in tqdm.tqdm(fh):
            try:
                raw = json.loads(line)
                y_train[idx] = raw.get("label", -1)
            except:
                y_train[idx] = -1
            idx += 1

y_train.flush()
print(f"\nTerminé ! Distribution des labels :")
unique, counts = np.unique(np.array(y_train), return_counts=True)
for u, c in zip(unique, counts):
    print(f"  label {u:.0f} : {c} samples")