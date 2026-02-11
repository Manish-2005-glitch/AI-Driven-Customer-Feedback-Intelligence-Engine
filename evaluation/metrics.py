from .relevance import relevance_score

def confidence_label(score: float) -> str:
    if score >= 0.80:
        return "High"
    elif score >= 0.60:
        return "Medium"
    else:
        return "Low"

def evaluate(question: str, answer: str) -> dict:
    relevance = relevance_score(question, answer)

    return {
        "relevance_score": round(relevance, 4),
        "confidence": confidence_label(relevance)
    }
