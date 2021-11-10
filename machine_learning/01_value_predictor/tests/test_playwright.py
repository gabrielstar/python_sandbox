import pages.search as p
import pytest


@pytest.mark.parametrize("search_phrase", {"dummy", "mummy"})
def test_search(page, search_phrase):
    search_page = p.SearchPage(page)
    search_page.navigate()
    search_page.search(search_phrase)
