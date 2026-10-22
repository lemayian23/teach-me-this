# Lesson 2 - strings and f-strings: this is how every prompt gets built
# Run:  python courses/ai-engineering/week1_foundations/lessons/02_strings_and_prompts.py

# A string is just text in quotes. One line or many.
greeting = "Send back the total amount."
print(greeting)

# Triple quotes hold text across several lines. Prompts usually live here.
instructions = """Extract from this receipt:
- total
- date
- payee"""
print(instructions)

# An f-string drops variables into text. This is the whole trick.
payee = "Naivas"
total = 1240.50
print(f"Receipt from {payee}: KES {total}")

# :.2f means "show this number with 2 decimal places". Money always needs it.
print(f"Receipt from {payee}: KES {total:.2f}")

# Real prompt = a template string with the document text inserted.
document_text = "NAIVAS  19/10/2026  TOTAL KES 1240.50  M-PESA TXN TJ7K9LM2"
prompt = f"""Read the text below and return the total, the date and the payee.

Text:
{document_text}"""
print(prompt)

# len() counts characters, .upper() and .strip() return cleaned-up copies.
print(len(document_text), document_text[:6], instructions.strip())
