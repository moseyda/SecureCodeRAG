from app.core.config import settings

def calculate_confidence(
    static_hits: int,
    retrieved_docs: int
) -> dict:
    """
    Confidence score is based on:
    - static detection strength
    - amount of supporting documentation
    """

    score = min(
        1.0,
        (static_hits * 0.4) + (retrieved_docs * 0.15)
    )

    if score >= settings.CONFIDENCE_HIGH:
        level = "High"
    elif score >= settings.CONFIDENCE_MEDIUM:
        level = "Medium"
    else:
        level = "Low"

    return {
        "score": round(score, 2),
        "level": level
    }
