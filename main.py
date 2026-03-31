from score_calculator import calculate_score
from suggestions import get_suggestions

def get_user_input():
    print("=== Digital Privacy Score Checker ===")

    password = input("Password strength (weak/medium/strong): ").lower()
    two_fa = input("Is 2FA enabled? (yes/no): ").lower()
    public_wifi = input("Do you use public WiFi frequently? (yes/no): ").lower()
    permissions = input("App permissions level (low/medium/high): ").lower()

    return password, two_fa, public_wifi, permissions

def main():
    user_data = get_user_input()
    score = calculate_score(*user_data)

    print("\nYour Privacy Score:", score)

    if score < 40:
        print("Risk Level: HIGH 🔴")
    elif score < 70:
        print("Risk Level: MODERATE 🟡")
    else:
        print("Risk Level: SAFE 🟢")

    suggestions = get_suggestions(*user_data)

    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)

if __name__ == "__main__":
    main()