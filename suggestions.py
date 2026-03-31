def get_suggestions(password, two_fa, public_wifi, permissions):
    suggestions = []

    if password != "strong":
        suggestions.append("Use a strong password with symbols and numbers")

    if two_fa == "no":
        suggestions.append("Enable Two-Factor Authentication (2FA)")

    if public_wifi == "yes":
        suggestions.append("Avoid using public WiFi or use a VPN")

    if permissions == "high":
        suggestions.append("Limit app permissions to only necessary ones")

    if not suggestions:
        suggestions.append("Great job! Your privacy practices are strong")

    return suggestions