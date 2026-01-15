# SPDX-FileCopyrightText: 2026 Sam Hanes <sam@maltera.com>
# SPDX-License-Identifier: CC-BY-SA-4.0

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

class NetRole(SphinxRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.literal(classes=["net"])

        stars = self.text.split("*")
        while len(stars) > 1:
            slash = stars.pop(0).rsplit('/', 1)
            if len(slash) > 1:
                node.append(nodes.inline(text=slash[0] + '/', classes=["net-pos"]))
                node.append(nodes.inline(text=slash[1], classes=["net-neg"]))
            else:
                node.append(nodes.inline(text=slash[0], classes=["net-neg"]))

        if len(stars) > 0 and stars[0] != "":
            node.append(nodes.inline(text=stars[0], classes=["net-pos"]))

        return [node], []

def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role('net', NetRole())

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
