import logging

import requests, app


class ProductApi:
    """商品Api接口方法"""

    def __init__(self):
        # 获取商品分类url
        self.get_product_classify_url = app.base_url + "/category/all"
        # 获取商品分类下的商品url
        self.get_products_goods_url = app.base_url + "/product/by_category"
        # 获取商品信息url
        self.get_product_info_url = app.base_url + "/product/{}"

    def get_product_classify(self):
        """获取商品分类"""
        logging.info("商品-获取商品分类")
        return requests.get(self.get_product_classify_url)

    def get_products_goods(self, id=2):
        """获取商品分类下的商品"""
        logging.info("商品-获取商品分类下的商品")
        data = {"id": id}
        logging.info("请求数据：{}".format(data))
        return requests.get(self.get_products_goods_url, params=data)

    def get_product_info(self, num=2):
        """获取商品信息"""
        logging.info("商品-获取商品信息")
        return requests.get(self.get_product_info_url.format(num))
