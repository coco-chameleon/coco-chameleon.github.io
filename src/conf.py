# SPDX-FileCopyrightText: 2026 Sam Hanes <sam@maltera.com>
# SPDX-License-Identifier: CC-BY-SA-4.0

# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

sys.path.append(str(Path('../ext').resolve()))

project = 'CoCo Chameleon'
copyright = '%Y Sam Hanes'
author = 'Sam Hanes'

needs_sphinx = '9.0'
extensions = ['net']
primary_domain = None

templates_path = ['../templates']
exclude_patterns = []


html_title = 'CoCo Chameleon'
html_baseurl = 'https://coco-chameleon.github.io'

html_theme = 'basic'
html_theme_options = {
}
html_sidebars = {
    '**': [
        'searchbox.html',
        'globaltoc.html',
    ]
}
html_static_path = ['../static']
html_css_files = ['theme.css']
