""" This is the Threading for hive """

import inspect
from textwrap import dedent
import sys
import subprocess
from tempfile import NamedTemporaryFile

class HiveThread(object):
    """ This object exposes the threading API for TheHive """

    def __init__(self):
        pass

    def join(self):
        """ This is the function to call to join threads """
        pass

    def result(self):
        """ This function can be used to get the value returned by the thread """
        pass

    def run(self, farg, **kwargs):
        """ This is the function that packages and sends off a thread. """
        lines = dedent(inspect.getsource(self.main))
        lines += """
farg = {}
kwargs = {}

print(main(farg, **kwargs))

""".format(farg, kwargs)

        #print(lines)
        with NamedTemporaryFile(mode='w') as script_file:
            script_file.write(lines)
            script_file.flush()
            result = subprocess.check_output([sys.executable, script_file.name]).decode(sys.stdout.encoding)
            print("out: ", result)

    def main(farg, **kwargs):
        """ This is the function where the user writes the code """
        pass
