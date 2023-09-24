from pages.registration_page import RegistrationPage


def test_fill_authorization_form():
    registration_form = RegistrationPage()

    registration_form.open_form()

    registration_form.fill_name('Yana', 'Kormsh')
    registration_form.fill_email('test@ya.com')
    registration_form.select_gender_button(2)
    registration_form.fill_mobile_number('89783646677')
    registration_form.fill_date_of_birth('1997', 'January', '006')
    registration_form.fill_subject_field('English')
    registration_form.select_hobbies('3')
    registration_form.upload_picture()
    registration_form.fill_address('Moscow, Smolnaya street, 5')
    registration_form.select_state('Uttar Pradesh', 'Agra')

    registration_form.submit_the_form()

    registration_form.check_registered_user_info('Yana Kormsh', 'test@ya.com', 'Female', '89783646677',
                                                 '06 January,1997', 'English', 'Music', '65NkbF_oOdw.jpg',
                                                 'Moscow, Smolnaya street, 5', 'Uttar Pradesh Agra')

