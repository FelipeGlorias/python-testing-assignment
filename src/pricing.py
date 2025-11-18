def parse_price(text):
    """
    Parse a price like "$1,234.50" or "12.5" into a float.
    Raises ValueError for invalid formats.
    """
    s = str(text).strip()
    if not s:
        raise ValueError("Empty string is not a valid price")
    if s.startswith("$"):
        s = s[1:]
    
    if s.count(",") > 1 or any(not part.isdigit() for part in s.replace(",", "").split(".")):
        raise ValueError(f"Invalid price format: {text}")
    s = s.replace(",", "")
    return float(s)


def format_currency(value):
    """
    Format a float as a currency string, always 2 decimals, prefixed with $.
    """
    return "$" + f"{float(value):0.2f}"


def apply_discount(price, percent):
    """
    Reduce price by 'percent' (e.g., 10 means 10%).
    """
    if percent < 0:
        raise ValueError("percent must be >= 0")
    return price * (1 - percent / 100)  


def add_tax(price, rate=0.07):
    """
    Add tax to price. Default rate is 7%.
    """
    if rate < 0:
        raise ValueError("rate must be >= 0")
    return price * (1 + rate)


def bulk_total(prices, discount_percent=0, tax_rate=0.07):
    """
    Compute total of a list of prices after discount and tax.
    """
    subtotal = sum(float(p) for p in prices)
    after_discount = apply_discount(subtotal, discount_percent)
    return add_tax(after_discount, tax_rate)

