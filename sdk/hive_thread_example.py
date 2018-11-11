from hive_thread import HiveThread

class Example(HiveThread):
    """ Example usage of HiveThread """

    def __init__(self):
        HiveThread.__init__(self)

    def main(farg, **kwargs):
        return(farg + kwargs["arg2"])

if __name__ == "__main__":
    Example().run(2, arg2=3)
