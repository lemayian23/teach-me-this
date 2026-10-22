# Lesson 6 - mini project: a pretend version of the real endpoint
# Run:  python courses/ai-engineering/week1_foundations/lessons/06_mini_project.py

# Everything from lessons 2-4 in one 30-line program. No API key, no model:
# extract_fields() is a stand-in you will replace with a real call in Week 3.

KNOWN_PAYEES = {"NAIVAS": "Naivas", "QUICKMART": "Quickmart", "SACCO": "SACCO contribution"}


def build_prompt(document_text):
    return f"""Extract total, date and payee. Reply JSON only:
"total": number, "currency": "KES", "date": "YYYY-MM-DD", "payee": string.
Use null for anything unreadable.

Text:
{document_text}"""


def extract_fields(document_text):
    # Pretend model. Real ones arrive in Week 2 with Pydantic checking the shape.
    words = document_text.split()
    total = 0.0
    date = None
    for word in words:
        if "." in word and word.replace(".", "").isdigit():
            total = float(word)        # first decimal-looking number wins
        if "/" in word:
            date = word                # 19/10/2026
    return {
        "total": total,
        "currency": "KES",
        "date": date,
        "payee": KNOWN_PAYEES.get(words[0].upper()),
    }


def serve(document_text, credits):
    """One request: check the balance, debit it, do the work."""
    if credits < 1:
        return {"error": {"code": "insufficient_credits"}}, credits
    return {"fields": extract_fields(document_text), "credits_used": 1}, credits - 1


balance = 2
for text in ["NAIVAS 19/10/2026 1240.50", "QUICKMART 05/10/2026 890.00", "SACCO 02/10/2026 5000.00"]:
    answer, balance = serve(text, balance)
    print(build_prompt(text).splitlines()[0])   # what we would have sent
    print(answer, f"balance={balance}\n")
