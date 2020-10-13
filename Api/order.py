import logging

import requests, app


class OrderApi:
    def __init__(self):
        # 获取订单列表url
        self.get_order_list_url = app.base_url + "/order/by_user"
        # 创建订单url
        self.create_list_url = app.base_url + "/order"
        # 查看订单url
        self.look_list_url = app.base_url + "/order/{}"

    def get_order_list_api(self, num=1):
        """获取订单列表"""
        logging.info("订单-获取订单列表")
        data = {"page": num}
        return requests.get(self.get_order_list_url, headers=app.headers, params=data)

    def create_list_api(self,product_id=8,count=1):
        """创建订单"""
        logging.info("订单-创建订单")
        return requests.post(self.create_list_url, headers=app.headers,
                             json={"products": [{"product_id": product_id, "count": count}]})

    def look_list_api(self, num=50):
        """查看订单"""
        logging.info("订单-查看订单")
        return requests.get(self.look_list_url.format(num), headers=app.headers)
