# Lesson 4 - functions: wrap a prompt once, reuse it a thousand times
# Run:  python courses/ai-engineering/week1_foundations/lessons/04_functions.py

# A function is a named recipe: inputs in, one thing out.
def build_prompt(document_text, currency_hint="KES"):
    # currency_hint has a default, so callers can leave it out.
    return f"""Extract the fields from this document text.
Return total, date, payee. Assume currency {currency_hint}.

Text:
{document_text}"""


# Call it with the same template and different data.
first = build_prompt("NAIVAS 19/10/2026 TOTAL KES 1240.50")
second = build_prompt("SACCO CONTRIB 02/10/2026 5,000.00", currency_hint="KES")
print(first)
print(second[:40], "...")

# A function with a guard: reject input that cannot possibly work.
def estimate_credits(document_text, cost_per_document=1):
    if not document_text.strip():
        return 0                     # empty upload should never cost a credit
    return cost_per_document


print(estimate_credits("NAIVAS 1240.50"))
print(estimate_credits("   "))       # 0, and no exception

# Why this matters: in Week 3 this exact shape becomes your POST /v1/extract
# handler - document in, prompt built, credits debited.
