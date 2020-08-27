import logging
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pyinstaller_template.template import say_hello, logger


def run(argv):
    parser = create_parser()
    args = parser.parse_args(argv)
    params = vars(args)

    verbose = params.pop('verbose')
    if verbose:
        logger.setLevel(level=logging.DEBUG)

    say_hello(**params)


def create_parser():
    parser = ArgumentParser(
        # Set the prog value so we don't get __main__.py in the usage
        prog=None if globals().get('__spec__') is None else 'python -m {}'.format(__spec__.name.partition('.')[0]),
        #TODO modify prog if run as exe
        formatter_class=ArgumentDefaultsHelpFormatter)
    # Command Arguments
    parser.add_argument('--name', '-n',  type=str, required=True, help='The name of the person you wish to say hello to')
    parser.add_argument('--verbose', '-v', help="Increase output verbosity", action="store_true")
    return parser