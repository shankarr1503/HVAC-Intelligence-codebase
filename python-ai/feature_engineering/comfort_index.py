# comfort_index.py
"""Calculate passenger comfort indices."""

def compute_comfort_score(temp: float, humidity: float, heart_rate: float, skin_temp: float, seat_temp: float) -> float:
    # enhanced placeholder calculation using multiple cues
    score = 1.0 - abs(temp - 22.0) / 10.0
    score *= 1.0 - abs(humidity - 50.0) / 100.0
    score *= 1.0 - abs(skin_temp - 33.0) / 10.0
    score *= 1.0 - abs(seat_temp - 22.0) / 10.0
    # penalize high heart rate (stress)
    if heart_rate > 100:
        score *= 0.8
    return max(0.0, min(score, 1.0))
