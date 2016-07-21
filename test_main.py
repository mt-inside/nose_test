import sys
import os

from testconfig import config

from main import Utils

class TestUnit:
    @classmethod
    def setUpClass(cls):

        print sys.argv
        print "class static setup"
        print config['javaagent']

    def setUp(self):
        print sys.argv
        print "per instance setup"
        self.u = Utils()

    def test_fib_iter(self):
        print sys.argv
        #for k in os.environ:
        #    print "%s : %s" % (k, os.environ[k])
        assert self.u.fib_iter(5) == 8

    def tearDown(self):
        print "per instance teardown"
        pass

    @classmethod
    def tearDownClass(cls):
        print "class static teardown"
