# Pytest config file


def pytest_configure(config):
    config.addinivalue_line("markers", "integration")
    config.addinivalue_line("markers", "unit")
