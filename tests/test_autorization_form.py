from selene import browser, be, have
import os


def test_fill_authorization_form():
    browser.open('/automation-practice-form')

    browser.element("#firstName").click().type('Yana')
    browser.element("#lastName").type('Surname')
    browser.element("#userEmail").type('test@ya.com')
    browser.element("label[for='gender-radio-2']").click()
    browser.element("#userNumber").type('89771452365')
    browser.element("#dateOfBirthInput").click()

    browser.element(".react-datepicker__year-select").type('1997').click()
    browser.element('.react-datepicker__month-select').type('January').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--006"]').click()

    browser.element('#subjectsInput').type('English').press_enter()
    browser.element("label[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/65NkbF_oOdw.jpg'))
    browser.element('#currentAddress').type('Smolnaya street')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text(
        'Thanks for submitting the form'))
    browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
        'Yana Surname', 'test@ya.com', 'Female', '8977145236', '06 January,1997', 'English', 'Music',
        '65NkbF_oOdw.jpg', 'Smolnaya street', 'Uttar Pradesh Agra'))





