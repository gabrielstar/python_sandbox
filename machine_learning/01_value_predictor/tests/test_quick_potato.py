from QuickPotato import performance_test as pt
import pytest

"""
    Performance Unit Tests
    https://github.com/JoeyHendricks/QuickPotato
"""
sleepTimes = [0.2, 0.5, 0.7]


@pytest.mark.parametrize("sleepTime", sleepTimes)
def test_performance_of_function_predict(sleepTime, predict):
    pt.test_case_name = f"test_performance_of_function_predict-{sleepTime}"
    pt.max_and_min_boundary_for_average = {"max": float(0.8), "min": float(0.1)}
    pt.measure_method_performance(
        method=predict,  # <-- The Method which you want to test.
        arguments=[float(sleepTime)],  # <-- Your arguments go here.
        iteration=10,  # <-- The number of times you want to execute
        pacing=0,  # <-- How much seconds you want to wait between iterations.
    )
    assert pt.verify_benchmark_against_set_boundaries()
