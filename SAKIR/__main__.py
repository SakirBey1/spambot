# Developer : @SakirBey1
# GeliΕtirici : @SakirBey1

import glob
from pathlib import Path
from SAKIR.utils import load_plugins
import logging
from . import worker 


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s]: %(message)s',
                   level=logging.WARNING)

path = "SAKIR/plugins/*.py"
files = glob.glob(path)
for name in files:
  with open(name) as a:
    patt = Path(a.name)
    plugin_name = patt.stem
    load_plugins(plugin_name.replace(".py", ""))
    
print("π«πππππ π©πΕππΔ±πππ π»ππππππππΔ±")
print("π­ππππ ππ πΆπππππ πΆπππππΔ±πΔ±π πΎπππππ @SakirBey1")
if __name__=="__main__":
  worker.run_until_disconnected()
  
  
  # Kod SatΔ±r bitiΕi----------------------------@SakirBey1------------------------------
