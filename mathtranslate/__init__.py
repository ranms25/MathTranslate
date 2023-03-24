__version__ = "1.3.1"
__author__ = "Jiace Sun"

import os
ROOT = os.path.dirname(os.path.abspath(__file__))
from . import config
from . import translation
from . import tencent
from . import fix_encoding
from . import process_latex
from . import overleaf
from .translation import translate
from . import translate_tex
