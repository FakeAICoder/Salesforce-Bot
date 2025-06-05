import difflib
from dataclasses import dataclass
from typing import Optional

from .field_mapping import FIELD_MAPPING
from .logging_config import logger
from .salesforce_api import SalesforceAPI
from .learning import MappingLearner

@dataclass
class UpdateRequest:
    record_id: str
    field: str
    value: str

class SalesforceBot:
    def __init__(self):
        self.api = SalesforceAPI()
        self.learner = MappingLearner()

    def resolve_field(self, user_field: str) -> Optional[str]:
        """Resolve a user-provided field name to a Salesforce API field name."""
        corrected = self.learner.get_corrected_field(user_field)
        if corrected:
            return corrected
        candidates = FIELD_MAPPING.keys()
        matches = difflib.get_close_matches(user_field.lower(), candidates, n=1, cutoff=0.6)
        if matches:
            field = FIELD_MAPPING[matches[0]]
            logger.info("Resolved field '%s' -> '%s'", user_field, field)
            return field
        logger.warning("Could not resolve field: %s", user_field)
        return None

    def handle_update(self, req: UpdateRequest) -> bool:
        field_api_name = self.resolve_field(req.field)
        if not field_api_name:
            logger.error("Unknown field: %s", req.field)
            return False
        logger.info("Updating record %s field %s with value %s", req.record_id, field_api_name, req.value)
        return self.api.update_record('Loan__c', req.record_id, field_api_name, req.value)


def main():
    bot = SalesforceBot()
    print("Enter commands in the format: <loan_id> <field> <value>")
    print("Type 'quit' to exit")
    while True:
        raw = input('> ').strip()
        if raw.lower() in {'q', 'quit', 'exit'}:
            break
        parts = raw.split(maxsplit=2)
        if len(parts) != 3:
            print("Invalid input. Expected: <loan_id> <field> <value>")
            continue
        loan_id, field, value = parts
        req = UpdateRequest(record_id=loan_id, field=field, value=value)
        success = bot.handle_update(req)
        if success:
            print("Update successful")
        else:
            print("Update failed")

if __name__ == '__main__':
    main()
