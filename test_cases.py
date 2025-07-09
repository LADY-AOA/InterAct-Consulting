from playwright.sync_api import expect


# Test: Search supports multiple keywords
def test_verify_search_functionality_handles_multiple_keywords_input(setup):
    # Fill keywords and location with valid input
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").press("CapsLock")
    setup.locator("input[name=\"k\"]").fill("QA Engineer")
    setup.locator("input[name=\"l\"]").click()
    setup.locator("input[name=\"l\"]").fill("Sheffield")
    setup.get_by_role("button", name="Submit").click()


# Test: Search returns relevant results for a valid keyword
def test_verify_search_functionality_returns_relevant_keywords_when_valid_keywords_are_produced(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").fill("Automation ")
    setup.get_by_role("button", name="Submit").click()
    # Assert that expected job titles appear
    expect(setup.get_by_role(
        "link", name="QA Automation Engineer Guildford | 55-60k We are looking for an enthusiastic")).to_be_visible()
    expect(setup.get_by_role(
        "link", name="QA Automation Engineer Playwright C# London, Hybrid | 50-55k + Pension,")).to_be_visible()


# Test: Search returns relevant results for a valid location
def test_verify_search_functionality_returns_relevant_results_when_valid_location_are_produced(setup):
    setup.locator("input[name=\"l\"]").click()
    setup.locator("input[name=\"l\"]").fill("Manchester")
    setup.get_by_role("button", name="Submit").click()
    # Check that jobs for Manchester are displayed
    expect(setup.get_by_role("link", name="Senior Backend NestJS")).to_be_visible()
    expect(setup.get_by_role(
        "link", name="Senior React Engineer Fully")).to_be_visible()
    expect(setup.get_by_text("There are 2 jobs that match")).to_be_visible()


# Test: Search works when both fields are empty
def test_verify_search_functionality_behavior_when_no_input_is_provided(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"l\"]").click()
    setup.get_by_role("button", name="Submit").click()
    # Expect to see all job listings (default behavior)
    expect(setup.get_by_text("There are 11 jobs that match")).to_be_visible()


# Test: Search returns no results for invalid keyword
def test_verify_search_functionality_behavior_when_invalid_keywords_are_provided(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").fill("asdfghjkl")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Search returns no results for invalid location
def test_verify_search_functionality_behavior_when_invalid_loaction_are_provided(setup):
    setup.locator("input[name=\"l\"]").click()
    setup.locator("input[name=\"l\"]").fill("Nowhereville")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Handles special characters in keywords
def test_verify_search_functionality_handles_special_characters_in_the_keywords_field(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").fill("QA@Engineer#")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Handles special characters in location
def test_verify_search_functionality_handles_special_characters_in_the_location_field(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"l\"]").click()
    setup.locator("input[name=\"l\"]").fill("London!@#")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Search handles very long strings in keywords
def test_verify_search_functionality_handles_long_input_strings_in_the_keywords_field(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").fill("...very long string...")
    setup.locator("input[name=\"l\"]").click()
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Search handles very long strings in location
def test_verify_search_functionality_handles_long_input_strings_in_the_location_field(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"l\"]").click()
    setup.locator("input[name=\"l\"]").fill("...very long string...")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Check if search is case sensitive in keyword field
def test_verify_if_search_functionality_is_case_sensitive_for_keywords(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"k\"]").fill("developer")
    setup.get_by_role("button", name="Submit").click()
    lower_case_result = setup.get_by_text(
        "There are no jobs that match").inner_text()

    setup.locator("input[name=\"k\"]").fill("DEVELOPER")
    setup.locator("input[name=\"l\"]").click()
    setup.get_by_role("button", name="Submit").click()
    upper_case_result = setup.get_by_text(
        "There are no jobs that match").inner_text()

    setup.locator("input[name=\"k\"]").fill("Developer")
    setup.get_by_role("button", name="Submit").click()
    capitalized_result = setup.get_by_text(
        "There are no jobs that match").inner_text()

    # Assert all cases return same result
    assert lower_case_result == upper_case_result == capitalized_result


# Test: Check if search is case sensitive in location field
def test_verify_if_search_functionality_is_case_sensitive_for_location(setup):
    setup.locator("input[name=\"l\"]").fill("london")
    setup.get_by_role("button", name="Submit").click()
    lower_case = setup.get_by_text("There are 4 jobs that match").inner_text()

    setup.locator("input[name=\"l\"]").fill("LONDON")
    setup.get_by_role("button", name="Submit").click()
    upper_case = setup.get_by_text("There are 4 jobs that match").inner_text()

    setup.locator("input[name=\"l\"]").fill("London")
    setup.get_by_role("button", name="Submit").click()
    capitalized = setup.get_by_text("There are 4 jobs that match").inner_text()

    # Assert all cases return same result
    assert lower_case == upper_case == capitalized


# Test: Ensure XSS input is not executed or allowed
def test_verify_search_functionality_resilience_against_XSS_attacks_in_the_keywords_field(setup):
    setup.locator("input[name=\"k\"]").fill("<script>alert('XSS')</script>")
    setup.locator("input[name=\"l\"]").click()
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Ensure SQL injection is safely handled
def test_verify_search_functionality_resilience_against_SQL_injection_attacks_in_the_keywords_field(setup):
    setup.locator("input[name=\"k\"]").fill(" '' OR '1'='1")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Trimming input should not affect results
def test_verify_search_functionality_correctly_handles_leading_and_trailing_spaces_in_the_input_fields(setup):
    setup.locator("input[name=\"k\"]").fill("  QA Engineer ")
    setup.locator("input[name=\"l\"]").fill("  London  ")
    setup.get_by_role("button", name="Submit").click()
    # Check that valid results are still returned
    expect(setup.locator("#content div").filter(
        has_text="There are no jobs that match")).not_to_be_visible()


# Test: Empty fields should return default results
def test_verify_search_functionality_when_keywords_and_location_fields_are_empty(setup):
    setup.locator("input[name=\"k\"]").click()
    setup.locator("input[name=\"l\"]").click()
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are 11 jobs that match")).to_be_visible()


# Test: Numbers in keywords should be handled
def test_verify_search_functionality_handles_numeric_inputs_in_the_keywords_field(setup):
    setup.locator("input[name=\"k\"]").fill("12345")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Numbers in location should be handled
def test_verify_search_functionality_handles_numeric_inputs_in_the_location_field(setup):
    setup.locator("input[name=\"l\"]").fill("12345")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_be_visible()


# Test: Search result persists when using browser back/forward
def test_verify_search_functionality_persists_when_using_browser_back_and_forward_buttons(setup):
    search_results = setup.get_by_text(
        "There are 11 jobs that match").all_inner_texts()
    setup.get_by_role("link", name="HOME", exact=True).click()
    setup.go_back()
    setup.wait_for_load_state("networkidle")
    back_results = setup.get_by_text(
        "There are 11 jobs that match").all_inner_texts()
    assert search_results == back_results


# Test: Handles multiple words in the keyword field
def test_verify_search_functionality_correctly_handles_multiple_words_in_the_keywords_fields(setup):
    setup.locator("input[name=\"k\"]").press("CapsLock")
    setup.locator("input[name=\"k\"]").fill("Automation ")
    setup.locator("input[name=\"k\"]").fill("Automation Test ")
    setup.locator("input[name=\"k\"]").fill("Automation Test Engineer")
    setup.get_by_role("button", name="Submit").click()
    expect(setup.get_by_text("There are no jobs that match")).to_not_be_visible()
