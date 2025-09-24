# resortpass-automation

This is a Python framework that tests one of the most important ResortPass.com's functionality: search.

## Structure

```
resortpass/
├── pages/
│   ├── base_page.py            # Helper methods
│   ├── home_page.py            # Homepage interactions and locators
│   └── search_results_page.py  # Search results handling
├── tests/
│   └── smoke_tests.py          # Test case
├── config/
│   └── config.json             # Test configuration
├── conftest.py                 # Pytest fixtures
└── pytest.ini                  # Pytest configuration
```

## Test Case

**`test_search_valid_city`**

- Searches for "New York"
- Clicks search button
- Verifies results are found
- Prints first 30 hotel results

## Key Features

- **Automatic overlay handling** - dismisses promo popups
- **Robust element selection** - handles dynamic DOM changes
- **Clean page object model** - reusable methods
- **Comprehensive logging** - detailed test output

## Run Tests

```bash
pytest -s
```

## Requirements

- Python 3.13+
- Selenium WebDriver
- Chrome browser
