import logging
from Api.apiFactory import ApiFactory


class TestProduct:
    def test_get_product_classify(self):
        """获取商品分类"""
        res = ApiFactory.get_product_api().get_product_classify()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert False not in [i in res.text for i in ["id", "name", "topic_img_id", "description"]]

    def test__products_goods(self):
        """商品分类下商品"""
        res = ApiFactory.get_product_api().get_products_goods()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert False not in [i in res.text for i in ["id", "name", "price", "stock", "main_img_url"]]

    def test_get_product_info(self):
        """获取产品信息"""
        res = ApiFactory.get_product_api().get_product_info()
        # 打印请求地址  打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言
        assert res.json().get("id") == 2 and res.json().get("name") == "梨花带雨 3个" and res.json().get("price") == "0.01"
