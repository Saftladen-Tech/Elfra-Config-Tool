from app.routes import generate_theme_ts
from app import app
from io import BytesIO

def examplecolors():
    return {
        "primary": "#111111",
        "secondary": "#222222",
        "accent": "#333333",
        "dark": "#000000",
        "bright": "#ffffff",
        "success": "#00ff00",
        "warn": "#ffaa00",
        "error": "#ff0000",
    }

def test_generate_theme_ts_auth_disabled():
    colors = examplecolors()
    auth = {"enabled": False, "google": False, "apple": False, "github": False,
            "keycloak": False, "microsoft": False, "discord": False, "facebook": False}
    ts = generate_theme_ts(colors, "Roboto", "Google", auth, "name", "https://name", [])
    assert "enabled: false" in ts
    assert "oAuth" not in ts

def test_generate_theme_ts_auth_enabled():
    colors = examplecolors()
    auth = {"enabled": True, "google": True, "apple": False, "github": True,
            "keycloak": False, "microsoft": False, "discord": False, "facebook": False}
    topics = [{"name": "T1", "color": "amber"}]
    ts = generate_theme_ts(colors, "Roboto", "Google", auth, "name", "https://name", topics)
    assert "enabled: true" in ts
    assert "oAuth" in ts
    assert "google: true" in ts
    assert "apple: false" in ts
    assert "name: 'T1'" in ts
    assert "color: 'amber'" in ts
