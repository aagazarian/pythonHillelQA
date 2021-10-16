def test_email(homepage):
    homepage.open()
    homepage.fill_email("sdf")
    homepage.click_get_started_button()

    assert homepage.is_error_message_displayed(), "Error message isn't displayed"
    assert homepage.get_error_message_text() == "Please enter a valid email address"
