"""
Source from https://github.com/ChristianECooper
"""

import atexit
from datetime import datetime


class Test:
    """
    Implements the test interface as described here:
    http://www.codewars.com/docs/python-test-reference-1
    """

    def __init__(self):
        self.__desc = "Undefined"
        self.__itmsg = "Undefined"
        self.__failures = 0
        self.__successes = 0
        self.__start = datetime.now()

    def describe(self, msg):
        print(msg)
        self.__desc = msg

    def it(self, msg):
        print(msg)
        self.__itmsg = msg

    def _assert(self, p, actual, expected, msg):
        if not p(expected, actual):
            self._error(msg, expected, actual)
        else:
            self._success()

    def assert_equals(self, actual, expected, msg="{} should be {}"):
        eq = lambda a, b: a == b
        self._assert(eq, actual, expected, msg)

    def assert_not_equals(self, actual, unexpected, msg="{} should be {}"):
        neq = lambda a, b: a != b
        self._assert(neq, actual, unexpected, msg)

    def expect_error(self, msg, fn):
        try:
            fn()
            self._error("Expected an error" if not msg else msg, None, None)
        except:
            self._success()

    def expect(self, b, msg="Unexpected result"):
        be = lambda a, e: b
        self._assert(be, b, None, msg)

    def _error(self, msg, expected, actual):
        print("*** ERROR: {}".format(msg.format(actual, expected)))
        self.__failures += 1

    def _success(self):
        print("Test Passed")
        self.__successes += 1

    def report(self):
        end = datetime.now()
        print("\nTest run complete")
        print("Passed: {}".format(self.__successes))
        print("Failed: {}".format(self.__failures))
        print("Total:  {}".format(self.__successes + self.__failures))

        delta = end - self.__start
        print("Process took {:,}ms to complete".format((delta.microseconds + 1000000 * delta.seconds) // 1000))
        if self.__failures == 0:
            print("Happy Days!")
        else:
            print("Better luck next time!")

test = Test()
atexit.register(test.report)
