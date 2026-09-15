from hwi.load import load_all, check
def test_tables_load_and_join():
    db = load_all()
    assert len(db) == 12 and not check(db)
