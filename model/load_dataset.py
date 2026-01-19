import os
import json
from waf.feature_extraction import extract_features_from_json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

def load_folder(subfolder, label):
    X, y = [], []
    folder_path = os.path.join(DATASET_DIR, subfolder)

    for file in os.listdir(folder_path):
        if not file.endswith(".json"):
            continue

        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            requests = json.load(f)

        for req in requests:
            X.append(extract_features_from_json(req))
            y.append(label)

    return X, y
