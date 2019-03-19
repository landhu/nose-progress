"""Print progress to stdout. Enabled by --with-progress"""

from functools import partial
import itertools
import logging
import os
import sys

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.noseprogress')


class Progress(Plugin):
    name = 'progress'
    _handler_prefix = 'nose_progress_'
    encoding = "UTF-8"
    _totalTests = 0

    def __init__(self):
        super(Progress, self).__init__()  # involved the Plugin init
        self.test_numbers = itertools.count(1)

    def options(self, parser, env=os.environ):
        super(Progress, self).options(parser, env=env)

    def configure(self, options, conf):
        super(Progress, self).configure(options, conf)
        if not self.enabled:
            return

    def prepareTestLoader(self, loader):
        def capture_suite(orig_method, *args, **kwargs):
            self._totalTests += orig_method(*args, **kwargs).countTestCases()
            loader._visitedPaths = set()
            return orig_method(*args, **kwargs)
        if hasattr(loader, 'loadTestsFromNames'):
            loader.loadTestsFromNames = partial(capture_suite,
                                                loader.loadTestsFromNames)

    def startTest(self, test):
        progress = '[{0}/{1}] '.format(next(self.test_numbers), self._totalTests)
        sys.stderr.write(progress)
