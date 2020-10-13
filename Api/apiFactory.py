from Api.home import HomeApi
from Api.order import OrderApi
from Api.product import ProductApi
from Api.user import UserApi


class ApiFactory:

    @classmethod
    def get_home_api(cls):
        """返回首页Api"""
        return HomeApi()

    @classmethod
    def get_product_api(cls):
        """返回商品Api"""
        return ProductApi()

    @classmethod
    def get_user_api(cls):
        return UserApi()

    @classmethod
    def get_order_api(cls):
        return OrderApi()
