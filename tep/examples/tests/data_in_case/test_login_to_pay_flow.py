import allure

from utils.http_client import request

"""
测试登录到下单流程，需要先启动后端服务
"""


@allure.title("登录--搜索商品--添加购物车--下单--支付")
def test(env_vars, login_headers):
    # 搜索商品
    response = request(
        "get",
        url=env_vars["domain"] + env_vars["mockApi"] + "/searchSku",
        headers=login_headers,
        params={"skuName": "电子书"}
    )
    sku_id = response.jsonpath("$.skuId")
    sku_price = response.jsonpath("$.price")
    assert response.status_code < 400

    # 添加购物车
    sku_num = 3
    response = request(
        "post",
        url=env_vars["domain"] + env_vars["mockApi"] + "/addCart",
        headers=login_headers,
        json={"skuId": sku_id, "skuNum": str(sku_num)}
    )
    total_price = response.jsonpath("$.totalPrice")
    assert response.status_code < 400

    # 下单
    response = request(
        "post",
        url=env_vars["domain"] + env_vars["mockApi"] + "/order",
        headers=login_headers,
        json={"skuId": sku_id, "price": sku_price, "skuNum": str(sku_num), "totalPrice": total_price}
    )
    order_id = response.jsonpath("$.orderId")
    assert response.status_code < 400

    # 支付
    response = request(
        "post",
        url=env_vars["domain"] + env_vars["mockApi"] + "/pay",
        headers=login_headers,
        json={"orderId": order_id, "payAmount": "6.9"}
    )
    assert response.status_code < 400
    assert response.json()["success"] == "true"