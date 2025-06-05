from typing import Dict

# Example mapping from human-readable field names to Salesforce API field names
FIELD_MAPPING: Dict[str, str] = {
    "loan amount": "Loan_Amount__c",
    "interest rate": "Interest_Rate__c",
    "closing date": "Closing_Date__c",
    # Add more mappings as needed
}
