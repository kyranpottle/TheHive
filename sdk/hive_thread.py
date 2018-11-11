""" This is the Threading for hive """

import inspect
from textwrap import dedent
import sys
import subprocess
from tempfile import NamedTemporaryFile
import threading

thread_pool = []

class HiveThread(object):
    """ This object exposes the threading API for TheHive """

    def __init__(self):
        self.finished = False
        self.result = None
        self.join_lock = threading.Condition()

    def join(self):
        """ This is the function to call to join threads """
        with self.join_lock:
            while not self.finished:
                self.join_lock.wait()

    def set_result(self, returned_result):
        """ This function is used by the content producer to propagate the result back """
        with self.join_lock:
            self.finished = True
            self.result = returned_result
            self.join_lock.notifyAll()

    def get_result(self):
        """ This function can be used to get the value returned by the thread """
        if not self.finished:
            self.join()

        return self.result

    def run(self, farg, **kwargs):
        """ This is the function that packages and sends off a thread. """
        lines = dedent(inspect.getsource(self.main))
        lines += """
farg = {}
kwargs = {}

print(main(farg, **kwargs))

""".format(farg, kwargs)

        #print(lines)
        thread_pool.append(self)
        with NamedTemporaryFile(mode='w') as script_file:
            script_file.write(lines)
            script_file.flush()
            result = subprocess.check_output([sys.executable, script_file.name]).decode(sys.stdout.encoding)
            print("out: ", result)

    def main(farg, **kwargs):
        """ This is the function where the user writes the code """
        pass
