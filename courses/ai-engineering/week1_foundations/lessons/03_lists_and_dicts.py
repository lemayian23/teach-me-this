# Lesson 3 - lists and dicts: how data actually moves through an API
# Run:  python courses/ai-engineering/week1_foundations/lessons/03_lists_and_dicts.py

# A list is an ordered row of values. Counting starts at 0, not 1.
fields = ["total", "date", "payee"]
print(fields[0], fields[2])
print(len(fields))

# A dict is a set of labelled boxes: a key points at a value.
result = {"total": 1240.50, "currency": "KES", "payee": "Naivas"}
print(result["total"])

# .get() is the safe version: missing key gives None instead of an error.
print(result.get("date"))          # None
# print(result["date"])            # uncomment to see KeyError - read that error

# Nests are how a real API response looks: a dict holding a list of dicts.
response = {
    "request_id": "req_42",
    "credits_used": 1,
    "items": [{"name": "Sugar 1kg", "price": 110.0}, {"name": "Milk 500ml", "price": 65.0}],
}
for item in response["items"]:                 # loop over the list
    print(f"{item['name']:<12} KES {item['price']:.2f}")

# Sum the line items to check the receipt total adds up.
print(sum(item["price"] for item in response["items"]))
