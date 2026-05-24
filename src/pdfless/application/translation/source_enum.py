from enum import Enum
from deep_translator import (
    GoogleTranslator,
    LingueeTranslator,
    PonsTranslator,
    MyMemoryTranslator,
    ChatGptTranslator,
    DeeplTranslator,
    MicrosoftTranslator,
)


class SourceType(Enum):
    # Free sources
    GOOGLE = GoogleTranslator
    LINGUEE = LingueeTranslator
    PONS = PonsTranslator
    MY_MEMORY = MyMemoryTranslator

    # Paid sources (API key needed)
    CHAT_GPT = ChatGptTranslator
    DEEP_L = DeeplTranslator
    MICROSOFT = MicrosoftTranslator

    def get_instance(self, **kwargs):
        """
        Returns the given source translator
        """
        return self.value(**kwargs)
