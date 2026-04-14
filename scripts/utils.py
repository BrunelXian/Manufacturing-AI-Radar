import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List


ARXIV_QUERY_LIST = [
    {
        "label": "additive manufacturing machine learning",
        "query": 'all:"additive manufacturing" AND all:"machine learning"',
    },
    {
        "label": "LPBF machine learning",
        "query": '(all:"LPBF" OR all:"laser powder bed fusion") AND all:"machine learning"',
    },
    {
        "label": "LDED machine learning",
        "query": '(all:"LDED" OR all:"directed energy deposition") AND all:"machine learning"',
    },
    {
        "label": "welding machine learning",
        "query": 'all:"welding" AND all:"machine learning"',
    },
    {
        "label": "manufacturing reinforcement learning",
        "query": 'all:"manufacturing" AND all:"reinforcement learning"',
    },
    {
        "label": "process monitoring machine learning",
        "query": 'all:"process monitoring" AND all:"machine learning"',
    },
    {
        "label": "digital twin manufacturing AI",
        "query": 'all:"digital twin" AND all:"manufacturing"',
    },
    {
        "label": "defect detection manufacturing deep learning",
        "query": 'all:"defect detection" AND all:"manufacturing"',
    },
]

MANUFACTURING_TERMS = [
    "manufacturing",
    "additive manufacturing",
    "laser powder bed fusion",
    "lpbf",
    "directed energy deposition",
    "ded",
    "lded",
    "waam",
    "wire-arc",
    "welding",
    "machining",
    "melt pool",
    "process monitoring",
    "production",
    "industrial process",
    "shop floor",
    "quality control",
    "nondestructive evaluation",
    "assembly",
    "robotic assembly",
    "job shop",
    "flexible job shop",
]

PROCESS_PRIORITY_TERMS = [
    "melt pool",
    "thermal field",
    "thermal history",
    "microstructure",
    "porosity",
    "lack-of-fusion",
    "defect",
    "monitoring",
    "control",
    "surrogate",
    "process parameter",
]

AI_METHOD_TERMS = [
    "machine learning",
    "deep learning",
    "reinforcement learning",
    "physics-informed",
    "graph neural",
    "neural network",
    "transformer",
    "surrogate",
    "operator learning",
    "model predictive control",
    "anomaly detection",
    "computer vision",
    "multimodal",
    "hyperdimensional",
]

EXCLUSION_TERMS = [
    "tourism",
    "cultural heritage",
    "general survey",
    "electronic design automation",
    "large language models generate harmful content",
    "prompt learning",
    "activity prediction",
]

DOMAIN_TAG_RULES = {
    "additive-manufacturing": [
        "additive manufacturing",
        "lpbf",
        "laser powder bed fusion",
        "ded",
        "lded",
        "directed energy deposition",
        "waam",
        "wire-arc",
        "3d printing",
    ],
    "monitoring": [
        "monitoring",
        "soft sensor",
        "state estimation",
        "anomaly detection",
        "fault detection",
    ],
    "defect-detection": [
        "defect",
        "porosity",
        "crack",
        "lack-of-fusion",
        "inspection",
        "surface defect",
        "anomaly",
    ],
    "modelling": [
        "surrogate",
        "physics-informed",
        "thermal field",
        "thermal history",
        "melt pool",
        "microstructure",
        "stress-strain",
        "simulation acceleration",
        "operator",
    ],
    "control": [
        "model predictive control",
        "closed-loop",
        "real-time decision-making",
        "adaptive control",
        "process control",
        "control policy",
    ],
    "reinforcement-learning": [
        "reinforcement learning",
        "policy",
        "ppo",
        "sac",
        "td3",
        "markov decision process",
    ],
    "digital-twin": [
        "digital twin",
    ],
}

