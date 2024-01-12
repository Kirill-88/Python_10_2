from selene import browser, be, have


def test_correct_search_google(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_google_random_words(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(
        'лаваівавіаіваіваіваіваddfgfdgfdgfdfdgfd4fsdfdsfhrgfhfhtrва4уацуауцацуауцацуhtrfgh').press_enter()
    browser.element('[aria-level="3"]').should(
        have.text('По запросу лаваівавіаіваіваіваіваddfgfdgfdgfdfdgfd4fsdfdsfhrgfhfhtrва4уацуауцацуауцацуhtrfgh '
                  'ничего не найдено.'))
