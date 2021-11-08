import nox

"""
    Run tests in a clean room environment for reproducibility
    Run with 'nox -r' to re-use environment.
"""


@nox.session(python=["3.8.8"], venv_backend="conda")
def tests(session):
    # user_deps = ["pytest", "pytest-xdist", "flask"]
    # session.conda_install(*user_deps)
    # conda_deps = ["tensorflow", "numpy"]
    # session.conda_install(*conda_deps)
    # tests = ["test_locust.py", "test_unit_pytest.py", "test_flask_pytest.py"]
    # session.run("pytest", *tests)
    session.conda_install("--channel=conda-forge", "locust")
    locust_params = "--headless -u 1 -r 1 --run-time 5s -f test_locust.py"
    session.run("locust", "--headless -r 1 -u 1 -t 5s -f .\locustfile.py")
