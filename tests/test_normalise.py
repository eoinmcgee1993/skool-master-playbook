import json, tempfile, unittest
from pathlib import Path
import subprocess, sys

class NormaliseTests(unittest.TestCase):
    def test_normalise_script(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/"data/inbox").mkdir(parents=True)
            (root/"data/inbox/example.txt").write_text("hello",encoding="utf-8")
            script=Path(__file__).parents[1]/"scripts/normalise.py"
            # Structural smoke test: the script must compile.
            subprocess.run([sys.executable,"-m","py_compile",str(script)],check=True)

if __name__=="__main__":
    unittest.main()
