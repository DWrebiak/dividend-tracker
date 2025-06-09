def format_usd(value):
    return f"${value:.2f}" if value is not None else "No data"

def format_percent(value, already_percent=False):
    if value is None:
        return "No data"
    if already_percent:
        return f"{value:.2f}%"
    return f"{value * 100:.2f}%"
