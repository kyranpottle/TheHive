import inspect
from textwrap import dedent
import sys
from io import StringIO
import contextlib
import subprocess
from tempfile import NamedTemporaryFile

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class HiveThread(object):
    """ This object exposes the threading API for TheHive """

    def __init__(self):
        pass

    def join(self):
        """ This is the function to call to join threads """
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
        with NamedTemporaryFile(mode='w') as file:
            file.write(lines)
            file.flush()
            result = subprocess.check_output([sys.executable, file.name]).decode(sys.stdout.encoding)
            print("out: ", result)

    def main(farg, **kwargs):
        """ This is the function where the user writes the code """
        pass
