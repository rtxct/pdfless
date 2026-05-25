from .source_type_enum import SourceType


def supported_languages(
    translator: SourceType = SourceType.GOOGLE, api_key: str | None = None
) -> list[str] | dict[str, str]:
    """
    Returns all the supported languages from the given translator type
    """
    params = {}
    if api_key:
        params["api_key"] = api_key

    return translator.get_instance(**params).get_supported_languages(as_dict=True)
