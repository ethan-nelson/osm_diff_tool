import gzip
import osmdt


def test_process():
    f = gzip.GzipFile('tests/040.osc.gz')
    data = osmdt.process(f)

    assert data


def test_extract_changesets():
    f = gzip.GzipFile('tests/040.osc.gz')
    data = osmdt.process(f)
 
    changesets = osmdt.extract_changesets(data)

    assert 13123866 in changesets
    assert len(changesets) == 8


def test_extract_users():
    f = gzip.GzipFile('tests/040.osc.gz')
    data = osmdt.process(f)
 
    users = osmdt.extract_users(data)

    assert 'sammuell_imports' in users
    assert len(users) == 8


def test_extract_objects():
    f = gzip.GzipFile('tests/040.osc.gz')
    data = osmdt.process(f)
 
    objects = osmdt.extract_objects(data)

    assert 'n171200037' in objects
    assert 'w181174997' in objects
    assert len(objects) == 1742
