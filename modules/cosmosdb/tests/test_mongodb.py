import pytest
from testcontainers.cosmosdb import CosmosDBMongoEndpointContainer
from testcontainers.core.config import testcontainers_config


@pytest.fixture(scope="session", autouse=True)
def config_testcontatiners():
    testcontainers_config.max_tries = 300


def test_requires_a_version():
    with pytest.raises(AssertionError, match="A MongoDB version is required"):
        CosmosDBMongoEndpointContainer(mongodb_version=None)

    # instanciates
    CosmosDBMongoEndpointContainer(mongodb_version="4.0")


def test_runs():
    with CosmosDBMongoEndpointContainer(mongodb_version="4.0", partition_count=1) as emulator:
        assert emulator.env["AZURE_COSMOS_EMULATOR_ENABLE_MONGODB_ENDPOINT"] == "4.0"
        assert emulator.get_exposed_port(10255) is not None, "The MongoDB endpoint's port should be exposed"