PROCESS_TAG_RULES = {
    "welding": ["welding", "weld", "tig", "friction stir"],
    "machining": ["machining", "milling", "cnc"],
    "lpbf": ["lpbf", "laser powder bed fusion", "pbf-lb/m"],
    "ded": ["ded", "directed energy deposition", "lded", "wire-arc"],
    "bioprinting": ["bioprinting", "bioprinted"],
    "assembly": ["assembly", "din-rail", "robot skills"],
}

METHOD_TAG_RULES = {
    "physics-informed-ml": ["physics-informed", "pinn"],
    "multimodal-sensing": ["multimodal", "x-ray", "photodiode", "acoustic", "vision", "ultrasonic"],
    "graph-learning": ["graph", "graph neural", "graph attention"],
    "computer-vision": ["computer vision", "image", "vision-language", "segmentation", "cnn"],
    "surrogate-model": ["surrogate", "operator", "reduced-order"],
    "mpc": ["model predictive control", "mpc"],
    "reinforcement-learning": ["reinforcement learning", "ppo", "sac", "td3"],
}

CURATION_TARGETS = {
    "defect-detection": "refs/defect-detection.md",
    "modelling": "refs/modelling.md",
    "control": "refs/control.md",
    "reinforcement-learning": "refs/reinforcement-learning.md",
    "monitoring": "refs/monitoring.md",
    "additive-manufacturing": "refs/additive-manufacturing.md",
    "digital-twin": "refs/digital-twin.md",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def data_dir() -> Path:
    return repo_root() / "data"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def today_utc() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def append_log(log_path: Path, message: str) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{utc_now()}] {message}\n")


def normalize_whitespace(value: str) -> str:
    return " ".join((value or "").strip().split())


def normalize_title(title: str) -> str:
    text = normalize_whitespace(title).lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_author_name(author: str) -> str:
    return normalize_whitespace(author)


def build_dedup_key(title: str, year: Any = None, authors: Iterable[str] = ()) -> str:
    norm_title = normalize_title(title)
    first_author = normalize_title(next(iter(authors), ""))
    seed = f"{norm_title}|{year or ''}|{first_author}"
    return hashlib.sha1(seed.encode("utf-8")).hexdigest()


def extract_arxiv_base_id(short_id: str) -> str:
    short_id = normalize_whitespace(short_id)
    return short_id.split("v")[0]


def stable_source_id(source: str, base_id: str) -> str:
    return f"{source}:{base_id}"


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def score_keyword_hits(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term in lowered)


def pick_matching_tags(text: str, mapping: Dict[str, List[str]]) -> List[str]:
    lowered = text.lower()
    return [tag for tag, terms in mapping.items() if any(term in lowered for term in terms)]


def merge_unique_strings(values: Iterable[str]) -> List[str]:
    seen = []
    for value in values:
        norm = normalize_whitespace(value)
        if norm and norm not in seen:
            seen.append(norm)
    return seen


def merge_paper_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    for record in records:
        key = record["dedup_key"]
        if key not in merged:
            merged[key] = dict(record)
            merged[key]["query_sources"] = merge_unique_strings(record.get("query_sources") or [record.get("query_source", "")])
            continue

        current = merged[key]
        current["authors"] = merge_unique_strings((current.get("authors") or []) + (record.get("authors") or []))
        current["categories"] = merge_unique_strings((current.get("categories") or []) + (record.get("categories") or []))
        current["query_sources"] = merge_unique_strings((current.get("query_sources") or []) + (record.get("query_sources") or [record.get("query_source", "")]))
        current["date_discovered"] = min(current.get("date_discovered") or utc_now(), record.get("date_discovered") or utc_now())
        current["abstract"] = current.get("abstract") or record.get("abstract")
        current["url"] = current.get("url") or record.get("url")
        current["title"] = current.get("title") or record.get("title")
        current["year"] = current.get("year") or record.get("year")
    return sorted(merged.values(), key=lambda item: (item.get("year") or 0, item.get("date_discovered") or ""), reverse=True)


def digest_counter(values: Iterable[str]) -> Dict[str, int]:
    return dict(Counter(values))


def reason_text(parts: List[str]) -> str:
    return "; ".join(part for part in parts if part)
