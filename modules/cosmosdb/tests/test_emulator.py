import pytest
from testcontainers.cosmosdb._emulator import CosmosDBEmulatorContainer
from testcontainers.core.config import testcontainers_config


@pytest.fixture(scope="session", autouse=True)
def config_testcontatiners():
    testcontainers_config.max_tries = 300


def test_runs():
    with CosmosDBEmulatorContainer(partition_count=1) as emulator:
        assert emulator.server_certificate_pem is not None
        assert emulator.get_exposed_port(8081) is not None
