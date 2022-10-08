def test_expected_page():
    with open('fixture.html', "r", encoding='utf-8') as file:
        expected_page = file.read()
    with open('output.html', "r", encoding='utf-8-sig') as file:
        output_page = file.readlines()[:-1]

    assert expected_page == '\n'.join(output_page)
