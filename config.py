from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_cfg_path = Path(__file__).resolve().parent / 'app' / 'config.py'
_spec = spec_from_file_location('_app_config', _cfg_path)
_module = module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_module)

for _name in dir(_module):
    if not _name.startswith('_'):
        globals()[_name] = getattr(_module, _name)
