#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")


name = "lab4"
default_task = "publish"


@init
def set_properties(project):
    project.set_property('dir_source_main_python', 'src/main/python')
    project.set_property('dir_source_unittest_python', 'src/unittest/python')
    project.depends_on_requirements('requirements.txt')

