# Currency Converter by Waleed Mohamed

def convert_currency(amount, from_currency, to_currency):
    # Fixed exchange rates
    rates = {
        'USD': 1.0,        # base
        'EUR': 0.85,       # 1 USD = 0.85 EUR
        'CAD': 1.35        # 1 USD = 1.35 CAD
    }

    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency."

    # Convert to USD first, then to target currency
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return round(converted, 2)

# User input
print("Supported currencies: USD, EUR, CAD")
from_curr = input("From currency: ").upper()
to_curr = input("To currency: ").upper()
amount = float(input("Amount: "))

# Conversion
result = convert_currency(amount, from_curr, to_curr)
print(f"{amount} {from_curr} = {result} {to_curr}")
