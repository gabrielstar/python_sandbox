import pages.main as p


def test_prediciton(page, arg="aaa"):
    main_page = p.MainPage(page)
    main_page.navigate()
    main_page.submit(arg)
