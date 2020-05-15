import sys
import importlib

def update_library(library, method)
    importlib.reload(sys.modules[library])
    %reload_ext library
    %autoreload library
    from str(library) import str(method)