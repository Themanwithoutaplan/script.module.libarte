import sys
sys.argv.insert(1, 1)

from ..libartewebjsonparser import APIParser

def test_parseHome():

    parser = APIParser()
    result = parser.parseHome()
    assert result == {'favorites': [], 'lastvieweds': [], 'meta':
                     {'updatedAt': None}, 'nextEpisodes': [], 'subscriptions': []}
