from .languages_app import supported_languages
from .source_type_enum import SourceType


def translate(
    source: str,
    target: str,
    text: str,
    translator: SourceType = SourceType.GOOGLE,
    api_key: str | None = None,
) -> str | list[str]:
    """
    Translates the given text from a language to another.
    """
    if not all(isinstance(arg, str) for arg in (source, target, text)):
        raise TypeError("Source, Target and text must all be strings")

    params: dict = {}
    if api_key:
        params["api_key"] = api_key
    params["source"] = source
    params["target"] = target

    options: list[str] | dict[str, str] = supported_languages(translator)
    valid_options = (
        list(options.keys()) + list(options.values())
        if isinstance(options, dict)
        else options
    )

    if source not in valid_options or target not in valid_options:
        raise TypeError(
            f"Source and Target must be a valid option. Got: source='{source}', target='{target}'"
        )

    try:
        return translator.get_instance(**params).translate(text)
    except Exception as e:
        raise RuntimeError(
            f"It was not possible to translate the given text: {text}"
        ) from e
