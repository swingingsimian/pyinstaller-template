import pytest

from pyinstaller_template import template
logger = template.logger
logger.setLevel('DEBUG')


def test_template_hello(capsys):
    template.say_hello(name='Nathan')
    out, err = capsys.readouterr()
    assert out == 'Hello Nathan!\n'
    assert err is ''


