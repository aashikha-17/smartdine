from math import radians, cos, sin, asin, sqrt
from datetime import datetime

# --------------------------------------------------
# RULE DICTIONARIES
# --------------------------------------------------

HEALTHY_CUISINES = ["south indian", "salad", "veg", "continental"]

TASTE_RULES = {
    "cheesy": ["pizza", "burger", "pasta"],
    "sweet": ["dessert", "ice cream"],
    "spicy": ["biryani", "north indian"]
}

MOOD_RULES = {
    "sad": ["biryani", "north indian", "pasta"],
    "tired": ["coffee", "snacks"],
    "happy": ["pizza", "burger"]
}

BUDGET_RULES = {
    "cheap": "₹",
    "affordable": "₹",
    "premium": ["₹₹", "₹₹₹"]
}

LATE_NIGHT_START = 20  # 8 PM

# --------------------------------------------------
# DISTANCE UTILITY
# --------------------------------------------------

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return 2 * R * asin(sqrt(a))

# --------------------------------------------------
# HUMAN-READABLE EXPLANATION
# --------------------------------------------------

def build_reason(name, reasons):
    if not reasons:
        return f"Try {name} because it’s a popular nearby choice."

    phrases = []

    if any("cheesy" in r for r in reasons):
        phrases.append("something cheesy")

    if any("comfort" in r or "mood" in r for r in reasons):
        phrases.append("comfort food after a rough day")

    if any("quick" in r for r in reasons):
        phrases.append("a quick and affordable bite")

    if any("healthy" in r for r in reasons):
        phrases.append("healthy lunch options")

    if any("late" in r for r in reasons):
        phrases.append("late-night cravings")

    if any("special" in r for r in reasons):
        phrases.append("a special occasion dinner")

    if any("budget" in r for r in reasons):
        phrases.append("a budget-friendly option")

    if any("close" in r for r in reasons):
        phrases.append("nearby")

    return f"Try {name} because you wanted " + " and ".join(phrases) + "."

# --------------------------------------------------
# CORE RECOMMENDER
# --------------------------------------------------

def recommend(prompt, restaurants, user_lat, user_lon):
    prompt = prompt.lower()
    results = []
    current_hour = datetime.now().hour

    # --------------------------------------------------
    # PROMPT NORMALIZATION
    # --------------------------------------------------

    if "rough day" in prompt or "bad day" in prompt or "stress" in prompt:
        prompt += " sad comfort"

    if "comfort food" in prompt:
        prompt += " sad"

    if "not too expensive" in prompt or "under 100" in prompt:
        prompt += " cheap quick"

    if "healthy lunch" in prompt or "healthy" in prompt:
        prompt += " healthy"

    if "late night" in prompt or "open now" in prompt:
        prompt += " latenight"

    if "special occasion" in prompt:
        prompt += " premium"

    # --------------------------------------------------
    # SCORING LOOP
    # --------------------------------------------------

    for r in restaurants:
        score = 0
        reasons = []
        cuisine = r.cuisine.lower()

        # ---------- TASTE ----------
        for taste, foods in TASTE_RULES.items():
            if taste in prompt and any(f in cuisine for f in foods):
                score += 5
                reasons.append(f"matches your {taste} craving")
        

        # ---------- STRICT CHEESY ----------
        if "cheesy" in prompt and not any(f in cuisine for f in TASTE_RULES["cheesy"]):
            score -= 6
        # ---------- STRICT CHEESY OVERRIDE ----------
        if "cheesy" in prompt:
            if not any(f in cuisine for f in TASTE_RULES["cheesy"]):
                score = -20  # hard block non-cheesy restaurants


        # ---------- MOOD ----------
        for mood, foods in MOOD_RULES.items():
            if mood in prompt and any(f in cuisine for f in foods):
                score += 4
                reasons.append(f"suits your {mood} mood")

        # ---------- BUDGET ----------
        if "cheap" in prompt and r.price_range == "₹":
            score += 3
            reasons.append("fits your budget")

        if "premium" in prompt and r.price_range in ["₹₹", "₹₹₹"]:
            score += 4
            reasons.append("perfect for a special occasion")

        # ---------- QUICK ----------
        if "quick" in prompt and r.price_range == "₹":
            score += 3
            reasons.append("good for a quick bite")

        # ---------- HEALTHY ----------
        if "healthy" in prompt:
            if (
                (hasattr(r, "tags") and "healthy" in r.tags) or
                any(h in cuisine for h in HEALTHY_CUISINES)
            ):
                score += 5
                reasons.append("offers healthy lunch options")
            else:
                score -= 5

        if "healthy" in prompt and "dessert" in cuisine:
            score -= 8

        # ---------- LATE NIGHT (STRICT) ----------
        if "latenight" in prompt:
            if hasattr(r, "close_hour") and r.close_hour >= LATE_NIGHT_START:
                score += 6
                reasons.append("is open late at night")
            else:
                score -= 6

        # ---------- DISTANCE (TIE-BREAKER ONLY) ----------
        dist = haversine(user_lat, user_lon, r.latitude, r.longitude)
        if dist <= 2 and score > 0 and "latenight" not in prompt:
            score += 1
            reasons.append("is very close to you")

        results.append((score, dist, r, reasons))

    results.sort(key=lambda x: (-x[0], x[1]))

    return [
        {
            "id": r.id,
            "name": r.name,
            "cuisine": r.cuisine,
            "rating": r.rating,
            "latitude": r.latitude,
            "longitude": r.longitude,
             "image_url": r.image_url,
            "reason": build_reason(r.name, reasons)
        }
        for _, _, r, reasons in results[:3]
    ]
