import pytest
from testcontainers.cosmosdb import CosmosDBNoSQLEndpointContainer
from testcontainers.core.config import testcontainers_config


@pytest.fixture(scope="session", autouse=True)
def config_testcontatiners():
    testcontainers_config.max_tries = 300


def test_runs():
    with CosmosDBNoSQLEndpointContainer(partition_count=1) as emulator:
        assert emulator.port is not None, "The NoSQL endpoint's port should be exposed"
