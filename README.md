# InterAct-Consulting: Search Functionality Test Automation

## Overview

This repository contains automated test cases for the search functionality of the InterAct Consulting website, specifically targeting the job search page (`https://www.interactconsulting.co.uk/our-process-p5.aspx`). The tests are developed using Python and Playwright, a robust browser automation library, to ensure the reliability and correctness of the search feature.

## Project Structure

```
InterAct-Consulting/
├── .pytest_cache/       # pytest cache directory
├── __pycache__/         # Python cache directory
├── conftest.py          # pytest configuration and fixtures
├── search_functionality.py # Core Playwright automation logic for search
├── test_cases.py        # Automated test cases for search functionality
└── README.md            # This README file
```

## Technologies Used

*   **Python:** Programming language for test development.
*   **Playwright:** Python library for browser automation, enabling end-to-end testing.
*   **Pytest:** Testing framework for organizing and running tests.

## Features

*   **Automated Search Testing:** Comprehensive test suite covering various scenarios for the website's search functionality.
*   **Cross-Browser Compatibility:** Playwright supports testing across Chromium, Firefox, and WebKit.
*   **Robust Test Cases:** Includes tests for valid/invalid inputs, edge cases, and security considerations (XSS, SQL Injection).


## Installation

To set up and run the tests locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/LADY-AOA/InterAct-Consulting.git
    cd InterAct-Consulting
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    playwright install  # Install browser binaries
    ```

## Usage

To run the automated tests, navigate to the project root directory in your terminal and execute the following command:

```bash
pytest
```

### Running Specific Tests

You can run specific test files or test cases using pytest's filtering options:

*   **Run all tests in a file:**
    ```bash
    pytest test_cases.py
    ```
*   **Run a specific test case by name:**
    ```bash
    pytest test_cases.py::test_valid_keywords_location
    pytest -k test_valid_keywords_location
    ```

### Headless vs. Headed Mode

By default, Playwright runs browsers in headless mode (without a visible UI). To run tests in headed mode (with a visible browser UI), you can modify your `conftest.py` or pass a command-line argument to pytest (if configured):

```bash
pytest --headed
```

## Test Cases

The `search_test_cases.py` file contains a suite of tests covering various aspects of the search functionality. These include:

*   Valid keyword and location searches
*   Searches with only keywords or only location
*   Searches with no input
*   Invalid/non-existent keywords and locations
*   Handling of special characters and long input strings
*   Case sensitivity checks
*   Security vulnerability tests (XSS, SQL Injection)
*   Browser navigation and persistence of search results


