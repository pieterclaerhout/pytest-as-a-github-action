import utilities

def test_uuid():
    uuid = utilities.create_uuid()
    assert len(uuid) == 32
    assert uuid.find('-') == -1
 