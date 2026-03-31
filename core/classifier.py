# Maps category names to a list of keywords found in expense descriptions.
# To add a new category, simply add a new entry here.
from typing import Dict, List

CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "Food":          ["food", "lunch", "dinner", "breakfast", "restaurant", "cafe", "snack", "groceries", "zomato", "swiggy"],
    "Transport":     ["travel", "uber", "ola", "bus", "train", "metro", "fuel", "petrol", "cab", "flight"],
    "Entertainment": ["movie", "netflix", "spotify", "concert", "game", "cinema", "show"],
    "Shopping":      ["amazon", "flipkart", "clothes", "shirt", "shoes", "mall", "shopping"],
    "Health":        ["medicine", "doctor", "hospital", "pharmacy", "gym", "fitness"],
    "Bills":         ["electricity", "water", "rent", "wifi", "internet", "phone", "recharge"],
}


def classify_category(description: str) -> str:
    """Return the category that best matches the expense description.

    Checks the description (case-insensitively) against each category's
    keyword list. Falls back to 'Other' if no keyword matches.

    Args:
        description: The raw expense description entered by the user.

    Returns:
        A category string such as 'Food', 'Transport', or 'Other'.
    """
    lowered = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in lowered for word in keywords):
            return category
    return "Other"