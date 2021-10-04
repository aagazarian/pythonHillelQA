def test_get_all_cookies(homepage):
    assert len(homepage._cookie.get_all_cookies()) > 0


def test_get_cookie(homepage):
    assert homepage._cookie.get_cookie('lang') == "v=2&lang=en-us"


def test_save_and_print_cookie(homepage):
    homepage._cookie.save_cookie("python", "3.9.2")
    assert homepage._cookie.get_cookie('python') == "3.9.2"


def test_get_all_from_local_storage(homepage):
    assert len(homepage._local_storage.items()) == 0


def test_save_to_local_storage(homepage):
    homepage._local_storage.set("year", "2021")
    assert homepage._local_storage.get("year") == "2021"
