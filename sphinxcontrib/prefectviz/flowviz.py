from __future__ import print_function

import importlib
import os

import prefect
from docutils import nodes
from docutils.parsers.rst.directives.images import Image


class PrefectFlowViz(Image):
    has_content = True
    required_arguments = 1
    optional_arguments = 0

    def run(self):
        env = self.state.document.settings.env  # sphinx.environment.BuildEnvironment
        config = env.config  # sphinx.config.Config
        output_folder = os.path.abspath(
            os.path.join(env.srcdir, config["html_static_path"][0])
        )

        # Get the path to the object containing the metadata
        flowmodulepath = self.arguments[0]
        module = ".".join(flowmodulepath.split(".")[:-1])
        flowname = flowmodulepath.split(".")[-1]

        try:
            flow: prefect.Flow = getattr(importlib.import_module(module), flowname)
        except ImportError:
            error = self.state_machine.reporter.error(
                f'"{module}" could not be imported',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]
        except AttributeError:
            error = self.state_machine.reporter.error(
                f"flow can'n be found inside the given module",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        messages = []
        flowfilepath = os.path.join(*flowmodulepath.split("."))
        output_path = os.path.join(output_folder, flowfilepath)

        flow.visualize(filename=output_path, format="png")

        self.arguments.insert(0, "/" + f"{output_path}.png")
        messages.extend(Image.run(self))
        return messages
