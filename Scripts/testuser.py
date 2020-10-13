import logging
import pytest

import app
from Api.apiFactory import ApiFactory

@pytest.mark.run(order=0)
class TestUser:
    def test_get_token(self):
        """获取token"""
        res = ApiFactory.get_user_api().get_token_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 打印token
        print("获取的token:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言token
        assert "token" in res.json()
        # 保存token
        app.headers["token"] = res.json().get("token")

    def test_verify_token(self):
        """验证token"""
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言isvalid
        assert res.json().get("isValid") is True

    def test_get_adress_info(self):
        """获取地址信息"""
        res = ApiFactory.get_user_api().get_adress_info_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言name、mobile、province、country、detail
        assert res.json().get("name") == "大王"
        assert res.json().get("mobile") == "13888888888"
        assert res.json().get("province") == "上海市"
        assert res.json().get("country") == "浦东新区"
        assert res.json().get("detail") == "111号"
