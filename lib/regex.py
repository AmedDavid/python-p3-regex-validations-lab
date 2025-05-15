import re

# NAME REGEX:
# - Allows capitalized names (e.g., John Cena)
# - Allows hyphenated names (e.g., Anya Taylor-Joy)
# - Allows apostrophes (e.g., D'Angelo)
# - Only one space between first and last name or more parts
name = r"^[A-Z][a-z]+(?:[-'][A-Z][a-z]+)*(?: [A-Z][a-z]+(?:[-'][A-Z][a-z]+)*)?$"
name_regex = re.compile(r"^[A-Z][a-z]*(?:[-'][A-Z][a-z]*)?(?: [A-Z][a-z]*(?:[-'][A-Z][a-z]*)?)?$")


# PHONE REGEX:
# Matches:
# - 5555555555
# - 555-555-5555
# - (555) 555-5555
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# EMAIL REGEX:
# Rules:
# - Starts with a letter
# - Then letters, digits, or single dots (but no double dots, $, etc.)
# - Must have `@`, then domain and TLD
email_address = r"^[A-Za-z](?:[A-Za-z0-9]*\.?[A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]+$"
email_regex = re.compile(email_address)
