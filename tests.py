def test_expected_page():
    with open('tt.html', "r", encoding='utf-8-sig') as file:
        expected_page = file.read()
    with open('output.html', "r", encoding='utf-8-sig') as file:
        output_page = file.read()

    assert expected_page == output_page
