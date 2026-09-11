"""Load shared HTML parser without invoking the generator."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("build_site", Path(__file__).with_name("build-site.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Document, ROOT, ORIGIN = module.Document, module.ROOT, module.ORIGIN
