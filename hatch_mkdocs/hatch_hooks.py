from __future__ import annotations

from hatchling.plugin import hookimpl

from .plugin import MkDocsEnvironmentCollector


@hookimpl
def hatch_register_environment_collector():
    return MkDocsEnvironmentCollector
    return MkDocsEnvironmentCollector
