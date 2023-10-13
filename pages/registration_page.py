import os

from selene import browser, be, have

from data.uses import UserInfo


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self, name, surname):
        browser.element("#firstName").click().type(name)
        browser.element("#lastName").type(surname)
        return self

    def fill_email(self, email):
        browser.element("#userEmail").type(email)
        return self

    def select_gender_button(self, number):
        browser.element(f"label[for='gender-radio-{number}']").click()
        return self

    def fill_mobile_number(self, mobile_number):
        browser.element("#userNumber").type(mobile_number)
        return self

    def fill_date_of_birth(self, birth_year, birth_month, birth_day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(birth_year).click()
        browser.element('.react-datepicker__month-select').type(birth_month).click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--00{birth_day}"]').click()
        return self

    def fill_subject_field(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def select_hobbies(self, hobbies_number):
        browser.element(f"label[for='hobbies-checkbox-{hobbies_number}']").click()
        return self

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/65NkbF_oOdw.jpg'))
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit_the_form(self):
        browser.element('#submit').should(be.visible).click()
        return self

    def check_registered_user_info(self, user: UserInfo):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text(
            'Thanks for submitting the form'))
        browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
            f"{user.first_name} {user.last_name}",
            user.email,
            user.gender,
            user.phone_number,
            f"{user.birth_day} {user.birth_month},{user.birth_year}",
            user.subject,
            user.hobbies_number,
            user.picture,
            user.address,
            f"{user.state} {user.city}",
        ))
        return self
