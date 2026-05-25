from typing import Any, Union
from pydantic import BaseModel


class Page(BaseModel):
    text: Union[str, dict[Any, Any]]
    page_number: int
    images: dict[str, Any]
