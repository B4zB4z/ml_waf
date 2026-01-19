import re
import math
import json

SQL_KEYWORDS = [
    "select", "union", "insert", "drop", "update",
    "delete", "or", "and", "--", "'"
]

XSS_KEYWORDS = [
    "<script", "javascript", "onerror", "<img", "<svg"
]

def entropy(text):
    if not text:
        return 0.0
    probs = [text.count(c) / len(text) for c in set(text)]
    return -sum(p * math.log2(p) for p in probs)

def flatten_request(req):
    """
    Convert structured HTTP request into a single text string
    """
    parts = [
        req.get("method", ""),
        req.get("url", ""),
        json.dumps(req.get("headers", {})),
        str(req.get("dataset", ""))
    ]
    return " ".join(parts).lower()

def extract_features_from_json(req):
    text = flatten_request(req)

    return [
        len(text),
        sum(c in "'\";()<>" for c in text),
        sum(k in text for k in SQL_KEYWORDS),
        sum(k in text for k in XSS_KEYWORDS),
        entropy(text),
        sum(c.isdigit() for c in text),
        text.count("%"),          # URL encoding
        text.count("../"),        # path traversal
    ]
