# Builds a simple formatted report from fetched data

def generate_report(data):
    """
    Generate a human-readable report from ad data.
    """
    return (
        f"Campaign: {data['campaign']}\n"
        f"Clicks: {data['clicks']}\n"
        f"Impressions: {data['impressions']}\n"
        f"Cost: ${data['cost']:.2f}"
    )
