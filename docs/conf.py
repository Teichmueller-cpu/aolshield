import os
import sys

# Add project path
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Product Shield'
author = 'Ryah Ludins'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Bing Verification Meta Tag (Correct Way)
html_meta = {
    "google-site-verification": "YqICi0e1b-C8Ho87DB5clxbiDDZv6WYPDEVGcxN8tSc"
}

# Optional: Add custom CSS or JS (if needed)
html_css_files = []
html_js_files = []

# -- Options for internationalization ----------------------------------------
language = 'en'

# -- Misc settings -----------------------------------------------------------
master_doc = 'index'
