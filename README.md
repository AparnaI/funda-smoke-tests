# funda-smoke-tests

Smoke test automation for Funda website.

## Prerequisites

- Python
- pip
- Poetry

## Installation

Follow these instructions to set up the project:

```bash
# Clone the repository
git clone https://github.com/AparnaI/funda-smoke-tests.git

# Navigate to the project directory
cd funda

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies using Poetry
poetry install
```

Why Use a Virtual Environment?
Using a virtual environment (venv) is important for the following reasons:

Isolation: It isolates your project’s dependencies from other projects and the global Python environment, preventing conflicts between different versions of packages.
Dependency Management: It allows you to manage dependencies on a per-project basis, ensuring each project has its own set of dependencies.
Reproducibility: It ensures that your project runs with the exact versions of packages specified in your requirements.txt or pyproject.toml file, making it easier to reproduce the environment on different machines.
Cleaner Global Environment: It keeps your global Python environment clean and free from unnecessary packages that are only needed for specific projects.



Usage

To run the tests, use the following command:
# Run the tests
pytest

Using pytest Tags
You can use pytest tags to categorize and selectively run tests. Tags are defined in the pytest.ini file and added to tests using the pytest.mark decorator.

[pytest]
markers =
    smoke: mark a test as a smoke test
    regression: mark a test as a regression test

Running Tests with Specific Tags
To run tests with a specific tag, use the -m option:

pytest -m smoke
pytest -m regression


Project Structure
features: Contains the feature files for BDD scenarios.
    test_steps_TC1_home_page.py: Test steps for homepage loading.
    test_steps_TC2_search_function.py: Test steps for search functionality.
    test_steps_TC3_property_details.py: Test steps for property details page.
    test_steps_TC4_contact_form.py : Test steps for verifying contact form 
    test_steps_TC5_important_links.py: Test steps for important links on the homepage.
pages: Contains the page object models.
    base_page.py: Base page class with common functionalities.
    home_page.py: Page object model for the homepage.
    search_result_page.py: Page object model for the search results page.
    details_page.py: Page object model for the property details page.
    listing_page.py: Page object model for the property listing page.
    contact_page.py: Page object model for the contact form page.
config.py: Configuration file for the project.
conftest.py: Contains fixtures for the project.
poetry.lock: Contains the exact versions of dependencies used in the project.
pyproject.toml: Configuration file for Poetry, specifying project dependencies and settings.


Selecting the Python Interpreter
If you are using Visual Studio Code, follow these steps to select the Python interpreter:

Open the Command Palette (Ctrl+Shift+P).
Type Python: Select Interpreter and select it.
Choose the interpreter from the list that corresponds to your virtual environment (e.g., .venv).