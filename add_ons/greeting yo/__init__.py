import importlib

def main():
    a = importlib.import_module(f"{__name__}.scripts.main")
    a.ta()