# -*- coding: utf8 -*-
import os
import sys

sys.path.append(os.path.abspath('.'))

import test_child.child_module.src.child_module as CM


def foo():
  return 'foo'


def bar():
  return 'bar'


if __name__ == '__main__':
  print foo()
  print bar()
  print CM.baz()
