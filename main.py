import re

# Vorgabewerte für alle Farben
DEFAULT_COLORS = {
    "primary": "#669c35",
    "secondary": "#aaaaaa",
    "accent": "#fde1af",
    "dark": "#0e0e11",
    "bright": "#ffffff",
    "success": "#00DC82",
    "warn": "#fcc800",
    "error": "#ff6467"
}

# HEX-Validator
def is_valid_hex(color: str) -> bool:
    return bool(re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color))

# CLI-Abfrage einer Farbe
def prompt_color(name: str, default: str) -> str:
    while True:
        user_input = input(f"{name.capitalize()} [{default}]: ").strip()
        if not user_input:
            return default
        if is_valid_hex(user_input):
            return user_input
        print("❌ Ungültiger HEX-Wert. Bitte versuche es erneut (Beispiel: #112233)")

# TypeScript-Code generieren
def generate_theme_ts(colors: dict) -> str:
    ts_lines = ["export const theme = {", "  colors: {"]
    for key, value in colors.items():
        ts_lines.append(f'    {key}: "{value}",')
    ts_lines.append("  }")
    ts_lines.append("};")
    return "\n".join(ts_lines)

def main():
    print("🎨 Theme-Konfigurator für deine Nuxt/Tailwind-Webseite")
    print("Gib HEX-Farben ein oder drücke Enter, um die Standardfarbe zu übernehmen.\n")

    final_colors = {}
    for color_key, default in DEFAULT_COLORS.items():
        final_colors[color_key] = prompt_color(color_key, default)
    
    ts_code = generate_theme_ts(final_colors)

    output_path = "utils/theme.ts"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ts_code)

    print(f"\n✅ Theme-Datei erfolgreich erstellt unter: {output_path}")

if __name__ == "__main__":
    main()

