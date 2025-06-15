def format_usd(value, shorten=False):
    if value is None:
        return "No data"
    if shorten:
        abs_value = abs(value)
        if abs_value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"
        elif abs_value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
    return f"${value:,.2f}"

def format_percent(value, already_percent=False):
    if value is None:
        return "No data"
    if already_percent:
        return f"{value:.2f}%"
    return f"{value * 100:.2f}%"
