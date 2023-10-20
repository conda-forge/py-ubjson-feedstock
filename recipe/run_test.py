#!/usr/bin/env python

import unittest
import sys


def main():
  suite = unittest.TestLoader().discover('test', pattern = 'test.py')
  sys.exit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())


if __name__ == '__main__':
    main()
