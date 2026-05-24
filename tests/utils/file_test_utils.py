from pathlib import Path


RESOURCE_PATH = "resources"


def read_resource_file(file_path: str):
    root_dir = Path(__file__).resolve().parent.parent
    full_path = root_dir / RESOURCE_PATH / file_path

    with open(full_path, "r") as file:
        content = file.read()
        return content
