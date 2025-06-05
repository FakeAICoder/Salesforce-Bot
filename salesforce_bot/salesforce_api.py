class SalesforceAPI:
    """A stub Salesforce API client."""

    def __init__(self):
        # Placeholder for authentication initialization
        pass

    def update_record(self, object_name: str, record_id: str, field: str, value):
        """Update a field on a Salesforce record.

        In a real implementation this would make a REST API call.
        """
        print(f"[SalesforceAPI] Would update {object_name} {record_id}: {field}={value}")
        # return success status
        return True
