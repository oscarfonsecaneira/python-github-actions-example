import sys
sys.path.insert(1, '/Users/57300/Documents/GitHub/python-github-actions-example/src')

from app import index

def test_index():
    assert index() == "Hello, world!"