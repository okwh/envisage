#!/usr/bin/env python

#-----------------------------------------------------------------------------
#
#  Copyright (c) 2007 by Enthought, Inc.
#  All rights reserved.
#
#-----------------------------------------------------------------------------

"""
The entry point for an Envisage application.

"""

# Standard library imports.
import logging

# Enthought plugins.
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.developer.developer_plugin import DeveloperPlugin
from enthought.envisage.developer.ui.developer_ui_plugin import DeveloperUIPlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from enthought.envisage.ui.single_project.project_plugin import ProjectPlugin
from enthought.envisage.ui.workbench.api import WorkbenchApplication
from enthought.plugins.python_shell.python_shell_plugin import PythonShellPlugin

# Local imports.
from plugins.single_project.plugin_definition import EnvProjectPlugin
# FIXME: This is uncommented for now until we have the new TreeEditor
# implementation in place that can understand domain-objects that have
# been abstracted to an INode interface.
#from data.plugin.plugin_definition import DataPlugin

# Configure a logger for this application
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def main():
    """ Runs the application. """

    # Create the application.
    application = WorkbenchApplication(
        id = 'testProject_extended',
        plugins=[
            CorePlugin(),
            WorkbenchPlugin(),
            DeveloperPlugin(),
            DeveloperUIPlugin(),
            ProjectPlugin(),
            EnvProjectPlugin(),
            PythonShellPlugin(),
            # FIXME: This is uncommented for now until we have the new TreeEditor
            # implementation in place that can understand domain-objects that have
            # been abstracted to an INode interface.
            #DataPlugin(),
        ]
    )

    # Run the application.
    application.run()

    return


# Application entry point.
if __name__ == '__main__':
    main()
    