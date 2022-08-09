from src.counter import count_ocurrences


def test_counter():
    javascript_counting = count_ocurrences('src/jobs.csv', "javascript")
    python_counting = count_ocurrences('src/jobs.csv', "python")
    assert javascript_counting == 122
    assert python_counting == 1639
