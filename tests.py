def test_download():
    with open('fixture.html', "r", encoding="utf-16") as file:
        expected_page = file.read()
    with open('output.html', "r", encoding="'utf-16le'") as file:
        output_page = file.read()

    assert expected_page == output_page.encode('utf-8')
