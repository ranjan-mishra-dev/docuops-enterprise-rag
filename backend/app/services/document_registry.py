import json
from pathlib import Path

from app.config import settings


REGISTRY_PATH = Path(settings.documents_path) / "registry.json"


def _read_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {}

    with REGISTRY_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def _write_registry(registry: dict) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)

    temp_path = REGISTRY_PATH.with_suffix(".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(registry, file, indent=2)

    temp_path.replace(REGISTRY_PATH)


def get_all_documents() -> list[dict]:
    registry = _read_registry()
    return list(registry.values())


def get_document(document_id: str) -> dict | None:
    registry = _read_registry()
    return registry.get(document_id)


def save_document_record(
    document_id: str,
    filename: str,
    file_path: str,
    chunks: int,
) -> dict:
    registry = _read_registry()

    record = {
        "document_id": document_id,
        "filename": filename,
        "file_path": file_path,
        "chunks": chunks,
        "status": "indexed",
    }

    registry[document_id] = record
    _write_registry(registry)

    return record


def remove_document_record(document_id: str) -> bool:
    registry = _read_registry()

    if document_id not in registry:
        return False

    del registry[document_id]
    _write_registry(registry)

    return True