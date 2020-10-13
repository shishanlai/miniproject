import logging

import requests, app


class UserApi:
    """用户Api接口"""

    def __init__(self):
        # 获取token的url
        self.get_token_url = app.base_url + "/token/user"
        # token验证url
        self.token_verify_url = app.base_url + "/token/verify"
        # 获取地址信息url
        self.adress_info_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        logging.info("用户——获取token")
        return requests.post(self.get_token_url, headers=app.headers,
                             json={"code": app.code})

    def token_verify_api(self):
        """验证token"""
        logging.info("用户——验证token")
        return requests.post(self.token_verify_url, headers=app.headers,
                             json={"token": app.headers.get('token')})

    def get_adress_info_api(self):
        """获取地址信息"""
        logging.info("用户——获取地址信息")
        return requests.get(self.adress_info_url, headers={"token": app.headers.get('token')})
