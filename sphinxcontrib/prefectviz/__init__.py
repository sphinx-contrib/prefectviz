"""
    sphinxcontrib.prefectviz
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A short description of the extension

    :copyright: Copyright 2017 by Panagiotis Simakis <sp1thas@autistici.org>
    :license: BSD, see LICENSE for details.
"""

import pbr.version
from .flowviz import PrefectFlowViz

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

# __version__ = pbr.version.VersionInfo(
#     'sphinxcontrib-prefectviz').version_string()
__version__ = "0.1"


def setup(app):
    app.add_directive("flowviz", PrefectFlowViz)
    return {"version": __version__, "parallel_read_safe": True}
