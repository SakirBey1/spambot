# Developer : @SakirBey1
# Geliştirici : @SakirBey1

import glob
from pathlib import Path
from SAKIR.utils import load_plugins
import loggin
from . import worker 


loggin.basicConfig(format='[%(levelname) 5s/%(asctime)s]: %(message)s',
                   level=loggin.WARNING)

path = "SAKIR/plugins/*.py"
files = glob.glob(path)
for name in files:
  with open(name) as a:
    patt = Path(a.name)
    plugin_name = patt.stem
    load_plugins(plugin_name.replace(".py", ""))
    
print("𝑫𝒆𝒑𝒍𝒐𝒚 𝑩𝒂ş𝒂𝒓ı𝒚𝒍𝒂 𝑻𝒂𝒎𝒂𝒎𝒍𝒂𝒏𝒅ı")
print("𝕭𝖔𝖙𝖚𝖓 𝖁𝖊 𝕶𝖆𝖞𝖓𝖆𝖐 𝕶𝖔𝖉𝖑𝖆𝖗ı𝖓ı𝖓 𝕾𝖆𝖍𝖎𝖇𝖎 @SakirBey1")
if __name__=="__main__":
  worker.run_until_disconnected()
  
  
  # Kod Satır bitişi----------------------------@SakirBey1------------------------------
