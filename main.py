import os
import re
import sys

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
def generate_theme_ts(colors: dict, font: str, font_provider: str, auth_config: dict) -> str:
    ts_lines = [
        "export interface config  {",
        "  colors: {",
    ]
    for key in colors:
        ts_lines.append(f"    {key}: string;")
    ts_lines.append("  };")
    ts_lines.append("  font: string;")
    ts_lines.append("  fontProvider: string;")
    ts_lines.append("  auth: {")
    ts_lines.append("    enabled: boolean;")
    ts_lines.append("    provider?: string;")
    ts_lines.append("    publicKey?: string;")
    ts_lines.append("    secretKey?: string;")
    ts_lines.append("    server?: string;")
    ts_lines.append("  };")
    ts_lines.append("}\n")

    ts_lines.append("export const config: config = {")
    ts_lines.append("  colors: {")
    for key, value in colors.items():
        ts_lines.append(f'    {key}: "{value}",')
    ts_lines.append("  },")
    ts_lines.append(f"  font: \"{font}\",")
    ts_lines.append(f"  fontProvider: \"{font_provider}\",")
    ts_lines.append("  auth: {")
    ts_lines.append(f"    enabled: {str(auth_config['enabled']).lower()},")
    if auth_config['enabled']:
        ts_lines.append(f"    provider: \"{auth_config['provider']}\",")
        ts_lines.append(f"    publicKey: \"{auth_config['public_key']}\",")
        ts_lines.append(f"    secretKey: \"{auth_config['secret_key']}\",")
        ts_lines.append(f"    server: \"{auth_config['server']}\",")
    ts_lines.append("  }")
    ts_lines.append("};")
    return "\n".join(ts_lines)

def main():
    print("ELFRA Config Tool")
    print("Gib HEX-Farben ein oder drücke Enter, um die Standardfarbe zu übernehmen.\n")

    final_colors = {}
    for color_key, default in DEFAULT_COLORS.items():
        final_colors[color_key] = prompt_color(color_key, default)

    font = input("📄 Schriftart (z. B. 'Inter'): ").strip() or "Inter"
    font_provider = input("🔤 Font Provider (z. B. 'Google Fonts'): ").strip() or "Google Fonts"

    auth_config = {"enabled": False}
    use_auth = input("🔐 Usermanagement verwenden? (j/n): ").strip().lower()
    if use_auth in ("j", "ja", "y", "yes"):
        auth_config["enabled"] = True
        auth_config["provider"] = input("  🔑 Auth Provider: ").strip()
        auth_config["public_key"] = input("  🗝️  Public Key: ").strip()
        auth_config["secret_key"] = input("  🔒 Secret Key: ").strip()
        auth_config["server"] = input("  🌐 Server URL: ").strip()

    ts_code = generate_theme_ts(final_colors, font, font_provider, auth_config)

    # Zielpfad via Argument oder Default
    output_path = sys.argv[1] if len(sys.argv) > 1 else "config.ts"

    # Existiert Datei bereits?
    if os.path.exists(output_path):
        overwrite = input(f"⚠️  Die Datei '{output_path}' existiert bereits. Überschreiben? (j/n): ").strip().lower()
        if overwrite not in ("j", "ja", "y", "yes"):
            print("❌ Abgebrochen.")
            return

    # Verzeichnis sicherstellen
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ts_code)

    print(f"\n✅ Config-Datei erfolgreich erstellt unter: {output_path}")

if __name__ == "__main__":
    main()
# EOF