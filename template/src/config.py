"""
Brand Configuration Loader

Loads and validates the brand_config.json file, providing easy access
to colors, typography, voice settings, channel configuration, and
compliance rules.
"""

import json
from pathlib import Path
from typing import Union


class ColorEntry:
    """A single color definition from the brand config."""

    def __init__(self, data: dict):
        self.name = data.get("name", "")
        self.hex = data.get("hex", "#000000")
        self.rgb = tuple(data.get("rgb", [0, 0, 0]))
        self.usage = data.get("usage", "")

    def __repr__(self):
        return f"ColorEntry(name='{self.name}', hex='{self.hex}')"


class BrandConfig:
    """
    Complete brand configuration loaded from brand_config.json.

    Access patterns:
        config.brand_name -> "Acme Co"
        config.colors['primary'].hex -> "#243A4B"
        config.voice_and_tone['language_to_avoid'] -> [...]
        config.channels -> [{'name': 'LinkedIn', ...}, ...]
    """

    def __init__(self, raw: dict):
        self.brand_name = raw.get("brand_name", "")
        self.tagline = raw.get("tagline", "")
        self.version = raw.get("version", "1.0")

        self.colors = {}
        for key, value in raw.get("colors", {}).items():
            if isinstance(value, dict):
                self.colors[key] = ColorEntry(value)

        self.color_ratio = raw.get("color_ratio", {})
        self.typography = raw.get("typography", {})
        self.type_scale = raw.get("type_scale", {})
        self.voice_and_tone = raw.get("voice_and_tone", {})
        self.imagery = raw.get("imagery", {})
        self.compliance = raw.get("compliance", {})
        self.page_dimensions = raw.get("page_dimensions", {})

        channel_data = raw.get("channel_config", {})
        self.channels = channel_data.get("channels", [])

        self._raw = raw

    @property
    def active_channels(self):
        """Return only channels marked as active."""
        return [c for c in self.channels if c.get("active", False)]

    @property
    def language_to_avoid(self):
        """Convenience accessor for banned language list."""
        return self.voice_and_tone.get("language_to_avoid", [])

    @property
    def language_to_use(self):
        """Convenience accessor for preferred language list."""
        return self.voice_and_tone.get("language_to_use", [])

    @property
    def chart_colors(self):
        """Return a list of hex colors suitable for charts and data visualizations."""
        color_keys = ["secondary", "primary", "accent", "neutral_mid"]
        return [
            self.colors[k].hex
            for k in color_keys
            if k in self.colors
        ]

    def get_color_hex(self, color_key: str) -> str:
        """Get a hex color by its config key (e.g., 'primary', 'accent')."""
        if color_key in self.colors:
            return self.colors[color_key].hex
        return "#000000"

    def resolve_reference(self, ref: str) -> str:
        """
        Resolve a $-prefixed reference like '$colors.primary.hex' against the raw config.
        Returns the resolved value or the original string if not found.
        """
        if not ref.startswith("$"):
            return ref

        parts = ref[1:].split(".")
        current = self._raw
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return ref
        return str(current)


def load_brand_config(config_path: Union[str, Path] = None) -> BrandConfig:
    """
    Load brand configuration from a JSON file.

    Args:
        config_path: Path to brand_config.json. If None, searches for it
                     relative to this file's location.

    Returns:
        BrandConfig object with all brand settings.
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent / "brand" / "brand_config.json"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Brand config not found at {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        raw_config = json.load(f)

    return BrandConfig(raw_config)
