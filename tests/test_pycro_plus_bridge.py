from pathlib import Path

from pycromanager import start_headless
from pymmcore_plus import find_micromanager

from pycro_plus_bridge import pycroCorePlus

# Start the Java process


def test_for_smoke():
    mm_app_path = Path(find_micromanager())
    start_headless(
        str(mm_app_path), str(mm_app_path / "MMConfig_demo.cfg"), timeout=5000
    )
    pycroCorePlus()
