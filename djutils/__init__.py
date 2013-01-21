VERSION = (0, 2, 0, 'f')  # following PEP 386
# VERSION = (0, 5, 2, "a", "1")


def get_version(short=False):
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if short:
        return version
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    if VERSION[3] != "f":
        version = "%s%s%s" % (version, VERSION[3], VERSION[4])
    return version

__version__ = get_version()
