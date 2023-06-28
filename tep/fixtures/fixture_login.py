import pytest
from loguru import logger

from utils.http_client import request


@pytest.fixture(scope="session")
def login(tep_context_manager, env_vars):
    """
    tep_context_manager是为了兼容pytest-xdist分布式执行的上下文管理器
    该login只会在整个运行期间执行一次
    """

    def produce_expensive_data(variable):
        logger.info("----------------开始登录----------------")
        response = request(
            "post",
            url=variable["domain"] + "/api/users/login",
            headers={"Content-Type": "application/json"},
            json={"username": "admin", "password": "qa123456"}
        )
        assert response.status_code < 400
        logger.info("----------------登录成功----------------")
        return response.json()

    return tep_context_manager(produce_expensive_data, env_vars)


@pytest.fixture(scope="session")
def login_headers(login):
    return {"Authorization": "Bearer " + login["token"]}