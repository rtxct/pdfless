import ast

from pdfless.application.translation.languages_app import supported_languages
from tests.utils.file_test_utils import read_resource_file


def test_supported_languages():
    expected: dict = ast.literal_eval(
        read_resource_file("translation/res_supported_languages.txt")
    )

    assert expected == supported_languages()
