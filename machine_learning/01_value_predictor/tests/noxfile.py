import nox

"""
    Run tests in a clean room environment for reproducibility
    Run with 'nox -r' to re-use environment.

    `nox --list`
    Run tests within conda install:  `nox -r -s conda_tests`
    Run install in clean virtual env: `nox -r -s perf_tests`
"""


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "../application")


@nox.session(python=["3.8.8"], venv_backend="conda")
def conda_tests(session):
    """
        Our app is developed within conda.
        This is how to run nox in existing conda env.
        This is much much faster.
    """

    user_deps = ["pytest", "pytest-xdist", "flask"]
    session.conda_install(*user_deps)
    conda_deps = ["tensorflow", "numpy"]
    session.conda_install(*conda_deps)
    tests = ["test_unit_pytest.py", "test_flask_pytest.py"]
    session.run("pytest", *tests)


@nox.session(python=["3.8.8"])
def noconda_tests(session):
    """
        Our app is developed within conda.
        This is how to run nox outside of conda env.
        This will be slower on first run.
    """
    user_deps = ["pytest", "pytest-xdist", "flask"]
    session.install(*user_deps)
    conda_deps = ["tensorflow", "numpy"]
    session.install(*conda_deps)
    tests = ["test_unit_pytest.py", "test_flask_pytest.py"]
    session.run("pytest", *tests)


@nox.session(python=["3.8.8"])
def potato_tests(session):
    """
        Our app is developed within conda.
        This is how to run nox outside of conda env.
        This will be slower on first run.
    """
    user_deps = ["pytest", "pytest-xdist", "QuickPotato", "flask"]
    session.install(*user_deps)
    tests = ["test_quick_potato.py"]
    session.run("pytest", *tests)


@nox.session(python=["3.8.8", "3.7"])
def perf_tests(session):
    """
        Locust has issues to run in conda so we run it outside of conda.
    """
    session.install("locust")
    args = ["--headless", "-u 2", "-r 1", "-t", "5s", "-f", "locustfile.py"]
    session.run("locust", *args)


@nox.session(python=["3.8.8"])
def e2e_tests(session):
    """
        Playwright e2e tests
    """
    session.install(
        "flask", "pytest", "pytest-xdist", "playwright", "pytest-playwright"
    )
    # session.run("pytest", "test_playwright.py", "--headed")
    session.run("pytest", "test_playwright.py", "-n 2")

