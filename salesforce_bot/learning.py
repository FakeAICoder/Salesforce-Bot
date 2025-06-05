from typing import Dict
from .logging_config import logger

class MappingLearner:
    """Simple learner that stores user corrections to improve field mapping."""

    def __init__(self):
        self.corrections: Dict[str, str] = {}

    def record_correction(self, user_input: str, correct_field: str):
        logger.info("Recording correction: '%s' -> '%s'", user_input, correct_field)
        self.corrections[user_input.lower()] = correct_field

    def get_corrected_field(self, user_input: str) -> str:
        return self.corrections.get(user_input.lower())
