# SPDX-FileCopyrightText: 2026 Sam Hanes <sam@maltera.com>
# SPDX-License-Identifier: CC-BY-SA-4.0

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

class NetRole(SphinxRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.literal(text=self.text)
        return [node], []

def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role('net', NetRole())

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
