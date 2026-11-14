# ai-happy-01 entry (Python 3.13, standard library only): copies the committed
# image to /output/entry.png. Deterministic — both runs write the same bytes.
import os, shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(here, 'entry.png'), os.path.join(out, 'entry.png'))
