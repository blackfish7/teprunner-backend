import allure

from utils.cache import TepCache
from utils.function import data
from utils.http_client import request
from utils.step import Step

"""
测试登录到下单流程，需要先启动后端服务
"""


@allure.title("从登录到下单支付")
def test(login_headers, env_vars, case_vars):
    case_vars.put("headers", login_headers)
    cache = TepCache(env_vars=env_vars, case_vars=case_vars)

    Step("搜索商品", step_search_sku, cache)
    Step("添加购物车", step_add_cart, cache)
    Step("下单", step_order, cache)
    Step("支付", step_pay, cache)


def step_search_sku(cache: TepCache):
    url = cache.env_vars["domain"] + cache.env_vars["mockApi"] + "/searchSku"
    headers = cache.case_vars.get("headers")
    body = data("查询SKU")

    response = request("get", url=url, headers=headers, params=body)
    assert response.status_code < 400

    cache.case_vars.put("skuId", response.jsonpath("$.skuId"))
    cache.case_vars.put("skuPrice", response.jsonpath("$.price"))


def step_add_cart(cache: TepCache):
    url = cache.env_vars["domain"] + cache.env_vars["mockApi"] + "/addCart"
    headers = cache.case_vars.get("headers")
    body = data("添加购物车")
    body["skuId"] = cache.case_vars.get("skuId")

    response = request("post", url=url, headers=headers, json=body)
    assert response.status_code < 400

    cache.case_vars.put("skuNum", response.jsonpath("$.skuNum"))
    cache.case_vars.put("totalPrice", response.jsonpath("$.totalPrice"))


def step_order(cache: TepCache):
    url = cache.env_vars["domain"] + cache.env_vars["mockApi"] + "/order"
    headers = cache.case_vars.get("headers")
    body = data("下单")
    body["skuId"] = cache.case_vars.get("skuId")
    body["price"] = cache.case_vars.get("skuPrice")
    body["skuNum"] = cache.case_vars.get("skuNum")
    body["totalPrice"] = cache.case_vars.get("totalPrice")

    response = request("post", url=url, headers=headers, json=body)
    assert response.status_code < 400

    cache.case_vars.put("orderId", response.jsonpath("$.orderId"))


def step_pay(cache: TepCache):
    url = cache.env_vars["domain"] + cache.env_vars["mockApi"] + "/pay"
    headers = cache.case_vars.get("headers")
    body = data("支付")
    body["orderId"] = cache.case_vars.get("orderId")

    response = request("post", url=url, headers=headers, json=body)
    assert response.status_code < 400
    assert response.jsonpath("$.success") == "true"