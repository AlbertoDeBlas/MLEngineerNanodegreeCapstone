import sys
import importlib
import os

def update_library(library, method):
    importlib.reload(sys.modules[library])
    
    os.system("%reload_ext library")
    os.system("%autoreload library")
    #from str(library) import str(method)
    importlib.reload(sys.modules[library])