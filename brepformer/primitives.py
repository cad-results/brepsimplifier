#!/usr/bin/env python3
"""Re-export from the top-level primitives module.

The canonical implementation lives in brepsimplifier/primitives.py.
This module re-exports everything so that internal brepformer imports
(e.g. from defeature_v2.py) continue to work.
"""

import importlib
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import primitives as _prim  # noqa: E402

# Re-export public API
fit_primitives = _prim.fit_primitives
fit_primitives_from_step = _prim.fit_primitives_from_step
defeature_and_fit = _prim.defeature_and_fit

# Re-export everything
from primitives import *  # noqa: F401,F403,E402
from primitives import main, parse_args  # noqa: E402

if __name__ == "__main__":
    main()
