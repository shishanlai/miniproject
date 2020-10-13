import logging
from Api.apiFactory import ApiFactory


class TestOrder:

    def test_get_order_list(self):
        """获取订单列表"""
        res = ApiFactory.get_order_api().get_order_list_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert False not in [i in res.text for i in ["id", "order_no", "create_time", "total_price"]]

    def test_create_list(self):
        """创建订单"""
        res = ApiFactory.get_order_api().create_list_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert False not in [i in res.text for i in ["order_no", "order_id", "create_time", "pass"]]

    def test_look_list(self):
        """查看订单"""
        res = ApiFactory.get_order_api().look_list_api()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert False not in [i in res.text for i in ["id", "order_no", "total_price", "status", "snap_name"]]
