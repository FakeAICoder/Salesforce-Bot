# Salesforce Bot

This project provides a simple command line bot that demonstrates how chat inputs
could be mapped to Salesforce updates. It resolves user-provided field names to
Salesforce API field names, logs all actions, and includes a minimal self-learning
component for correcting field mappings.

## Usage

Run the bot with Python:

```bash
python -m salesforce_bot.bot
```

Enter commands in the format:

```
<loan_id> <field name> <value>
```

For example:

```
12345 "loan amount" 100000
```

This will attempt to update the `Loan_Amount__c` field for loan `12345` to `100000`.

All updates are logged to `salesforce_bot.log`.
