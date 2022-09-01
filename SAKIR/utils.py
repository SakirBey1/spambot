# Developer By : @SakirBey1
# Geliştirici : @SakirBey1

import sys 
import loggin
import importlib
from telethon import TelegramClient, events
from pathlib import Path

def load_plugins(plugin_name):
  path = Path(f"SAKIR/plugins/{plugin_name}.py")
  name = "SAKIR.plugins.{}".format(plugin_name)
  spec = importlib.util.spec_from_file_location(name, path)
  load = importlib.util.module_from_spec(spec)
  load.logger = loggin.getLogger(plugin_name)
  spec.loader.exec_module(load)
  sys.modules["SAKIR.plugins." + plugin_name] = load
  print("𝕤𝕡𝕒𝕞 𝕘ö𝕟𝕕𝕖𝕣𝕚𝕔𝕚 𝕓𝕠𝕥 𝕚ç𝕖 𝕒𝕜𝕥𝕒𝕣𝕕ı" + plugin_name)
