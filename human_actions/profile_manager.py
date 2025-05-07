import configparser
from pathlib import Path

class ProfileManager:
    def __init__(self, profile_file="profil.txt"):
        self.profile_file = profile_file
        self.profiles = self._load_profiles()
    def _load_profiles(self):
        config = configparser.ConfigParser()
        if not Path(self.profile_file).exists():
            raise FileNotFoundError(f"Profil dosyası bulunamadı: {self.profile_file}")
        config.read(self.profile_file)
        profiles = {}
        for section in config.sections():
            profiles[section] = {
                'name': config.get(section, 'name', fallback='Unknown'),
                'typing_speed_min': config.getfloat(section, 'typing_speed_min', fallback=0.1),
                'typing_speed_max': config.getfloat(section, 'typing_speed_max', fallback=0.3),
                'move_speed_min': config.getfloat(section, 'move_speed_min', fallback=0.05),
                'move_speed_max': config.getfloat(section, 'move_speed_max', fallback=0.3),
                'scroll_speed': config.get(section, 'scroll_speed', fallback='medium'),
                'error_rate': config.getfloat(section, 'error_rate', fallback=0.05),
                'jitter_intensity': config.getint(section, 'jitter_intensity', fallback=4)
            }
        return profiles
    def get_profile(self, profile_name):
        return self.profiles.get(profile_name, None)
    def list_profiles(self):
        return list(self.profiles.keys())