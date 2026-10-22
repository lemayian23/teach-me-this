# Lesson 5 - prompt structure: five parts, and what each one buys you

A prompt is not a wish. It is a specification. Missing parts do not fail loudly,
they fail quietly by returning plausible nonsense, which is worse.

## The five parts

| Part | Answers | What it buys |
|------|---------|--------------|
| Role | Who is speaking? | Vocabulary and judgement |
| Task | What exactly do it? | The single thing you want |
| Context | What material to work from? | Grounding, so it stops inventing |
| Format | What shape is the answer? | Code that can parse it |
| Examples | Show, don't describe | The biggest quality jump available |

## Weak prompt

```
Extract details from this receipt.
NAIVAS 19/10/2026 TOTAL KES 1240.50
```

You get a paragraph back. Maybe it contains the total. Your code cannot
reliably find it, so the endpoint cannot be metered, tested or sold.

## Same request, structured

```
You are a bookkeeper reconciling Kenyan retail receipts. (role)

Return the total amount, the date and the payee for the receipt below. (task)

Receipt text:
NAIVAS 19/10/2026 TOTAL KES 1240.50 (context)

Reply with JSON only, exactly this shape, no commentary: (format)
{"total": number, "currency": "KES", "date": "YYYY-MM-DD", "payee": string}
Use null for any field you cannot read. (escape hatch)

Example of correct output: (examples)
{"total": 890.0, "currency": "KES", "date": "2026-09-01", "payee": "Quickmart"}
```

Now the output is machine-readable, missing data says so instead of guessing,
and you can compare two versions of the prompt against the same 30 documents
in Week 5 and prove one is better.

## Rules that survive every model swap

1. One task per prompt. "Summarise and classify and translate" does all three badly.
2. Name the format and stick to it. JSON is not a style preference, it is an interface.
3. Say what to do with the unknown. Without `null`, the model invents a number.
4. Give dates as a format, or next month you get "19 Oct" and "2026-10-19" mixed.
5. Change one part at a time. Change three and you cannot know which helped.

## Exercise

Take the weak prompt. Add only the format line. Run both against five real
documents and write down what changed. Keep the notes; Week 5 turns them into
your first evaluation set.
