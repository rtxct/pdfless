import ast
import pytest

from unittest.mock import patch
from pdfless.application.translation.translator import supported_languages, translate
from tests.utils.file_test_utils import read_resource_file


def test_supported_languages():
    expected: dict = ast.literal_eval(
        read_resource_file("translation/res_supported_languages.txt")
    )

    assert expected == supported_languages()


def test_translate():
    expected: str = "Nor is there anyone who loves pain because it is pain"

    assert expected == translate(
        "la", "en", "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet"
    )


def test_translate_non_string_arguments():
    with pytest.raises(TypeError, match="Source, Target and text must all be strings"):
        translate(source=123, target="en", text="Neque porro")

    with pytest.raises(TypeError, match="Source, Target and text must all be strings"):
        translate(source="la", target=None, text="Neque porro")

    with pytest.raises(TypeError, match="Source, Target and text must all be strings"):
        translate(source="la", target="en", text=["Neque porro"])


def test_translate_invalid_language_options():
    with pytest.raises(
        TypeError,
        match="Source and Target must be a valid option. Got: source='xx', target='en'",
    ):
        translate(source="xx", target="en", text="Neque porro")

    with pytest.raises(
        TypeError,
        match="Source and Target must be a valid option. Got: source='la', target='yy'",
    ):
        translate(source="la", target="yy", text="Neque porro")


@patch("pdfless.application.translation.translator.SourceType")
@patch("pdfless.application.translation.translator.supported_languages")
def test_translate_runtime_error(mock_supported_languages, mock_source_type):
    mock_supported_languages.return_value = {"latin": "la", "english": "en"}

    mock_instance = mock_source_type.GOOGLE.get_instance.return_value
    mock_instance.translate.side_effect = Exception("Translation Failure")

    with pytest.raises(
        RuntimeError, match="It was not possible to translate the given text: Neque porro"
    ):
        translate(
            source="la",
            target="en",
            text="Neque porro",
            translator=mock_source_type.GOOGLE,
        )
