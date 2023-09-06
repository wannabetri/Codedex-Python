# Write code below 💖

def moon_phase(phase):
    moon_phases = {
        "New Moon": "🌑",
        "Waxing Crescent": "🌒",
        "First Quarter": "🌓",
        "Waxing Gibbous": "🌔",
        "Full Moon": "🌕",
        "Waning Gibbous": "🌖",
        "Last Quarter": "🌗",
        "Waning Crescent": "🌘"
    }

    return moon_phases.get(phase, "Invalid Moon Phase")


# Example usage:
answer = moon_phase("Waxing Crescent")
print(answer)  # Output: 🌑