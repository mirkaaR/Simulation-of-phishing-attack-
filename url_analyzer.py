import re

def analyze_url(url):
    risk_score = 0
    reasons = []
    url_lower = url.lower()

    # 1. Provera sumnjivih ključnih reči
    suspicious_keywords = [
        "login", "verify", "secure", "account", "update", 
        "bank", "paypal", "wallet", "confirm", "password"
    ]
    
    found_keywords = []
    for word in suspicious_keywords:
        if word in url_lower:
            found_keywords.append(word)
    
    if found_keywords:
        risk_score += len(found_keywords) # Svaka reč povećava rizik
        reasons.append(f"Детектоване сумњиве кључне речи: {', '.join(found_keywords)}")

    # 2. Provera dužine URL-a (Napadači često koriste duge linkove da sakriju pravi domen)
    if len(url) > 50:
        risk_score += 1
        reasons.append("URL је необично дугачак (тактика прекривања)")

    # 3. Provera vizuelnih varki (Typosquatting / Homoglifi)
    # Tražimo brojeve koji zamenjuju slična slova (npr. g00gle, paypa1)
    visual_tricks = {
        "0": "нула уместо слова O",
        "1": "број 1 уместо слова L ili I",
        "3": "број 3 уместо слова E",
        "4": "број 4 уместо слова A",
        "5": "број 5 уместо слова S"
    }
    
    found_tricks = []
    for digit, desc in visual_tricks.items():
        if digit in url:
            found_tricks.append(desc)
    
    if found_tricks:
        risk_score += 2
        reasons.append(f"Могућа визуелна обмана: {'; '.join(found_tricks)}")

    # 4. Provera broja poddomena
    if url.count(".") > 3:
        risk_score += 2
        reasons.append("Детектован велики број поддомена (чест знак phishinga)")

    # 5. Provera protokola (HTTPS vs HTTP)
    if url.startswith("http://"):
        risk_score += 2
        reasons.append("Сајт не користи сигурну енкрипцију  (HTTP уместо HTTPS)")

    # Određivanje nivoa rizika na osnovu skora
    if risk_score >= 4:
        level = "ВИСОК РИЗИК"
    elif risk_score >= 2:
        level = "СРЕДЊИ РИЗИК"
    else:
        level = "НИЗАК РИЗИК"

    return {
        "url": url,
        "score": risk_score,
        "level": level,
        "reasons": reasons
    }